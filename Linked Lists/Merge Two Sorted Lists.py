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
    def mergeTwoLists(self, list1: [ListNode], list2: [ListNode]) -> [ListNode]:
        newList = ListNode(2)  # add some random bullshit here, we return head.next anyway so it isnt used
        head = newList  # save the head

        print(newList, "SSSSSSSSSSS")
        while list1 and list2:  # while at least 1 list isn't pointing to none

            if list1.val <= list2.val:
                newList.next = list1
                list1 = list1.next
            else:
                newList.next = list2
                list2 = list2.next

            newList = newList.next # update pointer

        newList.next = list1 if list1 else list2 # add the end since the while loop doesn't reach the last element
        return head.next

    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next

if __name__ == "__main__":
    list1 = ListNode(1)
    list1.add(2)
    list1.add(4)

    list2 = ListNode(1)
    list2.add(3)
    list2.add(4)

    print(list1, list2)

    ass = Solution()
    print(ass.mergeTwoLists(list1,list2))




