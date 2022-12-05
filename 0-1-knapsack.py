
# 0-1 knapsack problem

from typing import List
def knapsack(P: List[int], W: List[int], M):
    N = len(P)
    K = [[0]*(M+1) for i in range(N+1)]
    for i in range(1,N+1): # prices length
        for j in range(1,M+1): # one by one bag capacity consideration
            # if the weight of i'th element is <= current bag capacity, then only compute formula
            if W[i-1] <= j:
                K[i][j] = max(K[i-1][j], K[i-1][j-W[i-1]] + P[i-1]) # j-W[i-1] means current bag capacity minus weight of previous item
            # otherwise just copy previous row item
            else:
                K[i][j] = K[i-1][j]
    print(K[N][M])
    i=N
    j=M
    while i>0 and j>0:
        if K[i][j] == K[i-1][j]:
            print(i, "= 0,", end=" ")
            i-=1
        else:
            print(i, "= 1,", end=" ")
            i-=1
            j-=W[i]

knapsack([1,2,5,6],[2,3,4,5],8)
# knapsack([60,100,120],[10,20,30],50)


