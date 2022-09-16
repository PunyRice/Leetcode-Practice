# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: [TreeNode]) -> [TreeNode]:  # my recursive sln, this is depth first search
        """
        Basically, we recursively do a DFS:
        DFS is when you search as deep as possible down one path of the tree, and once you hit a deadend you back up
            to where you begun and go down another path, this can be done recursively

        we set base case, if the root we've been passed is None, that means we
        """
        if not root:  # base case
            return
        
        '''if root.left == None and root.right == None:  # base case
            return root'''  # this line isnt needed because the prev if already catches when we reach leaves
        
        # swap left and right
        temp = root.left
        root.left = root.right
        root.right = temp

        # call recursively on each side
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root

