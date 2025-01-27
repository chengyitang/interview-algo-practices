class Solution:
    def maximizeMemoryPoints(self, memory: list[int]) -> int:
        
        memory.sort(reverse=True)

        for i in range(len(memory)):
            if i != 0:
                memory[i] += memory[i - 1]

        return sum(memory)
    
# Testing
solution = Solution()

# case 1
memory = [3, 4, 5]
output = 26
print(solution.maximizeMemoryPoints(memory) == output)

# case 2
memory = [1, 2, 3]
output = 14
print(solution.maximizeMemoryPoints(memory) == output)