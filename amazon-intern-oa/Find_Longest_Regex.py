class Solution:
    def findLongestRegex(self, x: str, y: str, z: str) -> str:
        
        if x == z or y == z:
            return "-1"
        
        n = len(x)

        invalid_pos = -1
        for i in range(n - 1, -1, -1):
            if (z[i] != x[i] or z[i] != y[i]) and (x[i] == y[i] or z[i] not in {x[i], y[i]}):
                invalid_pos = i
                break
        
        if invalid_pos == -1:
            return "-1"
        
        results = []
        for i in range(n):
            if i == invalid_pos:
                char_set = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
                char_set.discard(z[i])
            else:
                char_set = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

            regex = '[' + ''.join(sorted(char_set)) + ']'
            results.append(regex)

        return ''.join(results)
        

solution = Solution()
    
# Test cases
def test_regex_generator():
    # Test case 1
    x1, y1, z1 = "AB", "BD", "CD"
    print(f"Test 1: {solution.findLongestRegex(x1, y1, z1)}")
    
    # Test case 2
    x2, y2, z2 = "AERB", "ATRC", "AGCB"
    print(f"Test 2: {solution.findLongestRegex(x2, y2, z2)}")
    
    # Test case 3
    x3, y3, z3 = "ABCD", "CODE", "CODE"
    print(f"Test 3: {solution.findLongestRegex(x3, y3, z3)}")

# Run tests
if __name__ == "__main__":
    test_regex_generator()