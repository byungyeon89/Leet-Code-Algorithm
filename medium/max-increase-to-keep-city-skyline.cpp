/*
"""
807. Max Increase to Keep City Skyline

In a 2 dimensional array grid, each value grid[i][j] represents the height of a building located there.We are allowed to increase the height of any number of buildings, by any amount(the amounts can be different for different buildings).Height 0 is considered to be a building as well.

At the end, the "skyline" when viewed from all four directions of the grid, i.e.top, bottom, left, and right, must be the same as the skyline of the original grid.A city's skyline is the outer contour of the rectangles formed by all the buildings when viewed from a distance. See the following example.

What is the maximum total sum that the height of the buildings can be increased ?

"""

"""
Notes :

	1 < grid.length = grid[0].length <= 50.
	All heights grid[i][j] are in the range[0, 100].
	All buildings in grid[i][j] occupy the entire grid cell : that is, they are a 1 x 1 x grid[i][j] rectangular prism.
	"""

	"""
	Example :
	Input : grid = [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]
	Output : 35
	Explanation :
	The grid is :
[[3, 0, 8, 4],
[2, 4, 5, 7],
[9, 2, 6, 3],
[0, 3, 1, 0]]

The skyline viewed from top or bottom is : [9, 4, 8, 7]
The skyline viewed from left or right is : [8, 7, 9, 3]

The grid after increasing the height of buildings without affecting skylines is :

gridNew = [[8, 4, 8, 7],
[7, 4, 7, 7],
[9, 4, 8, 7],
[3, 3, 3, 3]]
"""
*/

#include "stdafx.h"


class Solution {
public:
	int maxIncreaseKeepingSkyline(vector<vector<int>>& grid) {
		size_t sum = 0;

		vector<int> skylineTB, skylineLR;
				
		for (size_t c = 0; c < grid.size(); c++) {			
			int rowMax = grid[c][0];
			for (size_t r = 1; r < grid[0].size(); r++) {
				if (rowMax < grid[c][r]) {
					rowMax = grid[c][r];
				}
			}
			skylineTB.push_back(rowMax);
		}

		for (size_t r = 0; r < grid[0].size(); r++) {
			int colMax = grid[0][r];
			for (size_t c = 1; c < grid.size(); c++) {
				if (colMax < grid[c][r]) {
					colMax = grid[c][r];
				}
			}
			skylineLR.push_back(colMax);
		}




		return sum;
	}
};
