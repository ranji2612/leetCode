# Range Sum Query
# https://leetcode.com/problems/range-sum-query-immutable/

class NumArray(object):
    s = []
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.s = [0]
        t = 0
        for i in nums:
            t+=i
            self.s.append(t)
        
    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.s[j+1]-self.s[i]


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)