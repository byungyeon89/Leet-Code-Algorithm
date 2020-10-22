"""
1079. Letter Tile Possibilities
Medium
80231Add to ListShare
You have n  tiles, where each tile has one letter tiles[i] printed on it.
Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.
 
Example 1:
Input: tiles = "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
Example 2:
Input: tiles = "AAABBC"
Output: 188
Example 3:
Input: tiles = "V"
Output: 1
 
Constraints:
	• 1 <= tiles.length <= 7
	• tiles consists of uppercase English letters.

"""
import sys
import logging

class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        
        res = []                
        N = len(tiles)
        v = [False for i in range(N)]
        
        def dfs(node, visited, path=""):
        	"""
        	:type node: str
        	:type visited: List[int] 
        	:type path: str       	        	
        	"""        	        	
        	
        	if path:
        		res.append(path)
        		
        	if len(path) == N:
        		return
        		
        	for i in range(N):      
        		if visited[i]:
        			continue
        			  		        		
        		visited[i] = True        		
        		dfs(node, visited, path+node[i])
        		visited[i] = False
        	        
        dfs(tiles, v, "")
        
        
        return len(list(set(res)))
        	    
                    
def main():

    s = Solution()

    test_cases = [
    		"AAB",
    		"AAABBC",
    		"V",
        ]
        
    for i, test in enumerate(test_cases):
    	print("[%d]" % (i + 1))
    	print("Input: ", test)
    	print("Output:", s.numTilePossibilities(test))
    	print('\n')

if __name__ == "__main__":
    loggerTest = logging.getLogger("test")
    loggerTest.setLevel(logging.INFO) # DEBUG < INFO < WARNING < ERROR < CRITICAL  
    #formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    streamHander = logging.StreamHandler()
    #streamHander.setFormatter(formatter)
    loggerTest.addHandler(streamHander)

    main()    
  