def inputs():
    # We would need to know how far the cities are from each other.
    # Let us create an empty list to append the wanted values of distance.
    city_distance = []
    
    # Ask the user to input the values of the distances between each city and create/append into 'city_distance'
    distance = input("Enter a list of numbers seperated by commas: ")
    city_distance = [x.strip() for x in distance.split(",")]
        
    # We would need to know at which cities, how much gallon(s) of gas we will get for the travel to the next city.
    # Let us create an empty list to append the wanted values of fuel for each stop.
    fuel = []
    
    # Ask the user to input the values of gallon(s) for each stop in a city is.
    gallon = input(f"Enter a list of {len(city_distance)} elements respective to how much gallon(s) is taken for each stop, seperated by commas: ")
    fuel = [x.strip() for x in gallon.split(",")]       # I still need to find a way to implement a Error exempt.
    
    # We would need an input of how efficient the car will be traveling throughout the cities.
    mpg = int(input("How fast will the car be going? (mpg): "))
    
    # Return the values to be used for the Hamiltonian Problem.
    print(city_distance, fuel, mpg)         # i have this to just check if my values are coming back correctly.
    return city_distance, fuel, mpg


# I might try to recall this problem onto the main.py? maybe idk...
def Hamiltonian_Problem(city_distance, fuel, mpg):
    print(city_distance, fuel, mpg)
    return city_distance, fuel, mpg

    '''
    for i in range(city_distance):
        
        return
    
    return
    '''

inputs()
Hamiltonian_Problem(inputs.city_distance, inputs.fuel, inputs.mpg)