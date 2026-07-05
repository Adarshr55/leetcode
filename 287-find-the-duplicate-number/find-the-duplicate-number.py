class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left=1
        right=len(nums)-1
        while left<right:
            mid=(left+right)//2
            count=sum(1 for num in nums if num <=mid)
            if count>mid:
                right=mid
            else:
                left=mid+1

        return left