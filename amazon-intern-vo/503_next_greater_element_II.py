class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        n = len(nums)
        stack = [] # save numbers
        ans = [-1] * n

        for i in range(n * 2 - 1, -1, -1):
            while stack and stack[-1] <= nums[i % n]: # current is greater than stack top
                stack.pop()
            if i < n: # check index
                ans[i] = -1 if not stack else stack[-1] # 
            stack.append(nums[i % n]) # append current number

        return ans
            
        
# Medium    
# Monotonic Stack
# Time: O(n)
# Space: O(n)

# Approach 🛠️🔧
# Double Trouble? Nope!: We’ll loop through the array twice using modulo magic 🧙‍♂️ to simulate circular behavior without actually duplicating the array. Cool, right? 😎✨
# Stack Up Your Odds: A stack helps keep track of elements that are still waiting for their bigger buddy! 📚🔝
# Reverse Engineer: By iterating from back to front (twice!), we catch all the big guys waiting to shine for the little ones ahead! 🚀🌟