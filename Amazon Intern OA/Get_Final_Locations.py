def getFinalLocations(locations: list[int], movedFrom: list[int], movedTo: list[int]) -> list[int]:

    current_location = set(locations)

    for i in range(len(movedFrom)):
        current_location.remove(movedFrom[i])
        current_location.add(movedTo[i])

    return sorted(list(current_location))

# Test
locations = [1, 7, 6, 8]
movedFrom = [1, 7, 2]
movedTo = [2, 9, 5]
output = [5, 6, 8, 9]

print(getFinalLocations(locations, movedFrom, movedTo) == output)
