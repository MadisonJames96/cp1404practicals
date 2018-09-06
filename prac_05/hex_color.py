def main():
COLOUR_NAMES = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "BlueViolet": "#8a2be2", "CadetBlue": "#5f9ea0",
                "chartreuse1": "#7fff00", "chocolate": "#d2691e", "cyan4": "#008b8b", "DarkOrchid": "#9932cc",
                "DarkViolet": "#9400d3", "DimGray": "#696969"}

colour = input("Enter colour name: ")
while colour != "":
    if colour in COLOUR_NAMES:
        print(COLOUR_NAMES[colour])
    else:
        print("Invalid colour name")
    colour = input("Enter colour name: ")

main()