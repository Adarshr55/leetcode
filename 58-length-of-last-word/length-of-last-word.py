class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        word=0
        res=s.split()
        for i in range(len(s)):
            if i==len(res)-1:
                word=len(res[i])
        return word
                
        