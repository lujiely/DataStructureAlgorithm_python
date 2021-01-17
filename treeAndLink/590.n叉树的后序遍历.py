#coding:utf-8
'''
给定一个 N 叉树，返回其节点值的后序遍历。

例如，给定一个 3叉树 :







返回其后序遍历: [5,6,3,2,4,1].



说明: 递归法很简单，你可以使用迭代法完成此题吗?
'''

class TreeNode:
    def __init__(self, val, children=None):
        self.val = val
        self.children = children

class Tree:
    def postOrderTraversalNT(self, root):
        '''方法一： 递归'''
        res, visited = [], set()
        def helper(root):
            if root in visited: return root
            if root:
                visited.add(root)
                for node in root.children:
                    if node not in visited:
                        helper(node)
                res.append(root.val)
        helper(root)
        return res

    def postOrderTraversalNT02(self, root):
        '''方法二： 迭代'''
        if not root: return
        stack, res = [root], []
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            stack.extend(root.children)
        return res[::-1]



