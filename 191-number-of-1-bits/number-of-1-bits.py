class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        s= bin(n)
        count=0
        for i in s:
            if i=="1":
                count+=1
        return count
