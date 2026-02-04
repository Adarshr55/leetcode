class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        """
        :type nums: List[int]
        :type k: int
        :type multiplier: int
        :rtype: List[int]
        """
        for i in range(0,k):
            res= nums.index(min(nums))
            nums[res]=min(nums)*multiplier
        return nums