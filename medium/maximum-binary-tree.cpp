/*
"""
654. Maximum Binary Tree

Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

The root is the maximum number in the array.
The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
Construct the maximum tree by the given array and output the root node of this tree.
"""

"""
Note:
The size of the given array will be in the range [1,1000].
"""

"""
Example 1:
Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

	  6
	/   \
   3     5
	\    /
	 2  0
	   \
		1
"""
*/

#include "stdafx.h"

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
	TreeNode* constructMaximumBinaryTree(vector<int>& nums) {
		return helper(nums);
	}

	TreeNode* helper(vector<int> vec) {
		TreeNode* newNode = new TreeNode();

		if (vec.size() == 0) {
			return NULL;
		}
		else {
			// create array of vectors to sotre the sub-vectors
			int maxIdx = std::distance(vec.begin(), std::max_element(vec.begin(), vec.end()));
			int maxVal = vec[maxIdx];

			printf("max index: %d\n", maxIdx);
			int num_sz = vec.size();
			int left_sz = maxIdx;
			int right_sz = num_sz - (maxIdx + 1);

			newNode->val = maxVal;

			if (left_sz > 0) {
				std::vector<int> left_vec;
				left_vec.resize(left_sz);

				printf("left: ");
				for (int i = 0; i < maxIdx; i++) {
					left_vec.push_back(vec[i]);
					printf("%d ,", vec[i]);
				}

				newNode->left = constructMaximumBinaryTree(left_vec);
			}

			if (right_sz > 0) {
				std::vector<int> right_vec;
				right_vec.resize(right_sz);

				printf("right: ");
				for (int i = maxIdx + 1; i < num_sz; i++) {
					right_vec.push_back(vec[i]);
					printf("%d ,", vec[i]);
				}

				newNode->right = constructMaximumBinaryTree(right_vec);
			}

		}

		return newNode;
	}
};

int main(int argc char *argv) {

	Solution s = new Solution();

	vector<int> input = { 3, 2, 1, 6, 0, 5 };
	s.constructMaximumBinaryTree(input);

	return 0;
}