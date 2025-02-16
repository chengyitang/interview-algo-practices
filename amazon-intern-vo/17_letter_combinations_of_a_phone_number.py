class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        keyboard = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtrack(index, curStr):
            if len(curStr) == len(digits):
                possible_combinations.append(curStr)
                return

            charOptions = keyboard[digits[index]]
            for c in charOptions:
                backtrack(index + 1, curStr + c)

        possible_combinations = []

        backtrack(0, "")
        return possible_combinations
    
# Backtracking
# Time: O(n * 4^n)
# Space: O(n)