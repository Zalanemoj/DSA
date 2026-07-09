import datetime
import sys
import Bike_Rental

# TODO 7 - Create Customer Class and initialize attributes
class Customer:
    def __init__(self):
        """Initializing of Customer class"""
        self.bikes=0
        self.rental_basis=0
        self.rental_time=0
        self.bill=0

    # TODO 8 - Create a method to request bike from the system
    def request_bike(self):
        """Takes a request from the customer for the number of bikes"""
        bikes=int(input("Enter the number of bikes: "))
        try:
            bikes=int(bikes)
        except ValueError:
            print("Please enter a valid integer")
            return -1
        if bikes <= 0:
            raise ValueError("Please enter a Positive number It cannot be zero")
        else:
            self.bikes=bikes
        return self.bikes

    # TODO 9 - Create a method to return bike to the system
    def return_bike(self):
        """Allows customers to return their bikes to the rental shop"""
        if self.rental_basis and self.rental_time and self.bikes:
            return self.rental_time,self.rental_basis,self.bikes
        else:
            return 0,0,0