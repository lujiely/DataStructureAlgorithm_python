#coding:utf-8
'''
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。



示例 1：


输入：head = [1,2,3,4]
输出：[2,1,4,3]
示例 2：

输入：head = []
输出：[]
示例 3：

输入：head = [1]
输出：[1]


提示：

链表中节点的数目在范围 [0, 100] 内
0 <= Node.val <= 100
'''

class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class ListOperator(object):
    def swapPairs(self, head):
        if head and head.next:
            head.next.next, head.next, head = head, self.swapPairs(head.next.next), head.next
        return head


if __name__ == '__main__':
    head = [1,2,3,4]
    newlist = ListNode(0)
    pre = newlist
    for num in head:
        pre.next = ListNode(num)
        pre = pre.next

    alist = []
    cur = newlist.next
    while cur:
        alist.append(cur.value)
        cur = cur.next
    print(alist)

    solu = ListOperator()
    ans = solu.swapPairs(newlist.next)
    print(ans)
    ans_lis = []
    while ans:
        ans_lis.append(ans.value)
        ans = ans.next
    print(ans_lis)

