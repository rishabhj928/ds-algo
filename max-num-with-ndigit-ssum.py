
# Given a target sum s, find maximum number having n digits without trailing zeros
# e.g. 2 digits and 15 sum, ans = 96 [another option could be 87 but it is less than 96]

def findLargest(n, s):
	if s == 0:
		if n == 1:
			return 0
		else:
			return -1
	if s > 9 * n:
		return -1
	
	ans = 0
	for i in range(n):
		ans *= 10
		if s >= 9:
			ans += 9
			s -= 9
		else:
			ans += s
			s = 0
	return ans

print(findLargest(2, 9))
print(findLargest(2, 15))
print(findLargest(3, 25))
