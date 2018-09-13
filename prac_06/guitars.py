from prac_06.guitar import Guitar

def main():

    guitar_list = []
    print("My guitars!")
    name = input("Name:")
    while name != "":
        year = int(input("Years: "))
        cost = float(input("Cost: $"))
        guitar_list.append(Guitar(name, year, cost))
        print("{} ({}) : ${:1,.2f} added.".format(name, year, cost))
        name = input("Name: ")

    guitar_list.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitar_list.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    print("These are my guitars:")
    for i, guitar in enumerate(guitar_list):
        if Guitar.is_vintage(guitar):
            vintage_string = "(vintage)"
            print("Guitar {}: {:>20} ({}), worth ${:1,.2f}{}".format(i + 1, guitar.name, guitar.year, guitar.cost,
                                                                  vintage_string))
        else:
            vintage_string = " "
            print("Guitar {}: {:>20} ({}), worth ${:1,.2f}{}".format(i + 1, guitar.name, guitar.year, guitar.cost,
                                                                      vintage_string))




main()