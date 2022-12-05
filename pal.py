
def ispPal(s: str) -> bool:
    l = 0
    h = len(s) - 1
    while l <= h:
        if s[l] != s[h]:
            return False
        l += 1
        h -= 1
    return True

print(ispPal('nitim'))
