class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        mp = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in mp:
                return [mp[complement], i]
            mp[nums[i]] = i

        return []