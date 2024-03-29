destinations = ["Paris, France", "Shanghai, China","Los Angeles, USA", "Sao Paulo, Brazil","Cairo, Egypt"]

test_traveler = ["Erin Wilkes", "Shanghai, China",["historical site","art"]]

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

#print(test_destination_index)
#print(attractions)

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

#print(attractions)

def find_attractions(destination,interests):
    destination_index = get_destination_index(destination)
    attractions_in_city = attractions[destination_index]
    attractions_with_interest = []
    for possible_attraction in attractions_in_city:
        attraction_tags = possible_attraction[1]
        for interest in interests:    
            if interest in attraction_tags:
                attractions_with_interest.append(possible_attraction[0])
    return attractions_with_interest

#print(find_attractions("Los Angeles, USA",["art"]))

def get_attractions_for_traveler(traveler):
    traveler_destination =  traveler[1]
    traveler_interests = traveler[2]
    traveler_attractions = find_attractions(traveler_destination,traveler_interests)
    traveler_attractions = ", ".join(traveler_attractions)
    interests_string = ("Hi "+ str(traveler[0]) + ", we think you will like these places around " +str(traveler_destination)+": " + traveler_attractions)

    return interests_string

print(get_attractions_for_traveler(test_traveler))
print(get_attractions_for_traveler(["Dereck Smill", "Paris, France", ["monument"]]))







    

        








    






