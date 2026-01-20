class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        st=set(nums)
        dub=[]
        for i in st:
            if nums.count(i)>1:
                dub.append(i)
        return dub