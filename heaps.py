
# max heap
def heapify(arr, n, i):
    mx = i
    l = 2*i+1
    r = 2*i+2
    if l < n and arr[mx] < arr[l]:
        mx = l
    if r < n and arr[mx] < arr[r]:
        mx = r
    if mx!=i:
        arr[i], arr[mx] = arr[mx], arr[i]
        heapify(arr, n, mx)

def heapsort(arr):
    n = len(arr)
    for i in range(n//2-1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

if __name__=="__main__":
    arr = [9,2,7,3,0,1,6,8,4,5]
    heapsort(arr)
    print(arr)

