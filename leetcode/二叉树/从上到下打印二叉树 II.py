#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： tian
# datetime： 2022/11/21 2:58 PM 
# ide： PyCharm
"""
从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]
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
        tree_list = []

        def insert_tree_tree(level, sub_root, tree_lis):
            if level >= len(tree_lis):
                tree_list.append([])
            tree_list[level].append(sub_root.val)
            if sub_root.left is not None:
                insert_tree_tree(level + 1, sub_root.left, tree_lis)
            if sub_root.right is not None:
                insert_tree_tree(level + 1, sub_root.right, tree_lis)

        insert_tree_tree(0, root, tree_list)

    # DFS
    def levelOrder2(self, root: TreeNode):
        if root is None:
            return []
        tree_list = []
        level = 0
        queue = collections.deque()
        queue.append(root)
        tmp = []  # tmp实用来存放下一层的数据
        while queue:
            if level >= len(tree_list):
                tree_list.append([])
            node = queue.popleft()
            tree_list[level].append(node.val)

            if node.left is not None:
                tmp.append(node.left)
            if node.right is not None:
                tmp.append(node.right)

            if queue.__len__() <= 0:  # 来判断是否可以进入下一层的level
                level += 1
                for t in tmp:
                    queue.append(t)
                tmp = []

        return tree_list


if __name__ == '__main__':
    s = Solution()
    # tree = TreeNode(3, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)))
    tree = TreeNode(1, left=TreeNode(2, left=TreeNode(4), right=TreeNode(5)), right=TreeNode(3))
    print(s.levelOrder2(tree))
