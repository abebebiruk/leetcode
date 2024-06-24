class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged = ""
        
        min_x = min(len(word1), len(word2))

        for x in range(min_x):
            merged += word1[x] + word2[x]
        
        if len(word1) > len(word2):
            return merged + word1[min_x:]
        elif len(word2) > len(word1):
            return merged + word2[min_x:]
        else:
            return merged