
import statistics
from itertools import combinations
def solve(arr):
    arr.sort()
    combos = combinations(arr, 3)
    res = (10**9)+1
    for a,b,c in combos:
        mean = (a+b+c)/3
        res = min(res, round(3*abs(b - mean)))
    return res
tc = [[1,4,5,8,9], [17,89,84,95,92], [53,40,46,89,51], [25,3,93,76,38], [80,59,29,97,30]]
# for t in tc:
    # print(solve(t))

# ----------------------------------------------------

from collections import Counter
def solve2(S, queries):
    ans = []
    abc = 'abcdefghijklmnopqrstuvwxyz'
    S = list(S)
    for i, x, y in queries:
        if i == 2:
            S[x-1] = abc[y-1]
        if i == 1:
            z = Counter(S[x-1:y]).values()
            xor = 0
            for k in z:
                xor = xor ^ k
            ans.append(xor)
    return ans
print(solve2('jnxsrfqnirzdgpaaotos', [[2,2,10],[2,19,22],[1,10,14],[2,16,9],[1,7,17],[1,9,14],[1,1,11]]))
