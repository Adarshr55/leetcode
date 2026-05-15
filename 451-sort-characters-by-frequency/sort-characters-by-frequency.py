class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq={}
        res=''
        for i in s:
            freq[i]=freq.get(i,0)+1
        max_freq=max(freq.values())
        for f in range(max_freq,0,-1):
            for ch,c in freq.items():
                if c==f:
                    res+=ch*c
        return res
