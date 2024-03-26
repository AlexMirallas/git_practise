destinations = ["Paris, France", "Shanghai, China","Los Angeles, USA", "Sao Paulo, Brazil","Cairo Egypt"]

test_traveler = ["Erin Wilkes", "Shangai, China",["historical site","art"]]

attractions = [[] for i in range(len(destinations))]

def get_destination_index(destination):
    destination_index = destinations.index(destination)
    return destination_index
    


#print(get_destination_index("Paris, France"))

def get_traveler_location(traveler):
    traveler_destination = traveler[1]
    traveler_destination_index = traveler.index(traveler_destination)
    return (traveler_destination_index)


test_destination_index = (get_traveler_location(test_traveler))

print(test_destination_index)
print(attractions)

def add_attraction(destination,attraction):
    destination_index = get_destination_index(destination)
    attractions_for_destination = attractions[destination_index]
    attractions_for_destination.append(attraction)
    return attractions_for_destination

add_attraction("Los Angeles, USA",["Venice Beach", ["beach"]])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("Sao Paulo, Brazil", ["Sao Paulo Zoo", ["zoo"]])
add_attraction("Sao Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

print(attractions)






    






