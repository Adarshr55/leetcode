class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        runningSum=[]
        total_sum=0
        for number in nums:
            total_sum+=number
            runningSum.append(total_sum)
        return runningSum