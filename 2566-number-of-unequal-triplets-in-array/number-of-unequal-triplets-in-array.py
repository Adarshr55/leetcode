class Solution(object):
    def unequalTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # from collections import Counter
        freq=Counter(nums)
        total=len(nums)
        left_sum=0
        ans=0
        for  i in freq.values():
            right_sum=total - left_sum-i
            ans+=left_sum * i *right_sum
            left_sum+=i
        return ans