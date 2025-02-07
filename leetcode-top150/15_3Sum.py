class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        output = []
        
        nums.sort() # n log n

        for i in range(len(nums) - 2): # n
            
            # skip duplicate numbers
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            two_sum = 0 - nums[i] # remaining two nums

            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == two_sum:
                    output.append([nums[i], nums[l], nums[r]])

                    # skip duplicate numbers
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                elif nums[l] + nums[r] > two_sum:
                    r -= 1
                else:
                    l += 1

        return output
    
# Medium. 
# Two pointers. Sort first, then we can do TwoSum II with two pointers inside the first for loop.
# Time: O(N sq). two sum part is O(N) and we call it N times. 
# Space: O(NlogN) ~ O(N) based on sorting algo

