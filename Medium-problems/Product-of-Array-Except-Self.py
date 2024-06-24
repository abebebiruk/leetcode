# This runs in O(n^2) 

import numpy
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        product = []
        leng = len(nums)

        for x in range(leng):
            if nums[x] != 0:
                product.append(numpy.prod(nums)/nums[x])
            else:
                nums[x] = 1
                product.append(numpy.prod(nums))
                nums[x] = 0
        return product