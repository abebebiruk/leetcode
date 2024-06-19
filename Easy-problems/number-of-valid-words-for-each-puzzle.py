
def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum = 1
        count = 0
        for x in range(3):
            if -1*min(nums) >= max(nums) and count < 2:
                maximum *= min(nums)
                nums.remove(min(nums))
                count += 1
            else:
                maximum *= max(nums)
                nums.remove(max(nums))
        return maximum
        # Need to account for more test-cases


        # Possible Solution

        # min1=min2=float('inf')
        # max1=max2=max3=float('-inf')
        # for num in nums:
        #     if num < min1:
        #         min2 = min1
        #         min1 = num
        #     elif num < min2:
        #         min2 = num
        #     if num>max1:
        #         max3=max2
        #         max2=max1
        #         max1=num
        #     elif num>max2:
        #         max3=max2
        #         max2=num
        #     elif num>max3:
        #         max3=num
        # return max(max1*min1*min2, max1*max2*max3)
             
