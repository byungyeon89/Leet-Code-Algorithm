"""
763. Partition Labels

A string S of lowercase English letters is given. 
We want to partition this string into as many parts as possible so that each letter appears in at most one part, 
and return a list of integers representing the size of these parts.
"""

"""
Note:
	• S will have length in range [1, 500].
S will consist of lowercase English letters ('a' to 'z') only.
"""

""" 
Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
"""
import sys
import logging

class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """                
        ans = []   
        
        def findLastIdx(val, ary):
        	idx = [i for i,x in enumerate(ary) if x == val]
        	
        	if idx:
        		return max(idx)
        	else:
        		return 0
        		
        	
        cnt = 0
        target = 0
        for curr in range(0, len(S)):
        	cnt = cnt + 1
        	target = max(target, curr + findLastIdx(S[curr], S[curr:])) 
        		
        	if curr == target:
        		ans.append(cnt)
        		cnt = 0
        		target = curr + 1                	
        		
        return ans
        		
        	
        
        
def main():

    s = Solution()

    test_cases = [
        "ababcbacadefegdehijhklij",			# 1
        "caedbdedda",										# 2
        "eaaaabaaec",										# 3       
        ]	

    for i, test in enumerate(test_cases):
        print("[%d]"% (i + 1))
        print("Input: ", test)
        print("Output:", s.partitionLabels(test))
        print('\n')

if __name__ == "__main__":
    loggerTest = logging.getLogger("test")
    loggerTest.setLevel(logging.INFO) # DEBUG < INFO < WARNING < ERROR < CRITICAL  
    #formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    streamHander = logging.StreamHandler()
    #streamHander.setFormatter(formatter)
    loggerTest.addHandler(streamHander)

    main()    
  