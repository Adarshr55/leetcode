class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        freq={}
        for i in arr:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        max=0
        for i in freq:
            if i==freq[i]:
                if max<i:
                    max=i
        if max==0:
            return -1
        else:
            return max