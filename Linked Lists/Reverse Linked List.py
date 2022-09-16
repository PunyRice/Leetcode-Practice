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
        print("added", x)

#class Solution:
    def reverseList(self, head):
        prev, curr = None, head
        # curr is the value at head, prev is the value at the end
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev  # at this point prev is the new head since its at the end of the linked list

    '''def reverseListRecur(self, head):
        if not head:  # if the linked list at this point is 1 long
            return None
        newHead = head
        if head.next: # if theres still a sub problem
            newHead = self.reverseListRecur(head.next)
            head.next.next = head  # reverse link
        head.next = None
        return newHead'''
    def reverseList(self, head):
        curr, prev = head, None
        while curr:  # 1 -> 2 -> 3 ->
            #
            temp = curr.next  # save the next pointer
            curr.next = prev  # point curr at nothing since the first curr is the end of the new linkedlist
            prev = curr  # update the prev pointer
            curr = temp  # update the curr pointer

        return prev

if __name__ == "__main__":
    linklist = ListNode(1)
    linklist.add(2)
    linklist.add(3)
    print(linklist)
    print(linklist.reverseList(linklist))




