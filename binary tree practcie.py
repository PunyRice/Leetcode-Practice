if __name__ == "__main__":
    print(5)

'''Algorithm Postorder(tree)
   1. Traverse the left subtree, i.e., call Postorder(left-subtree)
   2. Traverse the right subtree, i.e., call Postorder(right-subtree)
   3. Visit the root.

Algorithm Preorder(tree)
   1. Visit the root.
   2. Traverse the left subtree, i.e., call Preorder(left-subtree)
   3. Traverse the right subtree, i.e., call Preorder(right-subtree) 

Algorithm Inorder(tree)
   1. Traverse the left subtree, i.e., call Inorder(left-subtree)
   2. Visit the root.
   3. Traverse the right subtree, i.e., call Inorder(right-subtree)'''

# binary tree
class BSTNode:
    def __init__(self, data=None):  # root is empty by default
        self.left = None
        self.right = None
        self.data = data

    def insert(self, value):
        if not self.data:  # if there is nothing at current node
            self.data = value
            return

        if self.data == value:  # if the current node is equal to value
            print("duplicate detected, do nothing")
            return

        # data goes on the left if: - data is smaller than curr node AND curr node's left spot is empty
        if value < self.data:
            if self.left: # if curr node's left spot is not empty
                self.left.insert(value)
                return
            else: # Condtion satisfied, define a BSTNode and add it to left
                self.left = BSTNode(value)

        # data goes on the right if: - data is larger than curr node AND curr node's right spot is empty
        else:
            if self.right:
                self.right.insert(value)
                return
            else: # Condtion satisfied, define a BSTNode and add it to right
                self.right = BSTNode(value)

    def printTree(self):
        if not self.data:
            return

        if self.left:
            print(self.left)

        if self.right:
            print(self.right)


        self.print(root.left)
        self.print(root.right)

if __name__ == "__main__":
    BST = BSTNode()
    test = [1,2,3,4,5,6]

    for i in test:
        BST.insert(i)

    BST.printTree(1)
