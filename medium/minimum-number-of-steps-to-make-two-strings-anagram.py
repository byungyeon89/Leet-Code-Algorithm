"""
1347. Minimum Number of Steps to Make Two Strings Anagram
Medium
34026Add to ListShare
Given two equal-size strings s and t. In one step you can choose any character of t and replace it with another character.
Return the minimum number of steps to make t an anagram of s.
An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.
 
Example 1:
Input: s = "bab", t = "aba"
Output: 1
Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.
Example 2:
Input: s = "leetcode", t = "practice"
Output: 5
Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.
Example 3:
Input: s = "anagram", t = "mangaar"
Output: 0
Explanation: "anagram" and "mangaar" are anagrams. 
Example 4:
Input: s = "xxyyzz", t = "xxyyzz"
Output: 0
Example 5:
Input: s = "friend", t = "family"
Output: 4
 
Constraints:
	• 1 <= s.length <= 50000
	• s.length == t.length
s and t contain lower-case English letters only.

"""
import sys
import logging

import tree
                
class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """      
        hmap = {}                        
        for ch in t:
        	if ch in hmap.keys():
        		hmap[ch] += 1
        	else:
        		hmap[ch] = 1
        	
        
        print(hmap)
        	
        for ch in s:
        	if ch in hmap.keys():
        		if hmap[ch]>0:
        			hmap[ch] -= 1
        		        
        return sum(hmap.values())
        
        
                    
def main():

    s = Solution()

    test_cases = [    		
        		["bab", "aba"],
        		["leetcode", "practice"],
        		["anagram", "mangaar"],
        		["xxyyzz", "xxyyzz"],
        		["friend", "family"]
        ]
                

    for i, test in enumerate(test_cases):
    	print("[%d]" % (i + 1))
    	print("Input: s=", test[0], " t=", test[1])
    	print("Output:", s.minSteps(test[0], test[1]))
    	print('\n')

if __name__ == "__main__":
    loggerTest = logging.getLogger("test")
    loggerTest.setLevel(logging.INFO) # DEBUG < INFO < WARNING < ERROR < CRITICAL  
    #formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    streamHander = logging.StreamHandler()
    #streamHander.setFormatter(formatter)
    loggerTest.addHandler(streamHander)

    main()    
  