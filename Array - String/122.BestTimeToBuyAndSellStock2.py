#Snippet how to sum positive differneces between adjacent

# def sum_positive_diffs(arr):
#     total_gain = 0
#     for i in range(1, len(arr)):
#         # If there's and increase, add it to the total_gain
#         total_gain += max(0, arr[i] - arr[i-1])
#     return total_gain

# data = [10,12,8,15,5,9,15,14]
# # Captures 12-10=2, then 15-8=7, then 9-5=4. Total 2+7+4 = 13
# print(sum_positive_diffs(data))


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_gain = 0
        for i in range(1, len(prices)):
            total_gain += max(0, prices[i] - prices[i-1])
        return total_gain

# Solved at 5 mins.


# Algorithm: This is a Greedy Algorithm.
# Complexity:
# Time Complexity: O(n). You iterate through the prices list once. The operations inside the loop (len, range, comparison, subtraction, max, addition) take constant time.
# Space Complexity: O(1). You are only using a single variable (total_gain) to store the result, regardless of the input size.