#coding:utf-8
'''

给定一个二叉树，返回它的中序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？


'''
class TreeNode(object):
    def __init__(self,value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

class Tree(object):
    def inOrder(self, root):
        '''方法一：深度遍历'''
        alist = []
        def dfs(root):
            if root:
                dfs(root.left)
                alist.append(root.val)
                dfs(root.right)

        dfs(root)
        return alist


    def inOrderTraversal(self, root):
        '''迭代'''
        cur, stack, res = root, [], []
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res




if __name__ == '__main__':
    alist = [1,'null',2,3]
    '''
         1
    null    2
  3
    '''
    tree = TreeNode(1)
    tree.left = TreeNode('null')
    tree.right = TreeNode(2)
    tree.left.left = TreeNode(3)
    cur = tree
    stack = [cur]

    while cur and stack:
        temp = []
        for cur in stack:
            if cur and cur.val: print(cur.val)
            if cur.left: temp.append(cur.left)
            if cur.right: temp.append(cur.right)
        stack = temp

    solu = Tree()
    root = tree
    res = solu.inOrder(root)
    print(res)

    res = solu.inOrderTraversal(root)
    print(res)



