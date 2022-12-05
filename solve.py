
def solve(K, A):
    # print(set(A))
    c = 0
    kk = {}
    x = max(A)
    i=0
    while x >= 0:
        if i not in A:
            c += 1
            kk[c] = i
        else:
            x += 1
        if c == K:
            break
        x -= 1
        i += 1
    # print(kk)
    return kk[c]

print(solve(9, [14, 13, 17, 7, 13, 5, 16, 18, 10, 17, 8, 0, 0, 17, 1, 3, 7, 16, 11, 14])) #21
print(solve(3, [5, 13, 1, 19, 5, 0, 3, 12, 17, 9])) #6
print(solve(3, [7,5,7,1])) #3
print(solve(1, [2])) #0
