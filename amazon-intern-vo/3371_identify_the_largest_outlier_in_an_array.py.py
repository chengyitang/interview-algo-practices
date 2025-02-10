# Medium. Array, Hashmap.
# Time: O(n)
# Space: O(n)   

class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
    
        total_sum = sum(nums)  
        num_counts = Counter(nums)
        largest_outlier = float('-inf')
 
        for num in nums:
            # assume num is the sum of all other special numbers    
            potential_outlier = total_sum - 2 * num # equation: total_sum = outlier + 2 * num
 
            if potential_outlier in num_counts:
                # for outlier there are two cases:
                # 1. outlier != num ex. [1, 2, 3, 6, 8]
                # 2. outlier == num and counter[num] > 1 ex. [1, 2, 3, 6, 6]
                if potential_outlier != num or num_counts[num] > 1: 
                    largest_outlier = max(largest_outlier, potential_outlier)
    
        return largest_outlier