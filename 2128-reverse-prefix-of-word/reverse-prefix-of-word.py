class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        temp=''
        for i,c in enumerate(word):
            temp+=c
            if c==ch:
                rev=temp[::-1]
                return rev+word[i+1:]
        return word

