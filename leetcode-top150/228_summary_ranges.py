class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        if not nums:
            return []
        
        output = []
        start = nums[0]
        prev = start

        for i in range(1, len(nums)):
            if nums[i] != prev + 1:
                # add condition for edge case: nums[0] is an interval itself
                if start == prev:
                    output.append(str(start))
                else:
                    output.append(f"{start}->{prev}")
                # new start
                start = nums[i]
            prev = nums[i]

        # for last interval
        if start == prev:
            output.append(str(start))
        else:
            output.append(f"{start}->{prev}")

        return output

# Easy, frequent OA problem
# Time: O(N)
# Space: O(N)