from prac_08.silver_service_taxi import SilverServiceTaxi
from prac_08.taxi import Taxi

def main():

    taxi = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    bill = 0

    print("Let's drive!")
    menu_choice = input("q)uit, c)hoose taxi, d)rive")
    print(menu_choice)
    if menu_choice != "q":
        if menu_choice == "c":
            print("Taxi available:")
            print(taxi)
            taxi_choice = int(input("Choose taxi: "))
            taxi_selected = [taxi_choice]
            print("Bill to date: {}".format(bill))
            print()

        else:
            distance = int(input("Drive how far?"))
            taxi.drive(distance)
            print("Your {} trip cost you ${}".format(taxi.name, taxi.get_fare))
            bill = bill + taxi.get_fare
            print("Bill to date: {}".format(bill))


    print("Total trip cost: ${}".format(bill))
    print("Taxis are now:")
    print(taxi)




main()
