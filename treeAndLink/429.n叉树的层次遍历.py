#coding:utf-8
'''
给定一个 N 叉树，返回其节点值的层序遍历。 (即从左到右，逐层遍历)。

例如，给定一个 3叉树 :







返回其层序遍历:

[
     [1],
     [3,2,4],
     [5,6]
]


说明:

树的深度不会超过 1000。
树的节点总数不会超过 5000。
'''

class TreeNode:
    def __init__(self, val, children=None):
        self.val = val
        self.children = children

class Tree:
    def levelTraversalNT(self, root):
        stack, res = [root], []
        while stack:
            cur_val, cur_list = [], []
            for node in stack:
                if node:
                    cur_val.append(node.val)
                    for node in node.children:
                        cur_list.append(node)
            stack = cur_list
            if cur_val: res.extend([cur_val])
        return res
