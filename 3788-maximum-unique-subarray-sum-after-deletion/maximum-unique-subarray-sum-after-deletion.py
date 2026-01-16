class Solution(object):
    def maxSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p=[]
        n=[]
        s=set()
        for i in range(len(nums)):
            if nums[i]>=0:
                p.append(nums[i])
            else:
                n.append(nums[i])
        if len(p)>0:
            s=set(p)
            return(sum(s))
        else:
            return (max(n))

            