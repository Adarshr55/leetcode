class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr=[]
        for i in range(len(nums)):
            count=0
            for j in range(len(nums)):
                if nums[i]==nums[j]:
                    count+=1
            if count==1:
                arr.append(nums[i])
        return sum(arr)