# Secure Password Validation and Encryption

def check_strength(password):
    if len(password) < 8:
        return False

    upper = False
    lower = False
    digit = False
    special = False

    for ch in password:
        if ch.isupper():
            upper = True
        elif ch.islower():
            lower = True
        elif ch.isdigit():
            digit = True
        else:
            special = True

    return upper and lower and digit and special


def encrypt_password(password):
    encrypted = ""

    for ch in password:
        encrypted += chr(ord(ch) + 3)

    return encrypted


while True:

    print("\n===== PASSWORD SECURITY SYSTEM =====")
    print("1. Validate and Encrypt Password")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        password = input("Enter password: ")

        if check_strength(password):

            print("Password Strength: STRONG")

            encrypted = encrypt_password(password)

            with open("password.txt", "w") as file:
                file.write(encrypted)

            print("Password encrypted successfully.")
            print("Encrypted data:", encrypted)
            print("Data saved to password.txt")

        else:
            print("Password Strength: WEAK")
            print("Password must contain:")
            print("- At least 8 characters")
            print("- One uppercase letter")
            print("- One lowercase letter")
            print("- One digit")
            print("- One special character")

    elif choice == "2":
        print("Thank you for using the Password Security System.")
        break

    else:
        print("Invalid choice.")