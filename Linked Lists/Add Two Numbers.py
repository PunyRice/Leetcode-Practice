# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: [ListNode], l2:[ListNode]) -> [ListNode]:  # my own
        '''basically, detects carryovers, has a carry over variable that is always added to the sum, and at last if
        there are still carryover when we reach end of list, we add a leading 1
        '''

        newHead = ListNode(0)
        ans = newHead
        carryOver = 0
        # we will add l2 and l1 into new linked list

        while l1 or l2:
            if l1 and l2:
                l1.val += carryOver

                if l1.val + l2.val >= 10:  # if there is carryover for the next
                    newHead.val = l1.val + l2.val - 10
                    carryOver = 1
                else:
                    newHead.val = l1.val + l2.val
                    carryOver = 0

            elif l1:
                l1.val += carryOver

                if l1.val >= 10:

                    newHead.val += l1.val - 10
                    carryOver = 1
                else:
                    newHead.val = l1.val
                    carryOver = 0

            elif l2:
                l2.val += carryOver

                if l2.val >= 10:
                    newHead.val += l2.val - 10
                    carryOver = 1
                else:
                    newHead.val = l2.val
                    carryOver = 0

            # increment
            if l1: l1 = l1.next
            if l2: l2 = l2.next

            if l1 or l2:
                newHead.next = ListNode(0)
                newHead = newHead.next

        if carryOver == 1:
            newHead.next = ListNode(1)

        return ans

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:  # need code sln
        """
        basically he does the same thing except he simplifies things using floor divison and modulus to get rid of the
        if statements, making this alot faster than mine
        """
        dummy = ListNode()
        cur = dummy

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit
            val = v1 + v2 + carry
            carry = val // 10  # 1 if val is => 10, 0 if anything else
            val = val % 10
            cur.next = ListNode(val)  # add new node

            # update ptrs
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next

