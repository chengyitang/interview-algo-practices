"""A company's IT department is faced with a dilemma that users keep using simple passwords such as "password", "abc123" etc.

You are tasked with a challenge to write an algorithm to identify the total minimum number of changes (insertions and deletions) of characters to convert these simple passwords to their more difficult versions.

Input

The first line of input consists of a string-currPassword, representing the current password. The second line consists of a string-newPassword, representing the new password.

Output

Print an integer representing the minimum number of updates required (character insertions and deletions) to convert the current password into the new password."""
from collections import defaultdict

def minUpdates(currPassword: str, newPassword: str) -> int:
    # Damn this one is hard
    pass


def run_tests():
    # Test case 1: Original example
    assert minUpdates("password", "pss$w#rd") == 4, "Test case 1 failed"
    
    # Test case 2: Different lengths
    assert minUpdates("abc123", "abcd1234") == 2, "Test case 2 failed"
    
    # Test case 3: Complete different strings
    assert minUpdates("easy", "hard") == 6, "Test case 3 failed"
    
    # Test case 4: Same strings
    assert minUpdates("secure", "secure") == 0, "Test case 4 failed"
    
    # Test case 5: Empty string to non-empty
    assert minUpdates("", "password") == 8, "Test case 5 failed"
    
    # Test case 6: Non-empty to empty
    assert minUpdates("password", "") == 8, "Test case 6 failed"
    
    # Test case 7: Both empty strings
    assert minUpdates("", "") == 0, "Test case 7 failed"
    
    print("All test cases passed!")

if __name__ == "__main__":
    run_tests()