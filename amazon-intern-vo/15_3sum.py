class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # check null
        if not nums:
            return []
        
        output = []
        
        # sort first so we can use two pointers for the two sum later
        nums.sort()

        for i in range(len(nums)):

            # skip duplicate nums[i] for must not contain duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # two pointers for the two sum
            two_sum = 0 - nums[i]

            l, r = i + 1, len(nums) - 1

            while l < r:
                if nums[l] + nums[r] == two_sum:
                    output.append([nums[i], nums[l], nums[r]])
                
                    # skip duplicates nums[l] and nums[r]
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1

                elif nums[l] + nums[r] < two_sum:
                    l += 1
                else:
                    r -= 1  

        return output
    
# Medium
# Array, Two Pointers, Sorting
# Time: O(n^2)
# Space: O(1) - ignore output space
