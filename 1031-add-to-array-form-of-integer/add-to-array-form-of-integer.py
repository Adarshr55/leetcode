class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        n=int("".join([str(i)for i in num]))
        sum=n+k
        res=[int(i)for i in str(sum)]
        return res