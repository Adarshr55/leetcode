class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        number = int("".join(map(str, digits)))
        number+=1
        digits_list = [int(digit) for digit in str(number)]
        return digits_list
