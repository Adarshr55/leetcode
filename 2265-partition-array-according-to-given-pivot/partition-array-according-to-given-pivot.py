class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        gt=[]
        lt=[] 
        eq=[]
        for i in nums:
            if i<pivot:
                lt.append(i)
            elif i>pivot:
                gt.append(i)
            else:
                eq.append(i)
        res=lt+eq+gt
        return res