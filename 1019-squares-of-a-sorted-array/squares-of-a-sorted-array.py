class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num=map(lambda x:x*x,nums)
        num.sort()
        return num