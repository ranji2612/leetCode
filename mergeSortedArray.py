# Merge Sorted Array
# https://leetcode.com/problems/merge-sorted-array/

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        import copy
        x = copy.deepcopy(nums1)
        i=j=k=0
        while i<m or j<n:
            if j>=n or (i<m and x[i]<=nums2[j]):
                nums1[k]=x[i]
                i+=1
            else:
                nums1[k] = nums2[j]
                j+=1
            k+=1
        print nums1
        return
                