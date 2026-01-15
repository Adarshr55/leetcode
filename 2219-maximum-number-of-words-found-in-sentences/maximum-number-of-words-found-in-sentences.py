class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        word=0
        for i in sentences:
            res=i.split()
            if len(res)>word:
                word=len(res)
        return word
