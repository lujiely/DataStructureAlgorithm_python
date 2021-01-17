#coding:utf-8
'''
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。



示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
'''
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class ListNodeOperator:
    def mergeTwoListNode(self, l1, l2):
        '''方法一：迭代法'''
        new_list = ListNode(0)
        cur = new_list
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                cur = cur.next
                l1 = l1.next
            else:
                cur.next = l2
                cur = cur.next
                l2 = l2.next
        if l1: cur.next = l1
        if l2: cur.next = l2
        return new_list.next

    def mergeTwoListNode(self, l1, l2):
        '''方法二: 递归'''
        if not l1: return l2
        if not l2: return l1
        if l1 and l2:
            if l1.val > l2.val:
                l1.val, l2.val = l2.val, l1.val
            l1.next = self.mergeTwoListNode(l1.next, l2)
        return l1 or l2
