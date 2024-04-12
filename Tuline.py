#tuline

def encode(password):
    return ''.join(str((int(char) + 3) % 10) for char in password)

def decode(encodedpass):
    ogpass = ''
    for item in encodedpass:
        a = int(item) - 3
        if a < 0:
            ogpass += str(a + 10)
        else:
            ogpass += str(a)
    return ogpass


def main():
    encoded_password = None

    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        option = input("Please enter an option: ")

        if option == "1":
            password = input("Please enter your password to encode: ")
            if len(password) == 8 and password.isdigit():
                encoded_password = encode(password)
                print("Your password has been encoded and stored!")
            else:
                print("Invalid password. Please make sure it is an 8-digit number.")
        elif option == "2":
            if encoded_password:
                decoded_password = decode(encoded_password)
                print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")
            else:
                print("No password available to decode.")
        elif option == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
