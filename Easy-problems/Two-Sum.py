class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for x in range(len(nums)):
            extra = target - nums[x]
            for y in range(x+1,len(nums)):
                if extra == nums[y]:
                    return [x,y]
                else:
                    continue
                