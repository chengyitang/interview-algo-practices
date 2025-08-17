"""
You are developing a feature for a linguistics research tool aimed at analyzing vowel patterns within words.
Linguists are particularly interested in the sequences of vowel ("a", "e", "i", "o", "u") within the text.

Given a string text consisting of lowercase English letters, count the number of substrings of length 3 that 
contain exactly two vowels (not necessarily distinct). 

Note: You are not expected to provide the most optimal solution, but a solution with time complexity not worse than O(text.length^2)
will fit within the execution time limit.

Example:
- For text = "aeiobe", the output should be solution(text) = 2.
- For text = "aeiou", the output should be solution(text) = 0.
"""


# Results: 
# Time complexity: O(n) - sliding window approach
# Space complexity: O(1): vowels set is constant space

def solution(text: str) -> int:
    """
    Count the number of substrings of length 3 that contain exactly two vowels.
    Uses sliding window approach for O(n) time complexity.
    """
    if len(text) < 3:
        return 0
    
    vowels = set("aeiou")
    count = 0
    
    # Count vowels in the first window of size 3
    vowel_count = 0
    for c in text[:3]:
        if c in vowels:
            vowel_count += 1
    
    # Check if first window has exactly 2 vowels
    if vowel_count == 2:
        count += 1
    
    # Slide the window and update vowel count
    for i in range(3, len(text)):
        # Remove the vowel count of the character leaving the window
        if text[i-3] in vowels:
            vowel_count -= 1
        
        # Add the vowel count of the character entering the window
        if text[i] in vowels:
            vowel_count += 1
        
        # Check if current window has exactly 2 vowels
        if vowel_count == 2:
            count += 1
    
    return count

def run_tests(): # Thanks LLM for the test cases!
    """Run comprehensive test cases for the solution function."""
    test_cases = [
        # Basic test cases
        ("aeiobe", 2, "Basic case with two valid substrings"),
        ("aeiou", 0, "All vowels - no substring has exactly 2 vowels"),
        ("ae", 0, "String too short"),
        ("aei", 0, "String of length 3 with 3 vowels"),
        ("atfeofri", 2, "Mixed consonants and vowels"),
        
        # Edge cases
        ("", 0, "Empty string"),
        ("a", 0, "Single character"),
        ("ab", 0, "Two characters"),
        ("abc", 0, "Three consonants"),
        ("aaa", 0, "Three vowels"),
        ("aab", 1, "Two vowels, one consonant"),
        ("aba", 1, "Vowel-consonant-vowel"),
        ("baa", 1, "Consonant-vowel-vowel"),
        
        # More complex cases
        ("aeio", 0, "Four vowels"),
        ("aeib", 1, "Three vowels, one consonant"),
        ("aeibc", 1, "Multiple valid substrings"),
        ("aeibcd", 1, "Valid substrings at beginning"),
        ("abcaei", 1, "Valid substring at end"),
        ("aeibcdaei", 2, "Multiple valid substrings"),
        
        # All consonants
        ("bcd", 0, "All consonants"),
        ("bcdef", 0, "All consonants longer string"),
        
        # Alternating pattern
        ("aeibc", 1, "Alternating vowels and consonants"),
    ]
    
    passed = 0
    total = len(test_cases)
    
    for i, (input_str, expected, description) in enumerate(test_cases, 1):
        try:
            result = solution(input_str)
            if result == expected:
                passed += 1
                print(f"✓ Test {i}: PASSED - {description}")
                print(f"  Input: '{input_str}' -> Expected: {expected}, Got: {result}")
            else:
                print(f"✗ Test {i}: FAILED - {description}")
                print(f"  Input: '{input_str}' -> Expected: {expected}, Got: {result}")
        except Exception as e:
            print(f"✗ Test {i}: ERROR - {description}")
            print(f"  Input: '{input_str}' -> Error: {e}")
    
    print(f"\nTest Results: {passed}/{total} tests passed")
    if passed == total:
        print("🎉 All test cases passed!")
    else:
        print("❌ Some test cases failed!")

if __name__ == "__main__":
    run_tests()

