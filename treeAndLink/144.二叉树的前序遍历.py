#coding:utf-8
'''
给你二叉树的根节点 root ，返回它节点值的 前序 遍历。



示例 1：


输入：root = [1,null,2,3]
输出：[1,2,3]
示例 2：

输入：root = []
输出：[]
示例 3：

输入：root = [1]
输出：[1]
示例 4：


输入：root = [1,2]
输出：[1,2]
示例 5：


输入：root = [1,null,2]
输出：[1,2]


提示：

树中节点数目在范围 [0, 100] 内
-100 <= Node.val <= 100


进阶：递归算法很简单，你可以通过迭代算法完成吗？


'''

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Tree:
    def preOrderTraversal(self, root):
        #递归方法
        res = []
        def helper(root):
            if root:
                res.append(root.val)
                helper(root.left)
                helper(root.right)
        helper(root)
        return res


    def preOrderTraversal(self, root):
        #迭代方法
        res, stack, cur = [],[], root
        while stack or cur:
            while cur:
                res.append(cur.val)
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            cur = cur.right

        return res


