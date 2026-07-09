import Bike_Rental as br
import Customer as cm

bike_system=br.BikeRental(100)
customer=cm.Customer()
# TODO 10 - Main program logic : print options to the console
while True:
    print("""
        ====== Bike Rental App ======
        1. Display available bikes
        2. Request a bike on hourly basis - $5
        3. Request a bike on daily basis - $20
        4. Request a bike on weekly basis - $60
        5. Return a bike(s)
        6. Exit """)

    # TODO 11 - Ask from user to get option (check if it is int)
    choise=input("Enter your choice: ")
    try:
        choise = int(choise)
    except ValueError:
        print("Please enter a valid integer")
        continue

    # TODO 12 - Based on selected choice call methods from Bike
    if choise==1:
        bike_system.display_stock()
    elif choise==2:
        customer.rental_time=bike_system.rent_bike_on_hourly_basis(customer.request_bike())
        customer.rental_basis=1
    elif choise==3:
        customer.rental_time = bike_system.rent_bike_on_daily_basis(customer.request_bike())
        customer.rental_basis = 2
    elif choise==4:
        customer.rental_time = bike_system.rent_bike_on_weekly_basis(customer.request_bike())
        customer.rental_basis = 3
    elif choise==5:
        bill=bike_system.return_bike(customer.return_bike())
        customer.bill=bill
        rental_time, rental_basis, number_of_bikes =0,0,0
    elif choise==6:
        break
    else:
        raise ValueError('Please enter a valid integer between 1 and 6')
