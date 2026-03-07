class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s.strip()=="":
            return 0
        else:
            a=s.split()
            return len(a)