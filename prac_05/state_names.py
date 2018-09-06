# TODO: Reformat this file so the dictionary code follows PEP 8 convention
STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales",
               "NT": "Northern Territory", "WA": "Western Australia",
               "ACT": "Australian Capital Territory", "VIC": "Victoria",
               "TAS": "Tasmania"}

state = input("Enter short state: ")
x = state.upper()
while x != "":
    x = state.upper()
    if x in STATE_NAMES:
        print(state, "is", STATE_NAMES[x])
    else:
        print("Invalid short state")
    state = input("Enter short state: ")
