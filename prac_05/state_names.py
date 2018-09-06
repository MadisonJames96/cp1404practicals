def main():
    STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales",
                   "NT": "Northern Territory", "WA": "Western Australia",
                   "ACT": "Australian Capital Territory", "VIC": "Victoria",
                   "TAS": "Tasmania"}

    state = input("Enter short state: ").upper()
    while state != "":
        if state in STATE_NAMES:
            print(state, "is", STATE_NAMES[x])
        else:
            print("Invalid short state")
        state = input("Enter short state: ").upper()

main()