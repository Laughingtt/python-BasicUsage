# %%

import matplotlib

matplotlib.use('TkAgg')
import graphviz
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)


# %%
class Tree():
    def __init__(self, nid=None,
                 node_type='Leaf',
                 stats={'gini': None, 'total': None, 'good': None, 'bad': None, 'bad%': None},
                 split={'var': None, 'cutoff': None},
                 child1=None,
                 child2=None):
        '''
        nid: node ID, which starts with 1 for the root node, followed by 11 and 12 for layer 1 splits,
            and 111/112 + 121/122 for layer 2 splits, so on and so forth
        type: either 'Leaf' or 'node'
        stats: statistics for current node, including # of samples, gini, etc
        split: The variable and cutoff value to split. only valid for Leaf.
        child1: sub tree for 'left' branch: the tree with value <= split cutoff
        child2: sub tree for 'right' branch: the tree with value > split cutoff
        '''
        self.nid = nid
        self.type = node_type
        self.stats = stats
        if node_type == 'Node':
            self.split = split
            self.child1 = child1
            self.child2 = child2

    def __repr__(self):
        if self.stats is not None:
            return '{}'.format(self.stats)


class CART():
    def __init__(self, max_depth=7, min_samples_split=100, min_samples_leaf=50,
                 min_pct_leaf=0.01, min_gini_gain=0.0001, ccp_alpha=0.0001):
        self._max_depth = max_depth
        self._min_samples_split = min_samples_split
        self._min_samples_leaf = min_samples_leaf
        self._min_pct_leaf = min_pct_leaf
        self._min_gini_gain = min_gini_gain
        self._ccp_alpha = ccp_alpha
        self.hyper_param = {'max_depth': max_depth,
                            'min_samples_split': min_samples_split,
                            'min_samples_leaf': min_samples_leaf,
                            'min_pct_leaf': min_pct_leaf,
                            'min_gini_gain': min_gini_gain,
                            'ccp_alpha': ccp_alpha}

    def _calculate_node_gini(self, y):
        '''
        y: numpy array, holding binary 0/1 label
        '''
        s = np.array([(y == 0).sum(), (y == 1).sum()])
        node_gini = 1 - np.sum(np.square(s / s.sum()))
        return node_gini

    def _calculate_split_gini(self, var, y, cutoff, ret_size=False):
        '''
        var: np array, holding the value of split variable
        y: label
        cutoff: threshold value for split
        '''
        y1 = y[var <= cutoff]
        y2 = y[var > cutoff]

        s1 = np.array([(y1 == 0).sum(), (y1 == 1).sum()])
        s2 = np.array([(y2 == 0).sum(), (y2 == 1).sum()])
        sum1 = s1.sum()
        sum2 = s2.sum()
        split_gini = ((1 - np.sum(np.square(s1 / sum1))) * sum1 + \
                      (1 - np.sum(np.square(s2 / sum2))) * sum2) / (sum1 + sum2)
        if ret_size:
            return split_gini, len(y1), len(y2)
        else:
            return split_gini

    def _find_best_split(self, data, label, Vars):
        '''
        data: dataFrame, containing label
        label: variable name for label
        vars: list of X variables.
        '''
        X = np.array(data[Vars])
        y = np.array(data[label])

        def find_best_cutoff_by_var(var, y):
            values = np.array(list(set(var)))
            if len(values) == 1:
                return None, None
            values.sort()
            cutoffs = (values[:-1] + values[1:]) / 2
            ls = map(lambda x: [x, *self._calculate_split_gini(var, y, x, ret_size=True)], cutoffs)
            ls = filter(lambda x: x[2] >= self.true_min_samples_leaf and x[3] >= self.true_min_samples_leaf, ls)
            ls = list(ls)
            if len(ls) == 0:
                return None, None
            cutoff, gini, n_left, n_right = min(ls, key=lambda x: x[1])
            return cutoff, gini

        ls = map(lambda x: [x, *find_best_cutoff_by_var(X[:, x], y)], range(X.shape[1]))
        ls = filter(lambda x: x[2] is not None, ls)
        ls = list(ls)
        if len(ls) == 0:
            return None

        col, cutoff, split_gini = min(ls, key=lambda x: x[2])
        best_split = {'col': col, 'cutoff': round(cutoff, 4), 'gini': split_gini}
        return best_split

    def _stop_split(self, data, label, Vars, current_depth):
        '''
        停止split的条件判断：
        - node样本数低于min_samples_split
        - 树深达到max depth
        - 所有样本的label都一样
        - 没有X变量
        - 所有X变量都为单一值        
        '''
        if len(data) < self._min_samples_split:
            early_stop = True
        elif current_depth >= self._max_depth:
            early_stop = True
        elif len(data[label].unique()) == 1:
            early_stop = True
        elif len(Vars) == 0:
            early_stop = True
        elif max(len(data[var].unique()) for var in Vars) == 1:
            early_stop = True
        else:
            early_stop = False

        return early_stop

    # to generate the summary for all leaves: gini, # of samples, bads, etc
    def _summarize_leaves(self, tree, ls=[]):
        if tree.type == 'Leaf':
            ls.append({'nid': tree.nid,
                       'gini': tree.stats['gini'],
                       'total': tree.stats['total'],
                       'bad': tree.stats['bad']
                       })
            return ls
        else:
            ls = self._summarize_leaves(tree.child1, ls)
            ls = self._summarize_leaves(tree.child2, ls)
            return ls

    # the calculate CCP alpha for the specified node
    def _calculate_node_alpha(self, node):
        node_gini = node.stats['gini']
        ls = self._summarize_leaves(node, ls=[])
        tree_gini = sum([leaf['total'] * leaf['gini'] for leaf in ls]) / node.stats['total']
        # node_alpha = (node_gini - tree_gini) / (len(ls) - 1)
        node_alpha = (node_gini - tree_gini) / (len(self.leaf_info) - 1)
        return node_alpha

    # to generate summary for non-leaf-nodes: node id, and ccp alpha
    def _summarize_nodes(self, tree, ls_node=[]):
        if tree.type == 'Node':
            ls_node.append({'nid': tree.nid, 'alpha': self._calculate_node_alpha(tree)})
            ls_node = self._summarize_nodes(tree.child1, ls_node)
            ls_node = self._summarize_nodes(tree.child2, ls_node)
            return ls_node
        else:
            return ls_node

    # to generate summary for all nodes, including leaves and non-leave nodes
    def _summarize_all_nodes(self, tree, ls=[]):
        ls.append({'nid': tree.nid,
                   'type': tree.type,
                   'gini': tree.stats['gini'],
                   'total': tree.stats['total'],
                   'bad': tree.stats['bad']
                   })
        if tree.type == 'Node':
            ls = self._summarize_all_nodes(tree.child1, ls)
            ls = self._summarize_all_nodes(tree.child2, ls)
        return ls

    # find the node with the lowest effective CCP alpha:
    def _find_node_with_lowest_alpha(self, tree=None):
        if tree is None:
            tree = self.tree
        node_info = self._summarize_nodes(tree, ls_node=[])
        df = pd.DataFrame(node_info).sort_values('alpha', ascending=True)

        # top 3 nodes excluded from pruning
        # df = df[~df['nid'].isin([1, 11,12])]
        df = df[df['nid'] != 1]

        if len(df) > 0:
            nid_low = df['nid'].iloc[0]
            alpha_low = df['alpha'].iloc[0]
        else:
            nid_low = None
            alpha_low = None
        return nid_low, alpha_low

    # to prune the node with specified node_id
    def _prune_node(self, tree, node_id):
        if tree.nid == node_id:
            tree.type = 'Leaf'
            del tree.split
            del tree.child1
            del tree.child2

            df = pd.DataFrame(self._summarize_leaves(self.tree, ls=[]))
            df['%total'] = round(df['total'] / df['total'].sum() * 100, 2)
            df['bad%'] = round(df['bad'] / df['total'] * 100, 2)
            df.sort_values(by='bad%', ascending=False, inplace=True)
            self.leaf_info = df
            return self.tree
        elif tree.type == 'Node':
            self._prune_node(tree.child1, node_id)
            self._prune_node(tree.child2, node_id)
            return tree

    # to prune the tree based on CPP alpha
    def _prune_tree(self, verbose=False):
        nid_low, alpha_low = self._find_node_with_lowest_alpha(self.tree)
        while alpha_low is not None and alpha_low <= self._ccp_alpha:
            if verbose:
                print('node %d is pruned, with alpha = %.4f' % (nid_low, alpha_low))
            self.tree = self._prune_node(self.tree, nid_low)
            nid_low, alpha_low = self._find_node_with_lowest_alpha(self.tree)

    def fit(self, data, label, Vars):
        '''
        data: dataFrame, containing label
        label: variable name for label
        vars: list of X variables.
        '''
        # calculate the min # of samples in leaf based on user input
        self.m = len(data)
        self.true_min_samples_leaf = max(self._min_samples_leaf, self.m * self._min_pct_leaf)

        def train(data, label, Vars, node_id=1, current_depth=0):
            node_gini = self._calculate_node_gini(data[label])
            total = len(data)
            bad = len(data[data[label] == 1])
            good = total - bad
            stats = {'gini': node_gini,
                     'total': total,
                     'good': good,
                     'bad': bad,
                     'bad%': round(bad / total * 100, 2)}

            if self._stop_split(data, label, Vars, current_depth):
                return Tree(nid=node_id, node_type='Leaf', stats=stats)

            # 计算当前node的gini，以及最佳split使用的变量、切分值和gini，计算gini下降是否高于阀值
            best_split = self._find_best_split(data, label, Vars)
            gini_gain = (node_gini - best_split['gini']) * len(data) / self.m
            if gini_gain <= self._min_gini_gain:
                return Tree(nid=node_id, node_type='Leaf', stats=stats)

            best_split_var = Vars[best_split['col']]
            best_split_cutoff = best_split['cutoff']
            df1 = data[data[best_split_var] <= best_split_cutoff]
            df2 = data[data[best_split_var] > best_split_cutoff]

            return Tree(nid=node_id,
                        node_type='Node',
                        stats=stats,
                        split={'var': best_split_var, 'cutoff': best_split_cutoff},
                        child1=train(df1, label, Vars, node_id * 10 + 1, current_depth + 1),
                        child2=train(df2, label, Vars, node_id * 10 + 2, current_depth + 1)
                        )

        self.tree = train(data, label, Vars)
        del self.m
        del self.true_min_samples_leaf

        df = pd.DataFrame(self._summarize_leaves(self.tree, ls=[]))
        df['%total'] = round(df['total'] / df['total'].sum() * 100, 2)
        df['bad%'] = round(df['bad'] / df['total'] * 100, 2)
        df.sort_values(by='bad%', ascending=False, inplace=True)
        self.leaf_info = df

    def plot_text(self):
        '''
        plot the tree structure in txt format
        '''

        def plot_tree(tree, indent='\t\t'):
            if tree.type == 'Leaf':
                return 'nid: %s, sample: %s, bad%%: %.2f%%' \
                       % (tree.nid, tree.stats['total'], tree.stats['bad%'])
            else:
                decision = '%s <= %.4f?' % (tree.split['var'], tree.split['cutoff'])
                child1 = indent + 'yes -> ' + plot_tree(tree.child1, indent + '\t\t')
                child2 = indent + 'no  -> ' + plot_tree(tree.child2, indent + '\t\t')
                return (decision + '\n' + child1 + '\n' + child2)

        print(plot_tree(self.tree))

    def export_graphviz(self, tree=None):
        '''
        export the tree in dot format for visulization in graphviz
        '''

        def plot_tree(tree, ls_dot):
            if tree.type == 'Leaf':
                txt = '%d [label="gini: %.4f\nsamples: %d\nbad%%: %.2f%%", fillcolor="#A5A5A5"];' \
                      % (tree.nid, tree.stats['gini'], tree.stats['total'], tree.stats['bad%'])
                ls_dot.append(txt)
                return ls_dot
            else:
                # ls_dot.append('%s <= %s ;' %(tree.split['var'], tree.split['cutoff']))
                txt = '%d [label="%s <= %s\n\ngini: %.4f\nsamples: %d\nbad%%: %.2f%%", fillcolor="#4472C4"];' \
                      % (tree.nid, tree.split['var'], tree.split['cutoff'], tree.stats['gini'],
                         tree.stats['total'], tree.stats['bad%'])
                ls_dot.append(txt)
                ls_dot = plot_tree(tree.child1, ls_dot)
                ls_dot.append('%d -> %d ;' % (tree.nid, tree.child1.nid))
                ls_dot = plot_tree(tree.child2, ls_dot)
                ls_dot.append('%d -> %d ;' % (tree.nid, tree.child2.nid))
                return ls_dot

        ls_dot = [
            'digraph Tree {',
            'node [shape=box, style="filled", color="black", fontname=calibri];',
        ]
        if tree is None:
            ls_dot = plot_tree(self.tree, ls_dot)
        else:
            ls_dot = plot_tree(tree, ls_dot)
        ls_dot.append('}')
        dot_data = '\n'.join(ls_dot)

        return dot_data

    def predict(self, data):
        '''
        data: data frame as the input, containing all the X featues
        output: return the probability as pandas Series
        '''

        def predict_leaf_prob(data_row, tree=self.tree):
            if tree.type == 'Leaf':
                # return tree.stats['bad'] / tree.stats['total']
                return tree.stats['bad%'] / 100
            else:
                split_var = tree.split['var']
                split_cutoff = tree.split['cutoff']
                if data_row[split_var] <= split_cutoff:
                    return predict_leaf_prob(data_row, tree.child1)
                else:
                    return predict_leaf_prob(data_row, tree.child2)

        s = data.apply(predict_leaf_prob, axis=1)
        return s

    def score(self, data, base_score=600, base_gb_odds=30, pdo=40):
        """
        PDO 比率翻倍的分值
        base_score 基础分
        base_gb_odds 好坏比
        """
        factor = pdo / np.log(2)
        offset = base_score - factor * np.log(base_gb_odds)
        A = self.predict(data)
        A = A.clip(lower=0.00000001, upper=0.99999999)
        gb_odds = (1 - A) / A
        score = np.round(offset + factor * np.log(gb_odds), 0).astype(int)
        return score

    def ks_roc(self, data, label, data_test=None, roc_plot=True, ks_plot=False):
        '''
        data: dataframe, contain both X and Y
        label: variable name for Y
        '''

        def ksroc(data, label):
            df1 = data.copy()
            df1['score'] = self.score(df1)

            df2 = df1.groupby('score', sort=True)[label].agg(['count', 'sum'])
            df2 = df2.reset_index()
            df2.rename(columns={'sum': 'bad', 'count': 'total'}, inplace=True)
            df2['good'] = df2['total'] - df2['bad']
            bad = df2['bad'].sum()
            good = df2['good'].sum()
            df2['fpr'] = df2['good'].cumsum() / good
            df2['tpr'] = df2['bad'].cumsum() / bad

            df2['ks'] = df2['tpr'] - df2['fpr']
            df2['auc'] = (df2['tpr'].shift() + df2['tpr']) * df2['fpr'].diff() / 2
            df2.loc[0, 'auc'] = df2.loc[0, 'tpr'] * df2.loc[0, 'fpr'] / 2
            ks = df2['ks'].max() * 100
            auc = df2['auc'].sum()
            return df2, ks, auc

        if data_test is None:
            df_train, ks_train, auc_train = ksroc(data, label)
            print('The KS is %.2f, and AUC is %.3f' % (ks_train, auc_train))
        else:
            df_train, ks_train, auc_train = ksroc(data, label)
            df_test, ks_test, auc_test = ksroc(data_test, label)
            print('Train KS = %.2f, Test KS = %.2f' % (ks_train, ks_test))
            print('Train AUC = %.3f, Test AUC = %.3f' % (auc_train, auc_test))

        # this is sklearn's method to calculate the auc.
        #        import sklearn.metrics as mx
        #        fpr, tpr, threshold = mx.roc_curve(Y, A)
        #        rocauc = mx.auc(fpr, tpr)

        if roc_plot:
            plt.title('ROC curve')
            if data_test is None:
                plt.plot(df_train['fpr'], df_train['tpr'], 'b', label='AUC = %0.4f' % auc_train)
            else:
                plt.plot(df_train['fpr'], df_train['tpr'], 'b', label='Train AUC = %0.4f' % auc_train)
                plt.plot(df_test['fpr'], df_test['tpr'], 'r', label='Test AUC = %0.4f' % auc_test)

            plt.legend(loc='lower right')
            plt.plot([0, 1], [0, 1], 'g--')
            plt.xlim([0, 1])
            plt.ylim([0, 1])
            plt.ylabel('True Positive')
            plt.xlabel('False Positive')
            plt.show()

        if ks_plot:
            #            plt.title('KS curve (KS = %.2f)' %ks_train)
            plt.title('KS curve')
            if data_test is None:
                plt.plot(df_train['score'], df_train['tpr'], 'b', label='Traing set: TPR')
                plt.plot(df_train['score'], df_train['fpr'], 'r', label='Traing set: FPR')
            else:
                plt.plot(df_train['score'], df_train['tpr'], 'b', label='Traing set: TPR')
                plt.plot(df_train['score'], df_train['fpr'], 'r', label='Traing set: FPR')
                plt.plot(df_test['score'], df_test['tpr'], 'b--', label='Testing set: TPR')
                plt.plot(df_test['score'], df_test['fpr'], 'r--', label='Testing set: FPR')
            plt.legend(loc='lower right')
            plt.plot([0, 1], [0, 1], 'k--')
            plt.xlim([df_train['score'].min(), df_train['score'].max()])
            plt.ylim([0, 1])
            plt.xlabel('score')
            #            plt.text(df2['score'].min() + 20, 0.9, 'KS = %.2f' %ks)
            plt.show()

    def pop_by_score_band(self, data, label):

        df = data.copy()

        df['score'] = self.score(df)

        df2 = df.groupby('score', sort=True)[label].agg(['count', 'sum'])
        df2 = df2.reset_index()
        df2.rename(columns={'sum': 'bad', 'count': 'total'}, inplace=True)
        df2['good'] = df2['total'] - df2['bad']
        total = df2['total'].sum()
        df2['%total'] = df2['total'] / total
        df2['%cum_total'] = df2['%total'].cumsum()

        # score_low是在此分数以下的样本至少为1%， score_high是在此分数以上的样本至少为1%
        score_low = df2.loc[df2['%cum_total'] >= 0.01, 'score'].min()
        score_high = df2.loc[df2['%cum_total'] <= 1 - 0.01, 'score'].max()

        # 把两个score转为10的倍数：
        if score_low % 10 != 0:
            score_low = (score_low // 10 + 1) * 10
        score_high = (score_high // 10) * 10

        # 拿到分数的最小和最大值，并转为10的倍数
        score_min = df2['score'].min()
        score_max = df2['score'].max()
        score_min = ((score_min - 1) // 10) * 10
        if score_max % 10 != 0:
            score_max = (score_max // 10 + 1) * 10

        score_bin_list = list(range(score_low, score_high + 10, 10))
        score_bin_list = [-1000, score_min] + score_bin_list + [score_max, 2000]
        df['bin'] = pd.cut(df['score'], score_bin_list).astype(str)
        df2 = df.groupby('bin', sort=True)[label].agg(['count', 'sum'])
        df2 = df2.reset_index()
        df2.rename(columns={'sum': 'bad', 'count': 'total'}, inplace=True)

        df2['good'] = df2['total'] - df2['bad']  # 计算负样本数
        total = df2['total'].sum()
        good = df2['good'].sum()
        bad = df2['bad'].sum()
        df2['bad%'] = round(df2['bad'] / df2['total'] * 100, 2)  # 计算正样本比例
        df2['%total'] = round(df2['total'] / total * 100, 2)
        df2['%bad'] = df2['bad'].replace(0, 1) / bad  # 避免值为0无法取对数
        df2['%good'] = df2['good'].replace(0, 1) / good  # 避免值为0无法取对数
        df2['woe'] = np.log(df2['%good'] / df2['%bad'])
        df2['iv'] = (df2['%good'] - df2['%bad']) * df2['woe']
        iv = df2['iv'].sum()

        df2['%cum_bad'] = df2['%bad'].cumsum()
        df2['%cum_good'] = df2['%good'].cumsum()
        df2['KS'] = round((df2['%cum_bad'] - df2['%cum_good']) * 100, 2)
        ks = df2['KS'].max()
        print('\nIV = %.4f, and KS = %.4f\n' % (iv, ks))
        print(df2[['bin', '%total', 'total', 'bad', 'bad%', 'woe', 'KS']])


#        return df2[['%total', '#total', '#bad', 'bad%', 'woe', 'KS']]

# %%

clf = CART(max_depth=3, min_samples_split=100, min_samples_leaf=50,
           min_pct_leaf=0.01, min_gini_gain=0.0001, ccp_alpha=0.0001)

data = pd.read_csv("/Users/tian/Projects/my_learning/算法/data/my_data_guest.csv")
label = "bad"
data_train = data.iloc[:, 1:]
Vars = data.columns[2:]

clf.fit(data_train, label, Vars)

###画图
dot_data = clf.export_graphviz()
graph1 = graphviz.Source(dot_data, filename="tree", directory="/Users/tian/Projects/my_learning/算法/data")
graph1.view()
print(clf.score(data_train))
clf.ks_roc(data_train, label)
