#coding:utf-8
'''
您需要在二叉树的每一行中找到最大的值。

示例：

输入:

          1
         / \
        3   2
       / \   \
      5   3   9

输出: [1, 3, 9]

'''
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Tree:
    def maxValueOflevelTree(self, root):
        stack, res = [root],[]
        while stack:
            cur_max, cur_list = float('-inf'), []
            for node in stack:
                if node:
                    cur_max = max(cur_max, node.val)
                    cur_list.append(node.left)
                    cur_list.append(node.right)
            stack = cur_list
            if cur_max != float('-inf'): res.append(cur_max)
        return res