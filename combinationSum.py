# Combination Sum
# https://leetcode.com/problems/combination-sum/

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(candidates)==0 or target<=0:
            return [[]] if target==0 else []
        candidates.sort()
        
        j = len(candidates)-1
        res = []
        
        while j>=0:
            for x in self.combinationSum(candidates[:j+1],target-candidates[j]):
                res.append(x+[candidates[j]])
            j-=1
        return res