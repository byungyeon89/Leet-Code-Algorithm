
"""
1008. Construct Binary Search Tree from Preorder Traversal

Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

It's guaranteed that for the given test cases there is always possible to find a binary search tree with the given requirements.

"""

"""
Constraints:

1 <= preorder.length <= 100
1 <= preorder[i] <= 10^8
The values of preorder are distinct.
"""

"""
Example 1:

Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

"""
import sys
import logging
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):    
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        def helper(A):
            """
            :type A: List[int]
            :rtpye: TreeNode
            """            
            if not A:
                return None
                                    
            node = TreeNode(A[0])
                        
            i = 1
            while i<len(A) and  A[i] < node.val:
                i+=1
                
            node.left = helper(A[1:i])
            node.right = helper(A[i:])

            return node

        return helper(preorder)

def main():

    s = Solution()

    test_cases = [[8,5,1,7,10,12]]

    for i, test in enumerate(test_cases):
        print("[%d]"% (i + 1))
        print("Input:", test)
        print("Output:", s.bstFromPreorder(test))
        print('\n')

if __name__ == "__main__":
    loggerTest = logging.getLogger("test")
    loggerTest.setLevel(logging.INFO) # DEBUG < INFO < WARNING < ERROR < CRITICAL  
    #formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    streamHander = logging.StreamHandler()
    #streamHander.setFormatter(formatter)
    loggerTest.addHandler(streamHander)

    main()    
  