class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        le=len(prices)
        min=prices[0]
        max=0
        for i in range(1,len(prices)):
            if prices[i]<min:
                min=prices[i]
            else:
                dif=prices[i]-min
                if dif>max:
                    max=dif
        return max  
