#This approach only passed 81/98 testcase

# class Solution(object):
#     def isValid(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         strs = ["()","{}","[]"]
#         check = ""
#         Valid = False
#         midway = len(s)//2

#         if len(s)%2 != 0:
#             return Valid

#         for x in range(len(s)):
#             check_1 = s[x] + s[-1-x]
#             if check_1 in strs:
#                 Valid = True
#                 if midway == x + 1:
#                     return Valid
#             else:
#                 Valid = False
#                 break

       
#         if Valid:
#             return Valid
#         else:
#             for x in range(len(s)):
#                 check += s[x]
#                 if len(check)%2 == 0:
#                     if check in strs:
#                         Valid = True
#                         check = ""
#                     else:
#                         Valid = False
#                         break
#                 else:
#                     continue

#             return Valid