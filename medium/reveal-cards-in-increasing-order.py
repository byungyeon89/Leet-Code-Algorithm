"""
950. Reveal Cards In Increasing Order
Medium
980173Add to ListShare
In a deck of cards, every card has a unique integer.  You can order the deck in any order you want.
Initially, all the cards start face down (unrevealed) in one deck.
Now, you do the following steps repeatedly, until all cards are revealed:
	1. Take the top card of the deck, reveal it, and take it out of the deck.
	2. If there are still cards in the deck, put the next top card of the deck at the bottom of the deck.
	3. If there are still unrevealed cards, go back to step 1.  Otherwise, stop.
Return an ordering of the deck that would reveal the cards in increasing order.
The first entry in the answer is considered to be the top of the deck.
 
Example 1:
Input: [17,13,11,2,3,5,7]
Output: [2,13,3,11,5,17,7]
Explanation: 
We get the deck in the order [17,13,11,2,3,5,7] (this order doesn't matter), and reorder it.
After reordering, the deck starts as [2,13,3,11,5,17,7], where 2 is the top of the deck.

1,2,3,4,5,6,7

#2 [1,2]
#3 [1,3,2]
#4 [1,3,2,4]
#5 [1,4,2,5,3]
#7 [1,6,2,5,3,7,4]

[1,5,2,4,3]
1, [2,4,3,5]
2, [3,5,4]
3, [4,5]
4, [5]
5

We reveal 2, and move 13 to the bottom.  The deck is now [3,11,5,17,7,13].
We reveal 3, and move 11 to the bottom.  The deck is now [5,17,7,13,11].
We reveal 5, and move 17 to the bottom.  The deck is now [7,13,11,17].
We reveal 7, and move 13 to the bottom.  The deck is now [11,17,13].
We reveal 11, and move 17 to the bottom.  The deck is now [13,17].
We reveal 13, and move 17 to the bottom.  The deck is now [17].
We reveal 17.
Since all the cards revealed are in increasing order, the answer is correct.

 
Note:
	1. 1 <= A.length <= 1000
	2. 1 <= A[i] <= 10^6
	3. A[i] != A[j] for all i != j


"""
import sys
import logging

import tree
                
class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        
        deck = sorted(deck, reverse=True)        
        
        re_deck = []   
        for val in deck:        
        	re_deck.insert(0, val)        	
        	if val == deck[-1]:
        		break
        	re_deck.insert(0, re_deck[-1])
        	re_deck.pop()		
        
        return re_deck
        
def main():

    s = Solution()

    test_cases = [    		
        		[17,13,11,2,3,5,7],
        ]
                

    for i, test in enumerate(test_cases):
    	print("[%d]" % (i + 1))
    	print("Input: ", test)
    	print("Output:", s.deckRevealedIncreasing(test))
    	print('\n')

if __name__ == "__main__":
    loggerTest = logging.getLogger("test")
    loggerTest.setLevel(logging.INFO) # DEBUG < INFO < WARNING < ERROR < CRITICAL  
    #formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    streamHander = logging.StreamHandler()
    #streamHander.setFormatter(formatter)
    loggerTest.addHandler(streamHander)

    main()    
  