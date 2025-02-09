def min_transitions(tiktokStorage):
    
    count_0 = tiktokStorage.count(0)
    count_1 = len(tiktokStorage) - count_0

    swap_required_0 = 0
    for i in range(count_0):
        if tiktokStorage[i] == 1:
            swap_required_0 += 1
    
    swap_required_1 = 0
    for i in range(count_1):
        if tiktokStorage[i] == 0:
            swap_required_1 += 1

    return min(swap_required_1, swap_required_0)

def test_min_transitions():
    # Test case 1: All 0s
    assert min_transitions([0, 0, 0, 0, 0]) == 0

    # Test case 2: All 1s
    assert min_transitions([1, 1, 1, 1, 1]) == 0

    # Test case 3: Equal number of 0s and 1s
    assert min_transitions([0, 1, 0, 1, 0, 1]) == 1
    assert min_transitions([1, 0, 1, 0, 1]) == 1

    # Test case 4: Alternating 0s and 1s
    assert min_transitions([0, 1, 0, 1, 0, 1, 0, 1]) == 2
    assert min_transitions([1, 0, 1, 0, 1, 0, 1, 0]) == 2

    # Test case 5: All 1s at the end
    assert min_transitions([0, 0, 0, 0, 1, 1, 1, 1]) == 0

    # Test case 6: All 1s at the beginning
    assert min_transitions([1, 1, 1, 1, 0, 0, 0, 0]) == 0

    print("All test cases passed!")

# Run the test function
test_min_transitions()