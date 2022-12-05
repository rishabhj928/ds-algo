
# 1. Longest Common Subsequence
def lcs(X: str, Y: str) -> str:
    m = len(X)
    n = len(Y)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    lcs, i, j = "", m, n
    while i>0 and j>0:
        if X[i-1] == Y[j-1]:
            lcs += X[i-1]
            i-=1
            j-=1
        elif dp[i-1][j] > dp[i][j-1]:
            i-=1
        else:
            j-=1
    return lcs[::-1]
# print(lcs("WGRHTGF", "ERWQERGT"))

# 2. Max profit with k transactions (given prices of stock for some days, find max profit by doing k transactions)
from typing import List
# def maxProfit(prices: List[int], K: int) -> int:
#     d = len(prices)
#     dp = [[0]*(d+1) for i in range(K+1)]
#     for i in range(1, K+1):
#         maxDiff = -prices[0]
#         for j in range(1, d):
#             maxDiff = max(maxDiff, dp[i][j-1] - prices[j-1])
#             dp[i][j] = max(dp[i][j-1], prices[j]+maxDiff)
#     return dp[K][d-1]
def maxProfit(prices: List[int], k: int) -> int:
    if k >= len(prices)//2:
        profit = 0
        for i in range(1, len(prices)):
            profit += max(0, prices[i] - prices[i-1])
        return profit
    buy = [1001] * (k + 1)
    sell = [0] * (k + 1)
    for p in prices:
        for t in range(1, k + 1):
            buy[t] = min(buy[t], p - sell[t - 1])
            sell[t] = max(sell[t], p - buy[t])
    return sell[-1]
# print(maxProfit([2,5,7,1,4,3,1,3], 3))

# 3. Egg dropping puzzle
# given n eggs and k no of floors, check min no of trials need to find the critical floor in worst case
import sys
mx = 1001
dp = [[-1]*mx for i in range(mx)]
def eggDrop(n: int, k: int) -> int:
    if dp[n][k] != -1:
        return dp[n][k]
    if k==1 or k==0:
        return k
    if n==1:
        return k
    mn = sys.maxsize
    res = 0
    for i in range(1, k+1):
        res = max(eggDrop(n-1, i-1), eggDrop(n, k-i))
        if res < mn:
            mn = res
    dp[n][k] = mn+1
    return mn+1
# print(eggDrop(5, 500))

def eggDrop1(eggs: int, floors: int) -> int:
	E = [[0]*(eggs+1) for _  in range(floors+1)]
	for floor in range(1, floors+1):
		for egg in range(1, eggs+1):
			E[floor][egg] = E[floor-1][egg-1] + E[floor-1][egg] + 1
		if E[floor][eggs] >= floors:
			return floor
# print(eggDrop1(2, 36))

# egg droop optimised K eggs and N floors
def eggDrop2(eggs: int, floors: int) -> int:
    dp = [0, 0]
    m = 0
    while dp[-1] < floors:
        for i in range(len(dp) - 1, 0, - 1):
            dp[i] += dp[i - 1] + 1
        if len(dp) < eggs + 1:
            dp.append(dp[-1])
        m += 1
    return m
# print("trials", eggDrop2(2, 36)) #8


