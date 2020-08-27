"""
1315. Sum of Nodes with Even-Valued Grandparent

Given a binary tree, return the sum of values of nodes with even-valued grandparent.  (A grandparent of a node is the parent of its parent, if it exists.)

If there are no nodes with an even-valued grandparent, return 0.

"""

"""
Constraints:

The number of nodes in the tree is between 1 and 10^4.
The value of nodes is between 1 and 100.
"""

"""
Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 18 
Explanation: The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.
"""


"""

Input: [50,null,54,98,6,null,null,null,34]
Output: 156
Expected: 138
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        self.sumVal = 0
        self.search(root, False, False)
    
        return self.sumVal

    def helper(self, node, isPrtEven, isGprtEven):        
        """
        :type node: TreeNode
        :type isPrtEven: bool
        :type isGprtEven: bool
        :rtype: None
        """
            
        if node is not None:
            if isGprtEven is True:
                self.sumVal = self.sumVal + node.val

            isEven = (node.val%2==0)
            self.search(node.left, isEven, isPrtEven)
            self.search(node.right, isEven,isPrtEven)