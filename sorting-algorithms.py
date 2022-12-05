
# Divide and Conquer sorting algorithms

# 1. Merge Sort O(nlogn)

def msMerge(B, C, A):
    i = j = k = 0
    p = len(B)
    q = len(C)
    while i<p and j<q:
        if B[i] < C[j]:
            A[k] = B[i]
            i+=1
        else:
            A[k] = C[j]
            j+=1
        k+=1
    for i in range(i,p):
        A[k] = B[i]
        k+=1
    for j in range(j,q):
        A[k] = C[j]
        k+=1

def mergeSort(A):
    n=len(A)
    if n>1:
        B = A[:n//2]
        C = A[n//2:]
        mergeSort(B)
        mergeSort(C)
        msMerge(B, C, A)


# 2. Quick Sort Q(nlogn) to O(n2)

def qsPartition(l,h,A):
    pi = l
    p = A[pi]
    while l<h:
        while l < len(A) and A[l] <= p:
            l+=1
        while A[h] > p:
            h-=1
        if l<h:
            A[l],A[h] = A[h],A[l]
    A[h],A[pi] = A[pi],A[h]    
    return h

def quickSort(l,h,A):
    if l<h:
        k = qsPartition(l,h,A)
        quickSort(l,k-1,A)
        quickSort(k+1,h,A)


# Brute Force Algo

# 1. Bubble Sort O(n2)
def bubbleSort(A):
    n = len(A)
    for i in range(n):
        for j in range(n):
            if A[i] > A[j]:
                A[i],A[j] = A[j],A[i]

# 2. Selection Sort O(n2)
def selectionSort(A):
    n = len(A)
    for i in range(n):
        m = i
        for j in range(i+1,n):
            if A[m] > A[j]:
                m = j
        A[i],A[m] = A[m],A[i]

# 3. Insertion Sort O(n2)
def insertionSort(A):
    n = len(A)
    for i in range(1,n):
        temp = A[i]
        j=i
        while j>0 and temp<A[j-1]:
            A[j] = A[j-1]
            j-=1
        A[j] = temp


if __name__=="__main__":
    arr = [32,14,3,15,27,16,29,80]
    # mergeSort(arr)
    # quickSort(0, len(arr)-1,arr)
    # bubbleSort(arr)
    # selectionSort(arr)
    # insertionSort(arr)
    print(arr)