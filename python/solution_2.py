'''
2. Add Two Numbers
https://leetcode.com/problems/add-two-numbers/
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy, carry, n1, n2 = ListNode(0), 0, l1, l2
        node = dummy
        while n1 or n2 or carry:
            n1_val = 0 if not n1 else n1.val
            n2_val = 0 if not n2 else n2.val
            s = n1_val + n2_val + carry
            carry, s = divmod(s, 10)
            node.next = ListNode(s)
            node = node.next
            if n1: n1 = n1.next
            if n2: n2 = n2.next
        return dummy.next