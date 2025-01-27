from collections import defaultdict

def getStablePeriodsCount(revenues: list[int], k: int) -> int:
    
    MOD = 10**9 + 7

    count = 0
    window = {}

    l = 0
    for r in range(len(revenues)):

        window[revenues[r]] = window.get(revenues[r], 0) + 1

        while len(window) > k:
            window[revenues[l]] -= 1
            if window[revenues[l]] == 0:
                del window[revenues[l]]
            l += 1

        count += (r - l + 1)
        count %= MOD

    return count

revenues = [1, 2, 1]
k = 1
output = 3
print(getStablePeriodsCount(revenues, k) == output)

revenues = [2, -3, 2, -3]
k = 2
output = 10
print(getStablePeriodsCount(revenues, k) == 10)