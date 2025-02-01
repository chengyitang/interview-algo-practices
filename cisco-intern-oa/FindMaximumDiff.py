import unittest

def findMaximumDifference(self, n: int, inputArray: list[int]) -> int:

    if n < 2: return 0
    
    max_diff = 0
    min_sofar = inputArray[0]

    for i in range(1, n):
        if inputArray[i] > min_sofar:
            max_diff = max(max_diff, inputArray[i] - min_sofar)
        min_sofar = min(min_sofar, inputArray[i])

    return max_diff

class TestFindMaximumDifference(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(findMaximumDifference(None, 7, [2, 3, 10, 6, 4, 8, 1]), 8)
    
    def test_case_2(self):
        self.assertEqual(findMaximumDifference(None, 3, [4, 3, 1]), 0)

if __name__ == '__main__':
    unittest.main()