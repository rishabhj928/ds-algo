

# Amazon Prime Games is designing a game. The player needs to pass n rounds sequentially in this game. Rules of play are as follows:
# - The player loses power[i] health to complete round i.
# - The player's health must be greater than 0 at all times.
# - The player can choose to use armor in any one round. The armor will prevent damage of min(armor, power[i]).
# Determine the minimum starting health for a player to win the game.
# Example:
# power = [1, 2, 6, 7]
# armor = 5
# ans = 12

def findMinHealth(power, armor):
    n = len(power)
    ans = 0
    arm = True
    for i in range(n):
        if power[i] > armor and arm == True:
            ans += power[i] - armor
            arm = False
        else:
            ans += power[i]
    if arm == True:
        temp = max(power)
        ans -= temp
        arm = False
    return ans + 1

def findMinHealth2(power, armor):
    total = sum(power)
    maxPower = max(power)
    return total + 1 - min(armor, maxPower)


print(findMinHealth2([1,2,6,7], 5))
print(findMinHealth2([1,2,6,7], 8))

