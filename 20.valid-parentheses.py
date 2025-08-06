#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for b in s:
            if b == '(' or b == '[' or b == '{':
                stack.append(b)
            else:
                if not stack: return False
                last = stack.pop()
                if b == ')' and last != '(':
                    return False
                if b == ']' and last != '[':
                    return False
                if b == '}' and last != '{':
                    return False
        if len(stack) != 0: return False
        return True
                


        
# @lc code=end

