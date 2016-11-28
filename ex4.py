# number of cars
cars = input("Number of cars: " )

# total capacity per car
space_in_a_car = input("Car Capacity: ")

# number of drivers
drivers = input("Number of drivers: ")

# total number of passengers
passengers = input("Total number of passengers: ")

# cars not being driven (number of cars minus the number of drivers) only one driver per car
cars_not_driven = cars - drivers

# number of cars driven = number of drivers
cars_driven = drivers

# total capacity of carpool.  Number of cars driven * the capacity per car
carpool_capacity = cars_driven * space_in_a_car

# the actual average number of passengers per car based on the number of cars driven
average_passengers_per_car = passengers / cars_driven

print "There are ", cars, " cars available."
print "There are only ", drivers, " drivers available."
print "There will be ", cars_not_driven, " empty cars today."
print "We can transport ", carpool_capacity, " people today."
print "We have ", passengers, " to carpool today."
print "We need to put about ", average_passengers_per_car, " in each car."