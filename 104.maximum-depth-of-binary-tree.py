#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None: return 0
        maxRight, maxLeft = 0, 0
        if root.right != None:
            maxRight = self.maxDepth(root.right)
        if root.left != None:
            maxLeft = self.maxDepth(root.left)
        
        if maxLeft > maxRight: return maxLeft+1
        else: return maxRight+1

        
# @lc code=end

