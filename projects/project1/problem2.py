# John Carlo Manuel, Timothy Tran
# johncarlomanuel@csu.fullerton.edu, timmyster413@csu.fullerton.edu
# CPSC 335
# Instructor Balaji Sai Charan Jalukuru
# 29 September 2024


def greedy_approach(city_distances, fuel, mpg):

    # Starting values for iterating through the arrays.
    starting_city = 0
    total_gas = 0

    # Walk through each value in array to determine which city is best to start at.
    for i in range(len(city_distances)):

        # Merge the fuel array with mpg to determine how far a car is able to go after each stop
        # We are left with two arrays which can be compared with each other
        # the variable total_gas is created to compare the two arrays and check to see if
        # gas_efficiency > city_distances at ALL times.
        gas_efficiency = fuel[i] * mpg
        total_gas += gas_efficiency - city_distances[i]

        # If however gas_efficiency < city_distances, we can assume that the car did NOT make it
        # Therefore, we iterate to the next city_distances[index] and start over.
        if total_gas < 0:
            starting_city = i + 1
            total_gas = 0

    # When the whole iteration is able to successfully pass through all elements in array
    # If our returned total_gas that is used is at least 0, then we can conclude
    # That the starting_city index is our valid city to start at.
    if total_gas >= 0:
        return starting_city

    # This will usually never be the case, since it is confirmed within the problem that
    # there will be guaranteed exactly one city that is valid to start at.
    else:
        return -1


def Hamilton_Problem():

    # Using the values given from the problem
    city_distances = [5, 25, 15, 10, 15]
    fuel = [1, 2, 1, 0, 3]
    mpg = 10

    # This will print out the valid city's index within the city_distances array
    print("valid starting city index:", greedy_approach(city_distances, fuel, mpg))


Hamilton_Problem()

