import unittest

def identifyNonTwinPerson(inputArr: list[int]) -> int:

    freq = {}

    for num in inputArr:
        freq[num] = freq.get(num, 0) + 1

    for num in inputArr:
        if freq[num] == 1:
            return num  
        
    return -1
        
class TestFindMaximumDifference(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(identifyNonTwinPerson([1, 1, 2, 3, 3, 4, 4]), 2)
    
    def test_case_2(self):
        self.assertEqual(identifyNonTwinPerson([1, 1, 2, 2]), -1)

if __name__ == '__main__':
    unittest.main()