import datetime

# TODO 1 - Create Bike Rental Class and initialize stock attribute
class BikeRental:
    """Initializing the bike rental class"""
    def __init__(self,stock:int=0):
        self.stock=stock

    # TODO 2 - Create a method to display stock
    def display_stock(self)->None:
        """Display the stock that is currently available"""
        print(f"The stock available is {self.stock}")

    # TODO 3 - Create a method to rent bike on hourly bases
    def rent_bike_on_hourly_basis(self,number_of_bikes):
        """Rental bike on hourly basis"""
        if number_of_bikes<0:
            raise ValueError("The number of bikes cannot be negative")
        elif number_of_bikes>self.stock:
            raise ValueError("The number of bikes cannot be greater than the stock")
        else:
            now=datetime.datetime.now()
            self.stock-=number_of_bikes
            print(f"You have rent {number_of_bikes} on hourly basis today at {now}")
            print(" You will be charged $5 for each bike per hour")
            return now

    # TODO 4 - Create a method to rent bike on daily bases
    def rent_bike_on_daily_basis(self,number_of_bikes):
        """Rental bike on daily basis"""
        if number_of_bikes<0:
            raise ValueError("The number of bikes cannot be negative")
        elif number_of_bikes>self.stock:
            raise ValueError("The number of bikes cannot be greater than the stock")
        else:
            now=datetime.datetime.now()
            self.stock-=number_of_bikes
            print(f"You have rent {number_of_bikes} on daily basis today at {now}")
            print(" You will be charged $30 for each bike per day")
            return now

    # TODO 5 - Create a method to rent bike on weekly bases
    def rent_bike_on_weekly_basis(self,number_of_bikes):
        """Rental bike on weekly basis"""
        if number_of_bikes<0:
            raise ValueError("The number of bikes cannot be negative")
        elif number_of_bikes>self.stock:
            raise ValueError("The number of bikes cannot be greater than the stock")
        else:
            now=datetime.datetime.now()
            self.stock-=number_of_bikes
            print(f"You have rent {number_of_bikes} on weekly basis today at {now}")
            print(" You will be charged $60 for each bike per week")
            return now

    # TODO 6 - Create a method to return bike from the system
    def return_bike(self,request)->None:
        """return the bike rented bike and increase the system"""
        rental_time,rental_basis,number_of_bikes=request
        bill=0
        if rental_time and rental_basis and number_of_bikes:
            self.stock+=number_of_bikes
            now=datetime.datetime.now()
            rental_period=now-rental_time
            if rental_basis == 1:
                bill = rental_period.seconds / 3600 * (5 * number_of_bikes)
            elif rental_basis == 2:
                bill= rental_period.days * (30 * number_of_bikes)
            elif rental_basis == 3:
                bill= (rental_period.days/7) * (60 * number_of_bikes)
            if 3 <= number_of_bikes <= 6:
                print("You are eligible for Family Rental promotion which is 30%")
                bill=int(bill*.7)
            print("Thanks for returning your bike hope you enjoyed the service!")
            print(f"Total bill is {bill}")
        else:
            raise Exception("You have not rented the bike from us.")
        return bill