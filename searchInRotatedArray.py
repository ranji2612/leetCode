class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        x =0
        s = 0
        e = len(nums)-1
        if nums[s] > nums[e]:
            #Finding the two partitions if the array is rotated
            while s<e-1:
                m = (s+e)/2
                if nums[m] > nums[e]:
                    s = m
                else:
                    e = m
            x = s+1
            #selecting which partition to search -> Improves performance
            if target>=nums[0]:
                nums = nums[:s+1]
                x=0
            else:
                nums = nums[s+1:]
            s = 0
            e = len(nums)-1
        #Binary search to find the element
        while s<=e:
            m = (s+e)/2
            if nums[m] == target:
                return x + m
            elif nums[m]>target:
                e = m-1
            else:
                s = m+1
        return -1