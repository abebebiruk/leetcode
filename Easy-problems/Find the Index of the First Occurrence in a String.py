class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for x in range(len(haystack)):
            if haystack[x:len(needle)+x] == needle:
                return x
        return -1
    