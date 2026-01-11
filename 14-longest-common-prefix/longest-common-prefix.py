class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return""
        prevword=strs[0]
        for i in strs[1:]:
            while not i.startswith(prevword):
                prevword=prevword[:-1]
                if not prevword:
                    return ""
        return prevword            
                    