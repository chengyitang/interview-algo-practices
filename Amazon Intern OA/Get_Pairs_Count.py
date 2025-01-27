
def getPairsCount(process: list[int], k: int) -> int:
    # sort first
    process.sort()
    pairs_n = 0
    l = 0
    for r in range(1, len(process)):
        # move left pointer while the difference is more than k
        while l < r and process[r] - process[l] > k:
            l += 1
        # All element from left to right-1 form valid pairs with process[r]
        if l < r:
            for i in range(l, r):
                print(f"({process[i]}, {process[r]})")
            pairs_n += r - l
    return pairs_n
    
process = [100, 200, 300, 400]
k = 250
getPairsCount(process, k)
