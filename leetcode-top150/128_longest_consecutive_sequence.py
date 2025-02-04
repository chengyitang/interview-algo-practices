class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        nums.sort()

        longest = 1
        current = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                if nums[i] == nums[i - 1] + 1:
                    current += 1
                else:
                    longest = max(longest, current)
                    current = 1
        return max(longest, current)
        
# Medium (with sort)
# Time: O(NlogN)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        longest = 0
        nums_set = set(nums)

        for num in nums_set:
            if num - 1 not in nums_set:
                current_num = num # update new sequence head
                current_len = 1

                while current_num + 1 in nums_set:
                    current_num += 1
                    current_len += 1

                longest = max(longest, current_len)

        return longest
    
# Without sort -> use set. 
# No need to check if consecutive number if adjacent to each other, just have to confirm they exist!
# Time: O(N)
# Space: O(N)