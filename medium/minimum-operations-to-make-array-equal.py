

"""
1551. Minimum Operations to Make Array Equal

You have an array arr of length n where arr[i] = (2 * i) + 1 for all valid values of i (i.e. 0 <= i < n).
In one operation, you can select two indices x and y where 0 <= x, y < n and subtract 1 from arr[x] and add 1 to arr[y] (i.e. perform arr[x] -=1 and arr[y] += 1). The goal is to make all the elements of the array equal. It is guaranteed that all the elements of the array can be made equal using some operations.
Given an integer n, the length of the array. Return the minimum number of operations needed to make all the elements of arr equal.
"""

"""
Constraints:
1 <= n <= 10^4
"""

"""
Example 1:
Input: n = 3
Output: 2
Explanation: arr = [1, 3, 5]
First operation choose x = 2 and y = 0, this leads arr to be [2, 3, 4]
In the second operation choose x = 2 and y = 0 again, thus arr = [3, 3, 3].
Example 2:
Input: n = 6
Output: 9

"""
import sys
import logging

class Solution(object):
    def minOperations(self, n):
        """
        :type n: int
        :rtype: int
        """              			
        	
        arr =	[2*i+1 for i in range(n)]        
        arr = list(map(lambda x: abs(x-n), arr))
        	
        return int(sum(arr)/2)
        
        
def main():

    s = Solution()

    test_cases = [
        3,					# 1
        6,					# 2
        4,					# 3       
        ]	

    for i, test in enumerate(test_cases):
        print("[%d]"% (i + 1))
        print("Input: ", test)
        print("Output:", s.minOperations(test))
        print('\n')

if __name__ == "__main__":
    loggerTest = logging.getLogger("test")
    loggerTest.setLevel(logging.INFO) # DEBUG < INFO < WARNING < ERROR < CRITICAL  
    #formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    streamHander = logging.StreamHandler()
    #streamHander.setFormatter(formatter)
    loggerTest.addHandler(streamHander)

    main()    
  