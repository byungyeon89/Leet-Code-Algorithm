"""
1395. Count Number of Teams

There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

You have to form a team of 3 soldiers amongst them under the following rules:

Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
A team is valid if:  (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).
"""

"""
Constraints:

n == rating.length
1 <= n <= 200
1 <= rating[i] <= 10^5
"""

"""
Example 1:

Input: rating = [2,5,3,4,1]
Output: 3
Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1). 

Example 2:

Input: rating = [2,1,3]
Output: 0
Explanation: We can't form any team given the conditions.

Example 3:

Input: rating = [1,2,3,4]
Output: 4

"""

class Solution(object):
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
            
        self.rst = 0

        self.helper(rating, 3, 0)
        self.helper(rating, 3, 1)

        return self.rst

    def helper(self, rating, n, updown:0):
        """
        :type rating: List[int]
        :type n: int
        """

        if n == 1:
            self.rst = self.rst + len(rating)
            
        else:       
            for i in range(len(rating[:-(n-1)])):
                if updown:
                    newList = list(filter(lambda x: x > rating[i], rating[i+1:]))
                else :
                    newList = list(filter(lambda x: x < rating[i], rating[i+1:]))
                if len(newList) >= (n-1) :
                    self.helper(newList, (n-1), updown)
    
def main():

    s = Solution()
    input = [2, 5, 3, 4, 1]
    #input = [1, 2, 3, 4]
    print(s.numTeams(input))


if __name__ == "__main__":
    main()
       
