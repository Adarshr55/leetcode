class Solution(object):
    def countPairs(self, nums, k):
        count=0
        for i,v in enumerate(nums):
            for j,va in enumerate(nums):
                if i<j and v==va and i*j%k==0:
                    count+=1
        return count
        