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


if __name__ == '__main__':
    s = Solution()
    tree = TreeNode(3, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)))
    s.levelOrder(tree)
