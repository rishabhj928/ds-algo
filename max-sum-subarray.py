from xml.dom.minidom import Element


# given an array, print max sum of unique elements

def maxSumSubarr(arr):
    i=0
    j=1
    set={}
    set[arr[0]]=1
    sum = arr[0]
    maxsum = sum
    while i<len(arr)-1 and j<len(arr):
        if arr[j] not in set:
            sum += arr[j]
            maxsum = max(maxsum, sum)
            set[arr[j]] = 1
            j += 1
        else:
            sum -= arr[i]
            del set[arr[i]]
            i += 1
    return [maxsum, i, j-1]


# sum of pair of nums in two arrays closest to x 
import sys
def closestPair(ar1, ar2, m, n, x):
    diff = sys.maxsize
    l = 0
    r = n-1
    while l<m and r>=0:
        if abs(ar1[l] + ar2[r] - x) < diff:
            rl = l
            rr = r
            diff = abs(ar1[l] + ar2[r] - x)
        if ar1[l] + ar2[r] > x:
            r -= 1
        else:
            l += 1
    print(ar1[rl], ar2[rr])

# sum of pair of array elements equal to x
# using hashmap h={}
def pair(arr, x):
    if 0 not in arr:
        arr.append(0)
    h = {}
    count = 0
    for i in range(len(arr)):
        tmp = x - arr[i]
        if tmp in h:
            print("index",h[tmp],i, end=" ")
            print("values",tmp,arr[i])
            count += 1
        h[arr[i]] = i
    print("count of pairs",count)
    print(h)

if __name__ == "__main__":
    # a = [2,1,4,2,5,7,4,2,3,4,7,9,1]
    # print(maxSumSubarr(a))
    # ar1 = [1, 4, 5, 7]
    # ar2 = [10, 20, 30, 40]
    # closestPair(ar1, ar2, len(ar1), len(ar2), 38)
    # pair([1, 4, 45, 6, 4, 5, 10, 8], 8)
    pair([4,4,4,4], 8)