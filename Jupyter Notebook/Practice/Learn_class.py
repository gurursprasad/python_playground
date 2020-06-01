class Car:

    def __init__(self):
        # A dictionary to map the type of car and price per day
        self.carFare = {'Hatchback': 30, 'Sedan': 50, 'SUV': 100}

    def display_fare_details(self):
        print("Cost per day: ")
        print("Hatchback: RS",self.carFare['Hatchback'])
        print("Sedan: RS", self.carFare['Sedan'])
        print("SUV: RS", self.carFare['SUV'])

    def calculate_fare(self, type_of_car, number_of_days):
        # Calculate the fare depending upon the type of car and number of days as requested by the user
        return self.carFare[type_of_car] * number_of_days


car = Car()
while True:
    print("Enter 1 to display the fare details")
    print("Enter 2 to rent a car")
    print("Enter 3 to exit")
    userChoice = (int(input()))
    if userChoice is 1:
        car.display_fare_details()
    elif userChoice is 2:
        print("Enter the type of car you would like to borrow")
        typeOfCar = input()
        print("Enter the number of days you would like to borrow the car")
        numberOfDays = int(input())
        fare = car.calculate_fare(typeOfCar, numberOfDays)
        print("Total payable amount: RS",fare)
        print("Thank you!")
    elif userChoice is 3:
        quit()
