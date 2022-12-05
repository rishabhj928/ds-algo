

def getsum(fenwick,i):
	s = 0
	i += 1
	while i > 0:
		s += fenwick[i]
		i -= i & (-i)
	return s

def updatebit(fenwick , n , i ,v):
	i += 1
	while i <= n:
		fenwick[i] += v
		i += i & (-i)

def construct(arr, n):
	fenwick = [0]*(n+1)
	for i in range(n):
		updatebit(fenwick, n, i, arr[i])
	# for i in range(1,n+1):
	# 	print fenwick[i],
	return fenwick

freq = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
fenwick = construct(freq,len(freq))
print("Sum of elements in arr[0..5] is " + str(getsum(fenwick,5)))
freq[3] += 6
updatebit(fenwick, len(freq), 3, 6)
print("Sum of elements in arr[0..5] after update is " + str(getsum(fenwick,5)))
