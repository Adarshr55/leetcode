class Solution(object):
    def recoverOrder(self, order, friends):
        """
        :type order: List[int]
        :type friends: List[int]
        :rtype: List[int]
        """
        li=[]
        for i in order:
            for f in friends:
                if i==f:
                    li.append(i)
        return li
   