"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        nodeP = p
        nodeQ = q
        pAn = {}
        while (p != None):
            pAn[p] = p.val
            p = p.parent
        while (q != None):
            if q in pAn:
                return q
            q = q.parent
        return null
        