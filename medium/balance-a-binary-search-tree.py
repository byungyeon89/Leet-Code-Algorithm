"""
1382. Balance a Binary Search Tree
Medium
37821Add to ListShare
Given a binary search tree, return a balanced binary search tree with the same node values.
A binary search tree is balanced if and only if the depth of the two subtrees of every node never differ by more than 1.
If there is more than one answer, return any of them.
 
Example 1:
Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2,null,null] is also correct.
 
Example 2:
Input: [14,9,16,2,13]
Output: [2,9,16,14,null,13]
Expected:[13,2,14,null,9,null,16]

Constraints:
	• The number of nodes in the tree is between 1 and 10^4.
The tree nodes will have distinct values between 1 and 10^5.

"""
import sys
import logging

import tree
                
class Solution(object):
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        def getAllValues(root):
        	"""
        	:type root: TreeNode
        	:rtype: List[int]
        	"""	        	
        	res = []        	
        	def helper(node):
        		"""
        		:type node: TreeNode
        		"""
        		if node:        		
        			res.append(node.val)
        			helper(node.left)
        			helper(node.right)
        	
        	helper(root)        		        	
        	
        	return res
        	
        def makeBalncedBT(nodes):
        	"""
        	:type nodes: List[int]
        	:rtype: TreeNode
        	"""      	
        	def helper(nt):
        		"""
        		:type nodes: List[int]
        		:type rtype: TreeNode
        		"""        	
        		if len(nt) <= 0:
        			return None
        			
        		if len(nt) == 1:
        			return TreeNode(nt[0])
        			        			
        		idx = int(len(nt)/2)	        		
        		        		
        		node = TreeNode(nt[idx])    		        			
        		node.left = helper(nt[:idx])
        		node.right = helper(nt[idx+1:])
        			
        		return node
       	
       		return helper(nodes)
       		       		
       	return makeBalncedBT(getAllValues(root))
                    
def main():

    s = Solution()

    test_cases = [
    		tree.createTree([1,None,2,None,3,None,4,None,None], 0, 8),    		    		
    		tree.createTree([14, 9, 16, 2, 13], 0, 4),
        ]
                

    for i, test in enumerate(test_cases):
    	print("[%d]" % (i + 1))
    	print("Input: ", test.printTree("pre"))
    	print("Output:", s.balanceBST(test))
    	print('\n')

if __name__ == "__main__":
    loggerTest = logging.getLogger("test")
    loggerTest.setLevel(logging.INFO) # DEBUG < INFO < WARNING < ERROR < CRITICAL  
    #formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    streamHander = logging.StreamHandler()
    #streamHander.setFormatter(formatter)
    loggerTest.addHandler(streamHander)

    main()    
  