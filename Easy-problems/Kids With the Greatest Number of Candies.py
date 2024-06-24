# class Solution(object):
#     def kidsWithCandies(self, candies, extraCandies):
#         """
#         :type candies: List[int]
#         :type extraCandies: int
#         :rtype: List[bool]
#         """
#         output = []
#         for x in range(len(candies)):
#             total_c = candies[x] + extraCandies
#             output.append(total_c >= max(candies))
#             total_c = 0
#         return output

#Simplifies to

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        output = []
        for x in range(len(candies)):
            output.append(candies[x] + extraCandies >= max(candies))
        return output