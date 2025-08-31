class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """ 
        nums = nums1 + nums2
        nums.sort() # sort the combined nums

        total_length = len(nums)

        # Odd length
        if total_length % 2 == 1:
            mid = total_length // 2
            return nums[mid]
        # Even length
        else:
            mid1 = total_length // 2
            mid2 = mid1 - 1
            return (nums[mid1] + nums[mid2]) / 2.0
