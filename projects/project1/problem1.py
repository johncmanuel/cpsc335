from typing import List


def couples(c: List[int]) -> int:
    swaps = 0
    personIndex = {person: i for i, person in enumerate(c)}

    # iterate by pairs
    for i in range(0, len(c), 2):
        # If the first person is even, the second person is the index + 1
        # Else, the second person is the index - 1
        # Example: (3, 2) => if first person is 3, it is odd, so second person is 2.
        # Example: (0, 1) => if first person is 0, it is even, so second person is 1.
        secondPerson = c[i] + 1 if c[i] % 2 == 0 else c[i] - 1

        if c[i + 1] != secondPerson:
            # get index of the first person's partner and update the dictionary
            # with the partner's index
            partner = personIndex[secondPerson]
            personIndex[c[i + 1]], personIndex[secondPerson] = partner, i + 1

            c[i + 1], c[partner] = c[partner], c[i + 1]
            swaps += 1

    return swaps


def main():
    testCases = [[[0, 2, 1, 3], 1], [[3, 2, 0, 1], 0], [[1, 0, 3, 2], 0]]
    for case in testCases:
        result = couples(case[0])
        print("test case passed:", result == case[1])


main()
