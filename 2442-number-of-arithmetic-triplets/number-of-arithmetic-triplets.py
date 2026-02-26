class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """
        newset=set(nums)
        count=0
        for i in range(len(nums)):
            if nums[i]+diff in newset and nums[i]+ 2*diff in newset:
                count+=1
        return count