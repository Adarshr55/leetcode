class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        """
        :type x: int
        :rtype: int
        """
        sum=0
        s=str(x)
        for i in s:
            sum+=int(i)
        if x%sum==0:
            return sum
        return -1