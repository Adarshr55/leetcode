class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        var=0
        for i in range(n):
            res=start+2*i
            var^=res
        return var

