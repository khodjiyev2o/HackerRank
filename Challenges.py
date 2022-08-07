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
#day 6 https://www.hackerrank.com/challenges/30-review-loop ,
    
        
