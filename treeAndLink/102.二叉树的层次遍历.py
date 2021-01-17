#coding:utf-8
'''

给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。



示例：
二叉树：[3,9,20,null,null,15,7],

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

'''
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Tree:
    def levelTraversal(self, root):

        res, stack = [], [root]
        while stack:
            temp_stack, temp_val = [],[]
            for node in stack:
                if node:
                    temp_val.append(node.val)
                    temp_stack.append(node.left)
                    temp_stack.append(node.right)
            stack = temp_stack
            if temp_val: res.extend([temp_val])
        return res


