class Solution(object):
    def isSameAfterReversals(self, num):
        """
        :type num: int
        :rtype: bool
        """
        s=int(str(num)[::-1])
        s1=int(str(s)[::-1])
        return num==s1