# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):  # prints the linked list
        lis = ""
        while self:
            lis += f" {self.val}"
            self = self.next
        return lis

    def add(self, x):
        while self.next: # while next isnt pointing to nothing
            self = self.next

        self.next = ListNode(x)

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        basically, have left and right pointers
        1. put left is on a dummy node, which is added before the first element (for edge cases)
        2. increment right so that the distance between left and right is n
        3. increment left and right at the same rate until right hits None
        4. at this point you know that left will land on n because the dist between r and l was n, and now just
            delete the node

        """
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # step 2
        while n > 0:
            right = right.next
            n -= 1
        # step 3
        while right:
            left = left.next
            right = right.next

        # delete
        left.next = left.next.next
        return dummy.next



if __name__ == "__main__":
    list1 = ListNode(1)
    list1.add(2)
    list1.add(3)
    list1.add(4)
    list1.add(5)


    ass = Solution()
    print("ANS:",ass.removeNthFromEnd(list1, 1))




