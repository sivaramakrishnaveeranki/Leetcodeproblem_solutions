# 2. Add Two Numbers

# Example 1:

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]


 class Solution(object):
        def addTwoNumbers(self, l1, l2):

        dummy = ListNode(0)   # starting point
        curr = dummy
        carry = 0

        while l1 or l2 or carry:

            if l1:
                x = l1.val
            else:
                x = 0

            if l2:
                y = l2.val
            else:
                y = 0

            total = x + y + carry

            carry = total // 10        # carry
            digit = total % 10         # digit to store

            curr.next = ListNode(digit)
            curr = curr.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next
