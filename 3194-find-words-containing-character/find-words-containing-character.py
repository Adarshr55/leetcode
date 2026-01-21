class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        li=[]
        for word in range(len(words)):
            if x in words[word]:
                li.append(word)
        return li
                
