"""
275. H-Index II

Given an array of citations sorted in ascending order (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."
"""

"""
Note:

If there are several possible values for h, the maximum one is taken as the h-index.

Follow up:

This is a follow up problem to H-Index, where citations is now guaranteed to be sorted in ascending order.
Could you solve it in logarithmic time complexity?
"""

"""
Example:

Input: citations = [0,1,3,5,6]
Output: 3 
Explanation: [0,1,3,5,6] means the researcher has 5 papers in total and each of them had 
             received 0, 1, 3, 5, 6 citations respectively. 
             Since the researcher has 3 papers with at least 3 citations each and the remaining 
             two with no more than 3 citations each, her h-index is 3.

"""

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        n = len(citations)
        for h in range(1, n+1):
            moreThanPapers = len(set(list(filter(lambda x: x >= h, citations))))
            lessThanPapers = n - moreThanPapers

            print('(1)h:', h, ',(2)n-h:', n-h, ',(3)countif([],>= (1)):', moreThanPapers, ',(4) n-(3):', lessThanPapers, ',(1)==(3):', h==moreThanPapers, ',(2)==(4):', (n-h)==lessThanPapers)
            if (n - h) == lessThanPapers and (h == moreThanPapers):
                return h

        return 0

def main():

    s = Solution()

    listInput = [[0, 1, 3, 5, 6],
             [0],
             [1],
             [11, 15],
             [1, 1],
             [1, 2]]

    for i, input in enumerate(listInput):
        print("[%d]"% (i+1))
        print("Input:", input)
        print("Output:", s.hIndex(input))
        print('\n')

if __name__ == "__main__":
    main()    
  