#Needs to be fixed
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        output = []
        for x in range(len(list1)):
            output.append(list1[x])
            output.append(list2[x])
    
        return output