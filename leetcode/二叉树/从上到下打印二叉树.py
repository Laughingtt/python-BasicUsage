#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： tian
# datetime： 2022/11/22 10:19 AM 
# ide： PyCharm
"""
例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回：

[3,9,20,15,7]


算法流程：
特例处理： 当树的根节点为空，则直接返回空列表 [] ；
初始化： 打印结果列表 res = [] ，包含根节点的队列 queue = [root] ；
BFS 循环： 当队列 queue 为空时跳出；
出队： 队首元素出队，记为 node；
打印： 将 node.val 添加至列表 tmp 尾部；
添加子节点： 若 node 的左（右）子节点不为空，则将左（右）子节点加入队列 queue ；
返回值： 返回打印结果列表 res 即可。

作者：Krahets
链接：https://leetcode.cn/problems/cong-shang-dao-xia-da-yin-er-cha-shu-lcof/solutions/134956/mian-shi-ti-32-i-cong-shang-dao-xia-da-yin-er-ch-4/
来源：力扣（LeetCode）
"""
import collections

class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    # 递归
    def levelOrder(self, root: TreeNode):
        if root is None:
            return []
        tree_list = []

        def insert_tree_tree(level, sub_root, tree_lis):
            if level >= len(tree_lis):
                tree_lis.append([])
            tree_lis[level].append(sub_root.val)
            if sub_root.left is not None:
                insert_tree_tree(level + 1, sub_root.left, tree_lis)
            if sub_root.right is not None:
                insert_tree_tree(level + 1, sub_root.right, tree_lis)

        insert_tree_tree(0, root, tree_list)
        res = []
        for tree in tree_list:
            res += tree

        return res

    # DFS 深度优先搜索算法
    def levelOrder2(self, root: TreeNode):
        if root is None:
            return
        queue = collections.deque()
        queue.append(root)
        res_list = []
        while queue:
            node = queue.popleft()
            res_list.append(node.val)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

        return res_list


if __name__ == '__main__':
    s = Solution()
    tree = TreeNode(3, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)))
    print(s.levelOrder2(tree))
