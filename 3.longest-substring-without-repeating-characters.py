#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subString = []
        curLength = 0
        maxLength = 0
        for c in s:
            if c in subString:
                while subString[0] != c:
                    subString.pop(0)
                    curLength -= 1 
                subString.pop(0)
                curLength -= 1
            subString.append(c)
            curLength += 1
            if curLength > maxLength: maxLength = curLength
        return maxLength



# @lc code=end

