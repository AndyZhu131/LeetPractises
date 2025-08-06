from typing import List

#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        # Kadane's Algorithm - O(n) time, O(1) space
        current_sum = nums[0]
        max_sum = nums[0]
        
        for i in range(1, len(nums)):
            # Either extend the current subarray or start a new one
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)
        
        return max_sum
        
# @lc code=end

# Test case
if __name__ == "__main__":
    solution = Solution()
    nums = [-9,-2,1,8,7,-6,4,9,-9,-5,0,5,-2,5,9,7]



    result = solution.maxSubArray(nums)
    expected = 33
    print(f"Input: {nums}")
    print(f"Expected: {expected}, Got: {result}")
    print(f"Pass: {result == expected}")

