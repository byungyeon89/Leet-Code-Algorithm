

"""
1305. all-elements-in-two-binary-search-trees

Given two binary search trees root1 and root2.
Return a list containing all the integers from both trees sorted in ascending order.
"""

"""
Constraints:
	• n == graph.length
	• 2 <= n <= 15
	• 0 <= graph[i][j] < n
	• graph[i][j] != i (i.e., there will be no self-loops).
The input graph is guaranteed to be a DAG.
"""

"""
Example 1:
Input: root1 = [2,1,4], root2 = [1,0,3]
Output: [0,1,1,2,3,4]
Example 2:
Input: root1 = [0,-10,10], root2 = [5,1,7,0,2]
Output: [-10,0,0,1,2,5,7,10]
Example 3:
Input: root1 = [], root2 = [5,1,7,0,2]
Output: [0,1,2,5,7]
Example 4:
Input: root1 = [0,-10,10], root2 = []
Output: [-10,0,10]
Example 5:
Input: root1 = [1,null,8], root2 = [8,1]
Output: [1,1,8,8]
 

"""
import sys
import logging

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
                           
        ans = []
        
        def helper(tree):		#dfs
        	if tree:
        		ans.append(tree.val)
        		helper(tree.left)
        		helper(tree.right)
        		
        helper(root1)
        helper(root2)
        
        return sorted(ans)
        			
                  
def main():

    s = Solution()

    test_cases = [
        [[2,1,4], [1,0,3]],					# 1
        [[0,-10,10], [5,1,7,0,2]],	# 2
        [[], [5,1,7,0,2]],					# 3
        [[0,-10,10], []],						# 4
				[[1,None,8], [8,1]],				# 5
        ]	

    for i, test in enumerate(test_cases):
        print("[%d]"% (i + 1))
        print("Input: root1 =", test[0], ", root2 =", test[1])
        print("Output:", s.getAllElements(test[0],test[1]))
        print('\n')

if __name__ == "__main__":
    loggerTest = logging.getLogger("test")
    loggerTest.setLevel(logging.INFO) # DEBUG < INFO < WARNING < ERROR < CRITICAL  
    #formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    streamHander = logging.StreamHandler()
    #streamHander.setFormatter(formatter)
    loggerTest.addHandler(streamHander)

    main()    
  