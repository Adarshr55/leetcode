class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        x= s.split()
        x.sort(key=lambda word:int(word[-1]))
        result=[word[:-1]for word in x]
        n=(" ".join(result))
        return n