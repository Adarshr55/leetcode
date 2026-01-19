class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        k=celsius+273.15
        fa=celsius*1.80+32.00
        
        return  [k,fa]