"""
921. Minimum Add to Make Parentheses Valid
Medium
88968Add to ListShare
Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', and in any positions ) so that the resulting parentheses string is valid.
Formally, a parentheses string is valid if and only if:
	• It is the empty string, or
	• It can be written as AB (A concatenated with B), where A and B are valid strings, or
	• It can be written as (A), where A is a valid string.
Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.
 
Example 1:
Input: "())"
Output: 1
Example 2:
Input: "((("
Output: 3
Example 3:
Input: "()"
Output: 0
Example 4:
Input: "()))(("
Output: 4
 
Note:
	1. S.length <= 1000
S only consists of '(' and ')' characters.

"""
import sys
import logging

import tree
                
class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        
        cnt = 0
        visited = [1 for i in range(len(S))]
                
        for i, c in enumerate(S):                	
        	if c == "(":       		         		      		        	 		
        		for j, lc in enumerate(S[i+1:]):        		
        				if visited[i+j+1] and lc== ")":
        					visited[i] = 0 
	        				visited[i+j+1] = 0
	        				break	        				
        		
        cnt += sum(visited)
        
        return cnt
        	
                    
def main():

    s = Solution()

    test_cases = [    		
        		"())",
        		"(((",
        		"()",
        		"()))((",
        ]
                

    for i, test in enumerate(test_cases):
    	print("[%d]" % (i + 1))
    	print("Input: ", test)
    	print("Output:", s.minAddToMakeValid(test))
    	print('\n')

if __name__ == "__main__":
    loggerTest = logging.getLogger("test")
    loggerTest.setLevel(logging.INFO) # DEBUG < INFO < WARNING < ERROR < CRITICAL  
    #formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    streamHander = logging.StreamHandler()
    #streamHander.setFormatter(formatter)
    loggerTest.addHandler(streamHander)

    main()    
  