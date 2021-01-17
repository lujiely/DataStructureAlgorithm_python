#coding:utf-8
'''
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。



示例：

给你这个链表：1->2->3->4->5

当 k = 2 时，应当返回: 2->1->4->3->5

当 k = 3 时，应当返回: 3->2->1->4->5



说明：

你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
'''
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class ListNodeOperator:
    def reverseKGroupListNode(self, head, k):
        hair = ListNode(0)
        hair.next, step = head, 0
        prev = hair

        while head:
            tail = prev
            for _ in range(k):
                tail = tail.next
                if not tail:
                    return hair.next

            nex = tail.next

            head, tail = self.swap(head,tail)
            prev.next = head
            tail.next = nex

            prev = tail
            head = tail.next
        return hair.next

    def swap(self, head, tail):
        cur, pre = head, tail.next
        while pre != tail:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return tail, head

    
