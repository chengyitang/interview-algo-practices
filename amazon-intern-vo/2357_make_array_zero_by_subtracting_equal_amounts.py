class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        # To-Do: check null
        if not nums:
            return 0

        # Thought: answer = the number of unique non-zero numbers in the list
        return len(set(nums) - {0})

# Easy. 
# Array, Hashset.
# Time: O(n)
# Space: O(n)