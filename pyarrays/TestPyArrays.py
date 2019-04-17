# Python does not have built-in support for Arrays,
# but Python Lists can be used instead.

def showArrays():
    cars = ["Ford", "Volvo", "BMW"]
    for car in cars:
        print("Car Type : ", car)
    # Add some new cars
    cars.append("Mercedes")
    cars.append("Maruti")
    print("All cars : ", cars)

    # Show all car along with index value
    for i in cars:
        carIndex = cars.index(i)
        print(i + "<=========>" + str(carIndex))

    # Find the size of cars list
    print("Size of the list : ",len(cars))

    #delete by index
    cars.pop(3) # Third index

    # Remove by Object
    cars.remove("Maruti")

    print("Now all cars : ",cars)


if __name__ == "__main__":
    showArrays()
