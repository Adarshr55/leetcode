class Solution(object):
    def search(self, nums, target):
        for i,v in enumerate(nums):
            if v==target:
                return i
        return -1
