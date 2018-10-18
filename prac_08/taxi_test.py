
from prac_08.taxi import Taxi


def main():

    taxi = Taxi("Prius 1", 100)
    taxi.drive(40)
    print("taxi name =", taxi.name)
    print("current fare = $", taxi.get_fare())
    taxi.start_fare()
    taxi.drive(100)
    print("taxi name =", taxi.name)
    print("current fare = $", taxi.get_fare())

main()