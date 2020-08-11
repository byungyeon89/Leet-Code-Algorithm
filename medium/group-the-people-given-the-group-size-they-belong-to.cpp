/*
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
*/
#include "stdafx.h"

class Solution {
public:
	vector<vector<int>> groupThePeople(vector<int>& groupSizes) {
		// : type  groupSizes : vector<int>
		// : rtype : vector<vector<int>>

		vector<int>::iterator it;
		vector<vector<int>> ans;				
		size_t i = 0;

		for (size_t i = 0; i < groupSizes.size(); ++i) {
			if (groupSizes[i]) {
				vector<int> grouped;
				grouped.push_back(i);

				size_t val = groupSizes[i];
				size_t cnt = val - 1;
				size_t j = 1;

				while (cnt > 0) {
					if (val == groupSizes[i+j]) {
						groupSizes[i + j] = 0;
						grouped.push_back(i+j);
						cnt -= 1;
					}
					++j;
				}				
				ans.push_back(grouped);
			}
		}
		return ans;
	}
};
