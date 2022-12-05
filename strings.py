
# string permutation
def permute(a,l,r):
    if l==r:
        print(''.join(a))
    else:
        for i in range(l,r+1):
            a[l],a[i]=a[i],a[l]
            permute(a,l+1,r)
            a[l],a[i]=a[i],a[l]  # backtrack

def removeAdjDuplicates(s):
    arr=[]
    for i in range(len(s)):
        if(len(arr)==0):
            arr.append(s[i])
        else:
            if(arr[-1]==s[i]):
                arr.pop(-1)
            else:
                arr.append(s[i])
            #print(arr,s[i])
    s="".join(arr)
    if(len(s)==0):
        print('Empty String')
    else:
        print(s)

def check(s1: str, s2: str) -> bool:
    for i in range(len(s1)):
        if s1[i] in s2:
            s2 = s2.replace(s1[i],'',1)
    if len(s2)==0:
        return True
    return False



# s = "ABC"
# permute(list(s), 0, len(s)-1)
# removeAdjDuplicates("abbabcbabcbbabccbabc")

print(check('tight', 'night'))
