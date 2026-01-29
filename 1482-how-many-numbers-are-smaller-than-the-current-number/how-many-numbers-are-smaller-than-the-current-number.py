class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        max_val=max(nums)
        count=[0]*(max_val+1)
        for num in nums:
            count[num]+=1

        for i in range(1,len(count)):

            count[i]+=count[i-1]

        result=[]
        for num in nums:
            if num==0:
                result.append(0)
            else:
                result.append(count[num-1])
        return result
        
