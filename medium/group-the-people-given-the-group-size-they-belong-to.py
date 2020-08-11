"""
1282. Group the People Given the Group Size They Belong To

There are n people whose IDs go from 0 to n - 1 and each person belongs exactly to one group. Given the array groupSizes of length n telling the group size each person belongs to, return the groups there are and the people's IDs each group includes.

You can return any solution in any order and the same applies for IDs. Also, it is guaranteed that there exists at least one solution. 

"""

"""
Constraints:

groupSizes.length == n
1 <= n <= 500
1 <= groupSizes[i] <= n
"""

"""
Input: groupSizes = [3,3,3,3,3,1,3]
Output: [[5],[0,1,2],[3,4,6]]
Explanation: 
Other possible solutions are [[2,1,6],[5],[0,4,3]] and [[5],[0,6,2],[4,3,1]].

Input: groupSizes = [2,1,3,3,3,2]
Output: [[1],[0,5],[2,3,4]]
"""

class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        for idx, val in  enumerate(groupSizes):
            if(val>0):
                grouped = []
                grouped.append(idx)

                i = 1
                cnt = val - 1
                while(cnt > 0):                    
                    if(groupSizes[idx+i] == val):
                        groupSizes[idx+i] = 0
                        grouped.append(idx+i)
                        cnt -= 1
                    i += 1

                ans.append(grouped)


        return ans