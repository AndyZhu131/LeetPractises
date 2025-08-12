#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for s in strs:
            sortedS = ''.join(sorted(s))
            if sortedS in dict:
                dict[sortedS].append(s)
            else:
                dict[sortedS] = [s]
        twoD = []
        for l in dict:
            twoD.append(dict[l])
        return twoD
        
# @lc code=end

