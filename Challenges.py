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
