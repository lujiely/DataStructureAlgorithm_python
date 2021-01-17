#coding:utf-8
'''
给定一个 N 叉树，返回其节点值的前序遍历。

例如，给定一个 3叉树 :







返回其前序遍历: [1,3,5,6,2,4]。



说明: 递归法很简单，你可以使用迭代法完成此题吗?
'''

class TreeNode:
    def __init__(self, val, children=None):
        self.val = val
        self.children = children


class Tree:
    def preOrderTraversalNT(self, root):
        """方法一: 递归"""
        res, visited = [], set()
        def helper(root):
            if root in visited: return root
            if root:
                visited.append(root)
                res.append(root.val)
                for node in root.children:
                    if node not in visited:
                        helper(node)
        helper(root)
        return res

    def preOrderTraversalNT(self, root):
        '''方法二: 迭代'''
        if not root: return
        res, stack = [], [root]
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            stack.extend(cur.children[::-1])
        return res

