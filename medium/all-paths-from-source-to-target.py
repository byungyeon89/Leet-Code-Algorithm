

"""
797. all-paths-from-source-to-target

Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1, and return them in any order.
The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).
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

Input: graph = [[1,2],[3],[3],[]]Output: [[0,1,3],[0,2,3]]Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

Example 2:Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
Example 3:
Input: graph = [[1],[]]Output: [[0,1]]
Example 4:
Input: graph = [[1,2,3],[2],[3],[]]Output: [[0,1,2,3],[0,2,3],[0,3]]
Example 5:
Input: graph = [[1,3],[2],[3],[]]Output: [[0,1,2,3],[0,3]]


"""
import sys
import logging

class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        
        path_list = []
        
        if len(graph[0]) == 0:
        	return path_list # []
                        	
        dest_idx = len(graph) - 1
                
        def helper(_val, path):        	
        	if _val == dest_idx:
        		path_list.append(path)
        		
        	for x in graph[_val]:
        			helper(x, path + [x])        			        	
                
        helper(0, [0])
        		        
        return path_list        
def main():

    s = Solution()

    test_cases = [
        [[1,2],[3],[3],[]],						# 1
        [[4,3,1],[3,2,4],[3],[4],[]],	# 2
        [[1],[]],											# 3
        [[1,2,3],[2],[3],[]],					# 4
				[[1,3],[2],[3],[]],						# 5
        ]	

    for i, test in enumerate(test_cases):
        print("[%d]"% (i + 1))
        print("Input:", test)
        print("Output:", s.allPathsSourceTarget(test))
        print('\n')

if __name__ == "__main__":
    loggerTest = logging.getLogger("test")
    loggerTest.setLevel(logging.INFO) # DEBUG < INFO < WARNING < ERROR < CRITICAL  
    #formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    streamHander = logging.StreamHandler()
    #streamHander.setFormatter(formatter)
    loggerTest.addHandler(streamHander)

    main()    
  