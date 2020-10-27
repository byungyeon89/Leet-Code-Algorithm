"""
890. Find and Replace Pattern
Medium
77773Add to ListShare
You have a list of words and a pattern, and you want to know which words in words matches the pattern.
A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.
(Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.)
Return a list of the words in words that match the given pattern. 
You may return the answer in any order.
 
Example 1:
Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]
Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}. 
"ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation,
since a and b map to the same letter.

Example 1: 
Input: ["abc","cba","xyx","yxx","yyx"], "abc"
Output: ["abc","cba","xyx"]
Expected: ["abc","cba"]

Note:
	• 1 <= words.length <= 50
1 <= pattern.length = words[i].length <= 20

"""
import sys
import logging

import tree
                
class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """                
        def helper(word):
        	"""
        	:type word: str
        	:rtype: List[int]
        	# For a string such as "abb" or "mee", it will return the same hash of "1,1,2,2"
        	"""	
        	patt = []
        	word_list = []
        	
        	if len(word) < 2:
        		patt.append(len(word))
        	
        	else:
        		i = 0
        		j = 1
        		
        		while i < len(word):        			        			        			
        			p = 1        			
        			if word[i] in word_list:        				
        				patt.append(word_list.index(word[i])+1)
        			else:
        				word_list.append(word[i])
        				patt.append(len(word_list))        				
        				        				        			
        			while j < len(word):
        				if word[i] == word[j]:
        					p += 1
        					j += 1
        				else:
        					break        				
        			patt.append(p)
        			
        			i = j
        			j = i + 1
        			        		
        	return patt
        
        ans = []
        for w in words:
        	if helper(pattern) == helper(w):
        		ans.append(w)		
        	
        return ans
        
def main():

    s = Solution()

    test_cases = [    		
        		[["abc","deq","mee","aqq","dkd","ccc"], "abb"],
        		[["abc","cba","xyx","yxx","yyx"], "abc"]
        ]
                

    for i, test in enumerate(test_cases):
    	print("[%d]" % (i + 1))
    	print("Input: ", test[0], test[1])
    	print("Output:", s.findAndReplacePattern(test[0], test[1]))
    	print('\n')

if __name__ == "__main__":
    loggerTest = logging.getLogger("test")
    loggerTest.setLevel(logging.INFO) # DEBUG < INFO < WARNING < ERROR < CRITICAL  
    #formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    streamHander = logging.StreamHandler()
    #streamHander.setFormatter(formatter)
    loggerTest.addHandler(streamHander)

    main()    
  