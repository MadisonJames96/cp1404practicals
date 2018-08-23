def main():
    password = get_password()
    password = len(password)
    stars = number_of_stars(password)

def get_password():
    MIN_LENGTH = 2
    password = input("Password: ")
    while len(password) < MIN_LENGTH:
        print("password to short")
        password = input("Password: ")
    else:
        return password

def number_of_stars(password):
    for i in range(password):
        print('*', end=' ')
    print()

main()
