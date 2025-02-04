class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # One-pass solution
        d = {} # N: idx

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in d:
                return [i, d[complement]]
            d[nums[i]] = i
        return []

# Easy. # Brute force takes N sq, use two-pass or one-pass w/hashmap
# Time = Space = O(N)