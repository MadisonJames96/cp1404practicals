from prac_06.guitar import Guitar

def main():
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = Guitar(name, year, cost)

    print(guitar)

    print(guitar.get_age())
    print(guitar.is_vintage())

    print("{} get_age() - Expected {}. Got {}".format(guitar.name, 96,
                                                      guitar.get_age()))


main()