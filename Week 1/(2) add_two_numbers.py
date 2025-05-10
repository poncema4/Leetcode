# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not l1 and not l2:
            return None
        elif not l1:
            return l2
        elif not l2:
            return l1

        m = l1.val + l2.val
        p = ListNode(m % 10)
        p.next = self.addTwoNumbers(l1.next, l2.next)
        if m >= 10:
            p.next = self.addTwoNumbers(p.next, ListNode(1))
        return p