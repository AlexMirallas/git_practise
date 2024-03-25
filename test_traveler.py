destinations = ["Paris, France", "Shangai, China","Los Angeles, USA", "Sao Paolo, Brazil","Cairo Egypt"]

test_traveler = ["Erin Wilkes", "Shangai, China",["historical site","art"]]

def get_destination_index(destination):
    destination_index = destinations.index(destination)
    return destination_index
    


#print(get_destination_index("Paris, France"))

def get_traveler_location(traveler):
    traveler_destination = traveler[1]
    traveler_destination_index = traveler.index(traveler_destination)
    print(traveler_destination_index)


get_traveler_location(test_traveler)



    






