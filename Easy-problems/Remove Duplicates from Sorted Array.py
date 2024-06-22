#This satisfies answer to the question, but solution doesnt work
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        output = []
        for x in nums:
            if x not in output:
                output.append(x)
        
        return output #or len(output)