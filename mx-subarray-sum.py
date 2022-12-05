
# given an array, find it's unique elements and at those index in other array find max sum

def findMaxSumSubarray(X, Y, N):
    m = [-1] * 1001
    low = high = curSum = maxSum = 0
    while high<=N:
        if high==N:
            curSum=0
            for i in range(low,high):
                curSum += Y[i]
            maxSum = max(maxSum, curSum)
            break
        if m[X[high]] != -1 and m[X[high]] >= low:
            curSum=0
            for i in range(low,high):
                curSum += Y[i]
            maxSum = max(maxSum, curSum)
            low = m[X[high]] + 1
        m[X[high]] = high
        high += 1
    return maxSum

if __name__ == "__main__":
    X = [0,1,2,0,2]
    Y = [5,6,7,8,2]
    N = len(X)
    print(findMaxSumSubarray(X,Y,N))