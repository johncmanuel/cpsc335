from typing import List


def couples(arr: List[int]) -> int:
    swaps = 0
    personIndex = {person: i for i, person in enumerate(arr)}

    # iterate by pairs
    for i in range(0, len(arr), 2):
        first = arr[i]

        # If the first person is even, the second person is the index + 1
        # Else, the second person is the index - 1
        # Example: (3, 2) => if first person is 3, it is odd, so second person is 2.
        # Example: (0, 1) => if first person is 0, it is even, so second person is 1.
        second = first + 1 if first % 2 == 0 else first - 1

        if arr[i + 1] != second:
            # get index of the first person's partner and update the dictionary
            # with the partner's index
            partner = personIndex[second]
            personIndex[arr[i + 1]], personIndex[second] = partner, i + 1

            arr[i + 1], arr[partner] = arr[partner], arr[i + 1]
            swaps += 1

    return swaps


test_cases = [[[0, 2, 1, 3], 1], [[3, 2, 0, 1], 0], [[1, 0, 3, 2], 0]]

for i, test_case in enumerate(test_cases):
    result = couples(test_case[0])
    assert result == test_case[1]
print("Test cases succesfully ran!")
