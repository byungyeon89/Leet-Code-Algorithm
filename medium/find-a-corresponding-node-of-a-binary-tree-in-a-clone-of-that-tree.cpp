/*
"""
1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree

Given two binary trees original and cloned and given a reference to a node target in the original tree.

The cloned tree is a copy of the original tree.

Return a reference to the same node in the cloned tree.

Note that you are not allowed to change any of the two trees or the target node and the answer must be a reference to a node in the cloned tree.

Follow up: Solve the problem if repeated values on the tree are allowed.

"""

"""
Constraints:

The number of nodes in the tree is in the range [1, 10^4].
The values of the nodes of the tree are unique.
target node is a node from the original tree and is not null.
"""

"""
Input: tree = [7,4,3,null,null,6,19], target = 3
Output: 3
Explanation: In all examples the original and cloned trees are shown. The target node is a green node from the original tree. The answer is the yellow node from the cloned tree.
"""
*/

#include "stdafx.h"

// Definition for a binary tree node.
struct TreeNode {
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
	TreeNode* getTargetCopy(TreeNode* original, TreeNode* cloned, TreeNode* target) {
		if (cloned == NULL) {
			return NULL;
		}
		else {
			if (cloned->val == target.val) {
				return cloned;
			}
			else {
				TreeNode *pTreeleft = getTargetCopy(original, cloned->left, target);
				TreeNode *pTreeright = getTargetCopy(original, cloned->left, target);

				if (pTreeleft != NULL) {
					return pTreeleft;
				}
				else if (pTreeright != NULL) {
					return pTreeright;
				}
				else {
					printf("can not find matchted target value in the cloned tree!!!\n");
				}
			}
		}
	}
};