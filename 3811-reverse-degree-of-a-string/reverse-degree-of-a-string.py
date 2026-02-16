class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=0
        z=0
        for i in range(len(s)):
            n=(27-(ord(s[i])-96))
            z+=n*(i+1)
        return z
