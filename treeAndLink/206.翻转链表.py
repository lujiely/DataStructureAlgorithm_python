#coding:utf-8
'''
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
'''
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class ListOperator:
    def reverseList(self, head):
        cur, pre = head, None
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre


    #有头有尾的链表翻转
    def reverseList02(self, head, tail):
        cur, pre = head, tail.next
        while pre != tail:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return tail, head