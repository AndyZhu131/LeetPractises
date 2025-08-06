#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        step = []
        for i in range(n):
            if i == 0: step.append(1)
            elif i == 1: step.append(2)
            else:
                newStep = step[0] + step[1]
                step.pop(0)
                step.append(newStep)
        return step[-1]
        
# @lc code=end

