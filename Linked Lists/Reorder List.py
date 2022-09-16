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
    def reorderList(self, head: [ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        print("slow", slow)  # slow should stop at the middle element if the list is odd, and before the middle if the list is even
        print("fast", fast)  # at this point is fast is pointing at nothing, that means the list has odd elements

        # get second half of list and reverse it
        secondHalf = slow.next  # the reverse process shouldn't include the head
        slow.next = None  # this actually splits the linked list in 2

        prev = None  # initialize the flipping
        while secondHalf:  # curr is the value at head
            temp = secondHalf.next
            secondHalf.next = prev  # point beginning at previous
            prev = secondHalf
            secondHalf = temp
        print(prev)  # at this point prev is the new head since its at the end of the linked list

        # merge 2 list
        first, second = head, prev
        print(first, second)
        while second:
            tempFirst, tempSecond = first.next, second.next
            first.next = second  # connect first with second
            second.next = tempFirst  # connect second with first

            first = tempFirst  # increment first by pointing it at the original first.next
            second = tempSecond  # increment second by pointing it at the original second.next

        # basically, have a temp for every link you break
    '''def reorderList(self, head: ListNode) -> None:
        # find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge two halfs
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2'''


if __name__ == "__main__":
    list1 = ListNode(1)
    list1.add(2)
    list1.add(3)
    list1.add(4)
    list1.add(5)


    print(list1)

    ass = Solution()
    ass.reorderList(list1)
    print(list1)




