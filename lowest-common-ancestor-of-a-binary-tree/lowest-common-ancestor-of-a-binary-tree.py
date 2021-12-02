# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if (root == None or root == p or root == q):
            return root
        # find the value of left node 
        left = self.lowestCommonAncestor(root.left,p,q)
        # find for right node
        right = self.lowestCommonAncestor(root.right,p,q)
        if (left != None and right != None):
            return root
        elif (left != None):
            return left
        else:
            return right

        
        
        