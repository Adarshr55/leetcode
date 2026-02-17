class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        num=nums1+nums2
        num=sorted(num)
        if len(num)%2==0:
            res= (num[len(num)//2]+num[len(num)//2-1])
            return res /2.0
        else:
            return(num[len(num)//2])
        