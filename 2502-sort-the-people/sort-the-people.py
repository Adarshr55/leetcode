class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        d={}
        for i in range(len(names)):
            d[heights[i]]=names[i]
        sort=sorted(d.keys(),reverse=True)
        result=[]
        for s in sort:
            result.append(d[s])
        return result