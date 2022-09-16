class Node:
    def __init__(self, key, val):  # using a doubly linked list
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

    def __str__(self):  # prints the linked list
        lis = ""
        while self:
            lis += f" ({self.key, self.val})"
            self = self.next
        return lis


'''class LRUCache:

    def __init__(self, capacity: int):
        """
        the head of linked list is most recently used
        """
        self.currCap = 0
        self.capacity = capacity
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        curr = self.head
        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next

        return -1


    def put(self, key: int, value: int) -> None:
        # check if key already exists in cache
        curr = self.head
        while curr:
            if curr.key == key:
                curr.val = value
                return
            curr = curr.next

        # add new key value pair
        if self.currCap == self.capacity:  # if cache is at capacity, remove last node
            if self.tail is self.head:  # theres only 1 element:
                self.head = None
                self.tail = None

            else:
                prevDummy = self.tail.prev
                prevDummy.next = None  # remove next pointer from 1 node before tail
                self.tail.prev = None  # remove prev pointer

        else:
            self.currCap += 1

        dingdong = Node(key, value)
        dingdong.next = self.head

        self.tail = curr  # update tail
        self.head = dingdong  # update head
        print(self.tail)'''


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # maps the key to a pointer to the node

        self.head = Node(0,0)  # head is the least recently used
        self.tail = Node(0,0)  # tail is the most recently used

        # point the head and tail towards eachother
        self.head.next = self.tail
        self.tail.prev = self.head

    ################## helper functions
    def remove(self, node):  # remove from list
        """
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
        """
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node):  # insert node at tail, aka most recently used
        """
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev
        """
        self.tail.prev.next = node
        node.next = self.tail
        # 1 2 3 tail
        self.tail.prev = node
        node.prev = self.tail.prev
    ################## helper functions


    def get(self, key: int) -> int:
        # if found
        if key in self.cache:
            # update most recent
            self.remove(self.cache[key])  # remove the requested node
            self.insert(self.cache[key])  # re add the requested node at tail, aka most recently used
            return self.cache[key].val

        # if not found
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])  # remove the requested node
        self.cache[key] = Node(key, value)  # adding new node to cache dictionary
        self.insert(self.cache[key])  # add the requested node at tail, aka most recently used

        if len(self.cache) > self.capacity:  # if the size of the dictionary is larger than capacity
            # remove Least recently used
            LRU = self.head.next  #  self.left.next is always the LRU

            self.remove(LRU)  # remove the node from linked list
            del self.cache[LRU.key]  # remove the key value pair from dict

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == '__main__':

    # Your LRUCache object will be instantiated and called as such:
    peepeepoopoo = LRUCache(2)
    peepeepoopoo.put(1, 1)          # cache is {1=1}
    print(peepeepoopoo.head)

    peepeepoopoo.put(2, 2)          # cache is {1=1, 2=2}
    print(peepeepoopoo.head)

    print(peepeepoopoo.get(1))      # return 1

    peepeepoopoo.put(3, 3)          # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    print(peepeepoopoo.head)

    print(peepeepoopoo.get(2))      # returns -1 (not found)

    peepeepoopoo.put(4, 4)          # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    print(peepeepoopoo.head)

    print(peepeepoopoo.get(1))      # return -1 (not found)
    print(peepeepoopoo.get(3))      # return 3
    print(peepeepoopoo.get(4))      # return 4