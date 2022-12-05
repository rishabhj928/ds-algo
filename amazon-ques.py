
# def findPasswordStrength(password):
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     pairs = 0
#     vowelFound = False
#     consonantFound = False
#     for pas in password:
#         if pas in vowels:
#             vowelFound = True
#         else:
#             consonantFound = True
#         if consonantFound and vowelFound:
#             pairs += 1
#             consonantFound = False
#             vowelFound = False
#     return pairs
# print(findPasswordStrength("hackerrank")) #3
# print(findPasswordStrength("thisisbeautiful")) #6
# print(findPasswordStrength("rhythm")) #0

from heapq import *
def bestCombo(popularity, k):
    positives = 0
    answer = []
    n = len(popularity)
    for pop in popularity:
        if pop > 0:
            positives += pop
    answer.append(positives)
    for i in range(n):
        popularity[i] = abs(popularity[i])
    popularity.sort()
    maxheap = []
    heappush(maxheap, (popularity[0], 0))
    while maxheap and len(answer) < k:
        curmaxPopularity, i = heappop(maxheap)
        answer.append(positives - curmaxPopularity)
        if i+1 < n:
            heappush(maxheap, (curmaxPopularity - popularity[i] + popularity[i+1], i+1))
            heappush(maxheap, (curmaxPopularity + popularity[i+1], i+1))
    return answer
print(bestCombo([3, 5, -2], 3))
print(bestCombo([1, 2, 3, 1000], 4))
print(bestCombo([0, 0, 0, 0, 0], 3))
