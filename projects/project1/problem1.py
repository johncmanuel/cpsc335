def couples(arr):
    swaps = 0
    index = {person: i for i, person in enumerate(arr)}

    for i in range(0, len(arr), 2):
        first_person = arr[i]
        second_person = first_person ^ 1

        if arr[i + 1] != second_person:
            partner_index = index[second_person]

            index[arr[i + 1]] = partner_index
            index[second_person] = i + 1

            arr[i + 1], arr[partner_index] = arr[partner_index], arr[i + 1]
            swaps += 1

    return swaps


test_cases = [[[0, 2, 1, 3], 1], [[3, 2, 0, 1], 0], [[1, 0, 3, 2], 0]]

x = couples(test_cases[0][0])
y = couples(test_cases[2][0])
print(x, y)
