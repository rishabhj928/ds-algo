
# consider we have some stairs of length n, we can only move either 1 step up, or 2 steps up
# in how many distinct ways we can climb it?
# e.g.
# n = 2
# ans = 2
# explanation: there are 2 ways to climb up 2 stairs: 1 step + 1 step and 2 steps
# n=3
# ans=3
# exp: there are 3 ways to climb 3 stairs: 1+1+1, 1+2, 2+1

# dynamic programming: it can be either solved by top down approach (where we have to build a tree - n space complexity)
# or it can be solved by bottom up approach

# if we have 0 stair, we have 1 chance to do nothing
# if we have 1 stair, we can only climb by 1 chance

# old fashion recursion which takes a lot of extra work and already calculated values are calculated again for other recursions
def cs(n):
    if n==0 or n==1:
        return 1
    return cs(n-1)+cs(n-2)

# bottom up approach (dp)
def climbingStairsbu1(n): # O(n) time & O(n) space
    a = [0]*(n+1)
    a[1]=1
    for i in range(2,n+1):
        a[i]=a[i-1]+a[i-2]
    return a[n]+a[n-1]

# further it can be reduced by using just 2 variables, so not to use any array,
# because the next iteration would only depend on previous two
# dp
def climbingStairsbu2(n): # O(n) time and O(1) space
    i=0
    j=1
    while n>0:
        t=j
        j+=i
        i=t
        n-=1
    return j

# Top down approach (use dfs and use current results to reduce extra recursion)
def climbingStairstd(n): # O(2^n) time and O(n) space

    pass

print(cs(6))



# i j
# 1 1
# 1 2
# 2 3
# 3 5
# 5 8
# 8 13


