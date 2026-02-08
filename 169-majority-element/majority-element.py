class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=set(nums)
        res=None
        max_count=0
        for i in s:
            count=0
            for n in nums:
                if i==n:
                    count+=1
                if count>max_count:
                    max_count=count
                    res=i
        return res

