# day 1 https://leetcode.com/problems/best-time-to-buy-and-sell-stock
  
#   class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         buy = 0
#         sell = 1
#         max_profit = 0
#         while sell < len(prices) :
#             if prices[sell] > prices[buy]:
#                 current_profit = prices[sell] - prices[buy]
#                 max_profit = max(max_profit,current_profit)
#             else:
#                 buy = sell
#             sell += 1
                
                
#         return max_profit
