
def main():
STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales",
               "NT": "Northern Territory", "WA": "Western Australia",
               "ACT": "Australian Capital Territory", "VIC": "Victoria",
               "TAS": "Tasmania"}

for abbreviation in STATE_NAMES:
    state = abbreviation
    # print(abbreviation, "is", STATE_NAMES[state])
    print("{:3} is {}".format(abbreviation, STATE_NAMES[state]))

main()