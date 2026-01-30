class Solution(object):
    def maxProductDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        min=nums[0]*nums[1]
        max=nums[len(nums)-1]*nums[len(nums)-2]
        return max-min
                