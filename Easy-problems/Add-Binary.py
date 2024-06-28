class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        numb = 0
    
        for x in range(len(a)):
            if a[x] == "1":
                numb += 2**(len(a[x:])-1)

        for x in range(len(b)):
            if b[x] == "1":
                numb += 2**(len(b[x:])-1)
        
        
        numb = bin(numb)
        numb = numb.split("b")

        
        return numb[-1]