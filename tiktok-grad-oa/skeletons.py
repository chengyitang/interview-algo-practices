"""
Skeleton Matching Problem

DESCRIPTION:
You are given a string `word` consisting of lowercase English letters, and a list of strings 
`skeletons` consisting of '-' characters and lowercase English letters. Every `skeleton` will 
always be the same length as `word`.

TASK:
Your task is to return a list of skeletons that can form the given `word`. A skeleton can form 
a word if all '-' characters can be replaced with other characters taken from the same skeleton 
to make the string equal to the `word`. If no strings within `skeletons` can form the given 
`word` by doing this, return an empty list. The matching skeletons should be returned in the 
same order they appear in `skeletons` and the list of skeletons may not all be unique.

CONSTRAINTS:
- You are not expected to provide the most optimal solution
- A solution with time complexity not worse than O(skeletons.length x word.length^2) will fit 
  within the execution time limit

EXAMPLE:
For `word` = "hello" and `skeletons` = ["he-lo", "he--o", "-ell-", "hello"], 
the output should be `solution(word, skeletons)` = ["he-lo", "hello"]

EXPLANATION:

"he-lo" IS a skeleton of "hello":
- There is one '-' character, which should be an 'l'
- There is an 'l' in the skeleton in the fourth position
- The hyphen at index 2 in "he-lo" needs to be replaced by 'l' to form "hello". 
  The 'l' character is present in "he-lo" at index 3

"he--o" is NOT a skeleton of "hello":
- There are two '-' characters, which should both be 'l'
- But there are no 'l' characters in the skeleton
- The hyphens at indices 2 and 3 in "he--o" both need to be replaced by 'l' to form "hello". 
  However, the skeleton "he--o" does not contain the character 'l'

"-ell-" is NOT a skeleton of "hello":
- There are two '-' characters, which should both be 'h' and 'o' respectively
- But there are no 'h' and 'o' characters in the skeleton
- The hyphen at index 0 needs to be 'h' and the hyphen at index 4 needs to be 'o' to form "hello". 
  The skeleton "-ell-" does not contain 'h' or 'o'

ALGORITHM APPROACH:
1. For each skeleton in the list:
   - Check if it can form the target word
   - For each '-' in the skeleton, verify that the required character exists elsewhere in the skeleton
   - If all hyphens can be filled with characters from the same skeleton, include it in the result
2. Return the list of valid skeletons in their original order
"""

def is_valid_skeleton(word: str, skeleton: str) -> bool:
    """
    Time: O(m) where m = len(skeleton)
    Space: O(m) for available_chars list
    """
    if len(skeleton) != len(word):
        return False
    
    # Count available characters (excluding hyphens)
    available_chars = [c for c in skeleton if c != '-']

    for i, c in enumerate(skeleton):
        if c == '-':
            if word[i] not in available_chars:
                return False
        elif c != word[i]: # not a hyphen and not the same character
            return False
        
    return True

def solution(word: str, skeletons: list[str]) -> list[str]:
    """
    Time: O(n × m) where n = number of skeletons, m = length of word
    Space: O(n) for return list
    """
    return [skeleton for skeleton in skeletons if is_valid_skeleton(word, skeleton)]

def run_tests():
    
    test_cases = [
        ("hello", ["he-lo", "he--o", "-ell-", "hello"], ["he-lo", "hello"]),
        ("hello", ["he-lo", "he--o", "-ell-", "hell-"], ["he-lo"])
    ]

    for i, (word, skeletons, expected) in enumerate(test_cases):
        result = solution(word, skeletons)
        if result == expected:
            print(f"Test {i} passed")
        else:
            print(f"Test {i} failed: expected {expected}, got {result}")
            print(f"  Analysis:")
            for skeleton in skeletons:
                chars = [c for c in skeleton if c != '-']
                needed = [word[j] for j, c in enumerate(skeleton) if c == '-']
                print(f"    '{skeleton}': chars={chars}, needed={needed}, valid={is_valid_skeleton(word, skeleton)}")


if __name__ == "__main__":
    run_tests()