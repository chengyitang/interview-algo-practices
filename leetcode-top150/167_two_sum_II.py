class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l, r = 0, len(numbers) - 1

        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1

# Medium. 
# Two pointers: 已經是 sorted 所以才能用 two pointers 去找，TwoSum I 沒有 sorted
# Time: O(N)
# Space: O(1)