import unittest
from collections import defaultdict

def identifyNonTwinPerson(inputArr: list[int]) -> int:

    # Create frequency list
    freq = defaultdict(int)
    for num in inputArr:
        freq[num] += 1

    # Find the "smallest" non-twin
    min_non_twin = float('inf')
    for num in inputArr:
        if freq[num] == 1:
            min_non_twin = min(min_non_twin, num)
        
    return min_non_twin if min_non_twin != float('inf') else -1
        
class TestFindMaximumDifference(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(identifyNonTwinPerson([1, 1, 2, 3, 3, 4, 4]), 2)
    
    def test_case_2(self):
        self.assertEqual(identifyNonTwinPerson([1, 1, 2, 2]), -1)

if __name__ == '__main__':
    unittest.main()