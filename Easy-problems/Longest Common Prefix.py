class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # common_pre = ''
        # min_l = min(len(s) for s in strs)
        # common_prefix = ''
        # for i in range(min_l):
        #     current = strs[0][i]
        #     for s in strs:
        #         if s[i] != current:
        #             return common_prefix
        #     common_prefix += current
        # return common_prefix