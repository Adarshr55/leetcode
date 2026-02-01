class Solution(object):
    def minimumCost(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum=0
        first=nums[0]
        s=sorted(nums[1:])
        return first + s[0]+ s[1]




