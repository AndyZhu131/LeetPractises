#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numLength = len(nums)
        seen = {}
        for i in range(numLength):
            x = target - nums[i]
            if x in seen:
                return [seen[x], i]
            seen[nums[i]] = i
# @lc code=end

