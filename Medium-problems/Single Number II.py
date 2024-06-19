# Solution 1: run time:38ms and memory: 13.7mb
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict1 = {}
        for x in nums:
            if x not in dict1:
                dict1[x] = 1
            else:
                dict1[x] += 1
                
        for x in dict1:
            if dict1[x] == 1:
                return x


#Solution 2: runtime: 633ms and memory: 12.9mb
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for rtype in nums:
            if nums.count(rtype) == 1:   #.count() increases runtime
                return rtype