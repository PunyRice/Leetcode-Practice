# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: [ListNode]) -> bool:  # my sln
        """
        this one is super self explanatory, you just put into set and check if there
        are duplicates
        """
        hashMap = set()
        while head:
            if head in hashMap:
                return True
            hashMap.add(head)
            head = head.next

    def hasCycle(self, head: [ListNode]) -> bool:  # tortoise and hare algoritm soln
        """
        have a slow and faster pointer, slow increments by 1 and fast increments by 2

        if there's a loop, the fast pointer will always loop around and catch back up
        with the slow pointer, no matter the edge cases

        usually for this algoritm you use a do while loop but python dont have lol
        """
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                return True

        return False