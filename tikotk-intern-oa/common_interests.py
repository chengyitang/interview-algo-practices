import collections, math

def maxSharedCategories(favoriteCategories):

    if len(favoriteCategories) < 2: return 
    
    gcd_count = collections.defaultdict(int)

    for n in favoriteCategories:
        for i in range(1, int(math.sqrt(n)) + 1):
            if n % i == 0:
                gcd_count[i] += 1
                if i != n // i:
                    gcd_count[n // i] += 1
    
    # print(favoriteCategories)
    # print(gcd_count)

    max_gcd = 0
    for key, value in gcd_count.items():
        if value >= 2 and key > max_gcd:
            max_gcd = key

    return max_gcd

def test_max_shared_categories():
    # Test case 1: All unique categories
    assert maxSharedCategories([1, 2, 3, 4]) == 2

    # Test case 2: All common categories
    assert maxSharedCategories([4, 4, 4, 4]) == 4

    # Test case 3: Mixed categories
    assert maxSharedCategories([4, 2, 6, 8]) == 4

    # Test case 4: Empty input
    assert maxSharedCategories([]) == None

    # Test case 5: Single user
    assert maxSharedCategories([5]) == None

    print("All test cases passed!")

# Run the test function
test_max_shared_categories()