#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： tian
# datetime： 2022/11/21 2:58 PM 
# ide： PyCharm
"""
请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。

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
  [20,9],
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
    # DFS
    def levelOrder(self, root: TreeNode):
        if root is None:
            return []
        tree_list = []
        queue = collections.deque()
        queue.append(root)
        level = 0
        tmp = []
        while queue:
            if level >= len(tree_list):
                tree_list.append([])
            node = queue.popleft()
            tree_list[level].append(node.val)
            if node.left is not None:
                tmp.append(node.left)
            if node.right is not None:
                tmp.append(node.right)
            if len(queue) <= 0:
                for i in tmp:
                    queue.append(i)
                tmp = []
                if level % 2 == 1:
                    tree_list[level].reverse()
                level += 1
        return tree_list


if __name__ == '__main__':
    s = Solution()
    tree = TreeNode(3, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)))
    print(s.levelOrder(tree))
