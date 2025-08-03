from typing import List

#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if self.allNegCheck(nums):
            return max(nums)
        sum = [0, 0, 0]
        isPos = True
        index = 0
        for x in nums:
            isPos = x >= 0
            if not isPos and index == 0:
                index = 1
            elif isPos and index == 1:
                index = 2
            elif not isPos and index == 2:
                index = 1
                self.calculate(sum)
            sum[index] += x
            print(sum)
        
        self.calculate(sum)
        return max(sum)
    
    def calculate(self, sum: List[int]):
        if sum[0] + sum[1] > 0 and sum[1] + sum[2] > 0:
            sum[0] = sum[0] + sum[1] + sum[2]
        else:
            sum[0] = max(sum)
        sum[1] = 0
        sum[2] = 0
    
    def allNegCheck(self, nums):
        if not nums:
            return 0
            
        # Handle case with all negative numbers
        all_negative = True
        for num in nums:
            if num >= 0:
                all_negative = False
                break
        print(f"all negative check: {all_negative}")
        
        return all_negative
        
# @lc code=end

# Test case
if __name__ == "__main__":
    solution = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]


    result = solution.maxSubArray(nums)
    expected = 6
    print(f"Input: {nums}")
    print(f"Expected: {expected}, Got: {result}")
    print(f"Pass: {result == expected}")

