# we locking in!


def algo1(arr):
    swaps = 0
    # Map to store the current index of each person
    index = {person: i for i, person in enumerate(arr)}

    for i in range(0, len(arr), 2):  # Step through the array in pairs (0, 2, 4, ...)
        first_person = arr[i]
        second_person = (
            first_person ^ 1
        )  # Partner of first_person (0 -> 1, 1 -> 0, etc.)

        if arr[i + 1] != second_person:  # If not sitting with partner
            # Swap the current second person with the partner
            partner_index = index[second_person]

            # Update the index mapping before swapping
            index[arr[i + 1]] = partner_index
            index[second_person] = i + 1

            # Perform the swap
            arr[i + 1], arr[partner_index] = arr[partner_index], arr[i + 1]
            swaps += 1

    return swaps


test_cases = [[[0, 2, 1, 3], 1], [[3, 2, 0, 1], 0], [[1, 0, 3, 2], 0]]

x = algo1(test_cases[0][0])
y = algo1(test_cases[2][0])
print(x, y)
