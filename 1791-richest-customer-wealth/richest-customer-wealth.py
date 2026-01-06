class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        sum=0
        for args in accounts:
            summed=reduce(lambda x,y:x+y,args)
            if summed>sum:
                sum=summed
        return sum
        