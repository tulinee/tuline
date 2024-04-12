#tuline

def encode(password):
    return ''.join(str((int(char) + 3) % 10) for char in password)


def main():
    encoded_password = None

    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("3. Quit")
        option = input("Please enter an option: ")

        if option == "1":
            password = input("Please enter your password to encode: ")
            if len(password) == 8 and password.isdigit():
                encoded_password = encode(password)
                print("Your password has been encoded and stored!")
            else:
                print("Invalid password. Please make sure it is an 8-digit number.")

        elif option == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
