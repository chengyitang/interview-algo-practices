"""
We have several processes to run. Each process places a load (given as an integer) on the server it runs on. The total load of a server is the sum of loads of all processes assigned to it.

You have two servers available. Assign all processes to the two servers such that the absolute difference between their total loads is minimized.

Write a function that, given an integer array A (length N) where each element represents a process load, returns the minimal absolute difference between the two servers’ total loads.

"""

def solution(A):

    """
    Thoughts:
    ideal situation: S1 = S2 = TotalSum/2
    but in reality, we need to find the closest sum to TotalSum/2,
    we can use a greedy approach to find the closest sum to TotalSum/2.

    If S1 = subsetSum, 
    then S2 = TotalSum - subsetSum,
    then the difference = |S1 - S2| = |TotalSum - 2 * subsetSum|
    we need to find the subsetSum that makes the difference as small as possible.
    """

    total_sum = sum(A)
    target = total_sum // 2

    # dp[i] represents whether subsetSum i can be achieved
    # length of dp is target + 1 since we just need to find subsetSum closest to target
    dp = [False] * (target + 1)
    dp[0] = True

    for load in A:

        for i in range(target, load - 1, -1): # why load -1
            if dp[i - load]:
                dp[i] = True

    # search dp backward start from target, the find the first True
    for i in range(target, -1, -1):
        if dp[i]:
            best_subset_sum = i
            break
    return total_sum - 2 * best_subset_sum

    # Time: O(N * target)
    # Space: O(target)

print(solution([1, 2, 3, 4, 5])) # 1
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # 1
print(solution([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) # 1
print(solution([1, 3, 2, 4, 5])) # 1
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # 1
print(solution([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) # 1
print(solution([5, 2, 4, 3, 1, 6])) # 1
print(solution([5, 5, 5])) # 5

