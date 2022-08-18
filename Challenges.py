## When solving problems , think outside the box and be creative.Look at the problem from another angle !

##https://www.hackerrank.com/challenges/plus-minus/problem
#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# #
# # Complete the 'plusMinus' function below.
# #
# # The function accepts INTEGER_ARRAY arr as parameter.
# #

# def plusMinus(arr):
#     # Write your code here
#     positive_nums = []
#     negative_nums = []
#     zeros = []
#     n = len(arr)
#     for num in arr :
#         if num >0:
#             positive_nums.append(num)
#         elif num<0:
#             negative_nums.append(num)
#         elif num==0:
#             zeros.append(num)
#         p_len = len(positive_nums)
#         n_len = len(negative_nums)
#         z_len = len(zeros)
#         coef_p= p_len/n
#         coef_n= n_len/n
#         coef_z= z_len/n
#     print(coef_p)






#     print(coef_n)
#     print(coef_z)   
# if __name__ == '__main__':
#     n = int(input().strip())

#     arr = list(map(int, input().rstrip().split()))

#     plusMinus(arr)


symbol = "#"
space = ' '
for i in range(1,6+1):
    print(space * (6-i)+symbol*i)
    
#day 1 https://www.hackerrank.com/challenges/30-data-types/problem?isFullScreen=true
#day 2 https://www.hackerrank.com/challenges/list-comprehensions/problem
#day 3  https://www.hackerrank.com/challenges/utopian-tree 
#day 4 https://www.hackerrank.com/challenges/mini-max-sum/
#day 5 https://www.hackerrank.com/challenges/birthday-cake-candles/,
#day 6 https://www.hackerrank.com/challenges/30-review-loop ,https://www.hackerrank.com/challenges/find-digits/problem
#day 7 https://www.hackerrank.com/challenges/30-arrays 
#day 8 https://www.hackerrank.com/challenges/30-dictionaries-and-maps/forum      
#day 9 https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem
# n = int(input())
# users = [input().split() for _ in range(n)]
# mydict = {user: phone for user,phone in users}
# while True:
#     try:
#         name = input()
#         if name in mydict:
#             print('%s=%s' % (name, mydict[name]))
#         else:
#             print("Not found")
#     except:
#         break



#day 9 https://www.hackerrank.com/challenges/30-recursion/problem
# def factorial(n):
#     # Write your code here
#     if n == 1:
#         return 1
#     elif n>1:
#         return n*factorial(n-1)  



#day 10 https://www.hackerrank.com/challenges/diagonal-difference
# def diagonalDifference(arr):
#     # Write your code here
#     immut = len(arr)
#     n   = len(arr)
#     prim_d = 0
#     sec_d = 0
#     count = 1
#     for i in arr:
#         prim_d += i[immut-n]
#         sec_d += i[immut-count]
#         count+=1 
#         n-=1
#     return abs(prim_d-sec_d)




#day 12 https://www.hackerrank.com/challenges/30-inheritance

# class Student(Person):
#      def __init__(self, firstName, lastName, idNumber,scores):
#         super().__init__(firstName, lastName, idNumber)
#         self.scores = scores
          
#      def calculate(self):
#             overall = 0
#             count = 0 
#             for score in self.scores:
#                 overall += score
#                 count += 1
#             result = overall/count
#             if result>=90 and result<=100:
#                 return "O"
#             if result>=80 and result<90:
#                 return "E"
#             if result>=70 and result<80:
#                 return "A"
#             if result>=55 and result<70:
#                 return "P"
#             if result>=40 and result<55:
#                 return "D"
#             if result<40:
#                 return "T"


#day 12 Palindrome number :-------->>>>> 1 version 
# def isPalindrome(numbasString):
#    reverseStr = ''
#    for i  in  range(1,len(numbasString)+1):
#         reverseStr += numbasString[-i]
#    if reverseStr == numbasString :
#     return True
#    else:
#     return False

# -------->>>>>>>> 2 version 

# def isPalindrome(numbasString):
#    reverseStr = ''
#    reverseStr = numbasString[::-1]
#    if reverseStr == numbasString :
#     return True
#    else:
#     return False


#day 13 https://www.hackerrank.com/challenges/30-abstract-classes?isFullScreen=true
#day 14 https://www.hackerrank.com/challenges/30-scope/problem?
# class Difference:
#     def __init__(self, a):
#         self.__elements = a
#         self.maximumDifference = 0
# 	# Add your code here
    
#     def computeDifference(self):
#        result = max(self.__elements) - min(self.__elements)
#        self.maximumDifference = result

##
## day 15 https://www.hackerrank.com/challenges/validating-the-phone-number
# import re
# n = int(input())
# for i in range(n):
#     testString = input()
#     match = re.search('^\s*[7-9]',testString)
#     if match and len(testString) == 10 and testString.isdigit():
#         print("YES")
#     else:
#         print("NO")


# day 16 https://www.hackerrank.com/challenges/30-exceptions-string-to-integer
# S = input()
# try:
#     print(int(S))
# except ValueError:
#     print("Bad String")
    
#day 17 https://www.hackerrank.com/challenges/30-more-exceptions

# class Calculator:
    
#     def power(self,n,p):
#         if n < 0 or p < 0:
#              raise Exception("n and p should be non-negative")
#         else:
#             result = n**p
#             return result
