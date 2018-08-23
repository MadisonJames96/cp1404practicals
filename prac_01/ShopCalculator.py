

NumberOfItems = float(input("Number of items: "))
while NumberOfItems < 0:
    print("Invalid number of items!")
    NumberOfItems = float(input("Number of items: "))
loop = 0
Total = 0
while loop != NumberOfItems:
    PriceOfItem = float(input("Price of item: $"))
    Total = PriceOfItem + Total
    ItemPrice = PriceOfItem
    loop = loop + 1
# TODO use for loop

if Total > 100:
    TotalPercent = Total / 10
    Total = Total - TotalPercent
print("Total price for {} items is ${:.2f}".format(NumberOfItems, Total))
