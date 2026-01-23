class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        vo=[]
        co=[]
        vowels="aeiou"
        for i in s:
            if i in vowels:
                vo.append(i)
            else:
                co.append(i)
        countv={i:vo.count(i) for i in vo}
        countc={i:co.count(i) for i in co}
        max_vowels=max(countv.values()) if countv else 0
        max_consonents=max(countc.values()) if countc else 0
        return max_vowels+max_consonents
                
        
