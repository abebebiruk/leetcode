class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = ""
        rtype = []
        
        for x in range(len(digits)):
            num += str(digits[x])
        
        num = int(num) + 1
        num = str(num)

        for x in range(len(num)):
            rtype.append(int(num[x]))
        
        return rtype
    