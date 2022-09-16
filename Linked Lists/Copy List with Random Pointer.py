# Definition for singly-linked list.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

    def __str__(self):  # prints the linked list
        lis = ""
        while self:
            lis += f"val:{self.val}random:{self.random.val if self.random != None else None} "
            self = self.next
        return lis

    def add(self, x):
        while self.next: # while next isnt pointing to nothing
            self = self.next

        self.next = Node(x)

class Solution:
    '''def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':  # wrong answer
        currOri, nextOri = head, head.next

        currNew = Node(0)
        ans = currNew

        while nextOri != None:
            currNew.val = currOri.val
            currNew.next = Node(99)

            if currOri.random == None:
                currNew.random = None
            else:
                # if oriRandom isn't already in new random list, then make copy of oriRandom and set the pointer, else just set the pointer
                check = ans

                while currOri.random.val != check.val:  # and currOri.random.next != check.next and currOri.random.random != check.random:
                    if check.next != None:  # no copy found and hasn't reached end of list, so we increment
                        check = check.next

                    else:  # no copy found and have reached end of list, we conclude theres no copy
                        print("notFound")
                        currNew.random = Node(currOri.random.val, currOri.random.next,
                                              currOri.random.random)  ############ here is the issue: currNew.random points to a completely new node that gets made, but this new node's random pointer and next pointer points back to the original linked list, and thats not allowed
                        break

                else:  # copy is found
                    print(f'FOUND {currOri.random.val} {check.val}')
                    currNew.random = check

            currNew = currNew.next  # increment

            currOri = currOri.next  # increment
            nextOri = nextOri.next  # increment

        else:  # deals with the last item's val
            currNew.val = currOri.val
            currNew.next = None
            currNew.random = Node(currOri.random.val, currOri.random.next, currOri.random.random)

        return ans'''

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':  # my own dict soln
        """
        basically,
        1. you make oldtonew dictionary mapping old nodes to newly made nodes
        2. then you iterate through old linked list and plug those old nodes into dict to get new nodes and
        connect them with a new head
        3. return head

        """
        # init first pass var
        OldToNew = {None: None}  # add the last element for both linked lists
        count = 0

        # run first pass to create nodes with only val
        currOld = head
        while currOld:
            OldToNew[currOld] = Node(currOld.val)
            count += 1
            currOld = currOld.next


        # init second pass var
        currOld = head

        newHead = OldToNew[head]
        curr = newHead

        # second pass to add next and random pointers
        for i in range(count):
            curr.next = OldToNew[currOld.next]
            curr.random = OldToNew[currOld.random]

            # increment
            curr = curr.next
            currOld = currOld.next

        return newHead

    def copyRandomList(self, head: "Node") -> "Node":  # neetcode sln

        """
        basically, he uses the same idea, but less variables to do it
        """
        oldToCopy = {None: None}

        cur = head
        while cur:  # first pass
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next
        cur = head
        while cur: # second pass
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next
        return oldToCopy[head]


if __name__ == "__main__":
    list1 = Node(0, None)  # pointing 0 to 3

    list1.next = Node(1, list1)  # pointing 1 to 2

    list1.next.next = Node(2, None)  # pointing 2 to 3

    #  [[1,null],[2,0],[3,null]] -> none

    print(list1)

    ass = Solution()
    print("ANS:",ass.copyRandomList(list1))




