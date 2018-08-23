
finished = False
result = 0
while not finished:
    try:
        number = int(input("Enter the number: "))
        result = number
        finished = True

    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", result)