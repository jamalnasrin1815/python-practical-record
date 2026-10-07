# Password Encryption and File Storage

password = input("Enter your password: ")

if len(password) < 8:
    print("Password must contain at least 8 characters.")

else:
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        else:
            has_special = True

    if has_upper and has_lower and has_digit and has_special:

        encrypted = ""

        for ch in password:
            encrypted += chr(ord(ch) + 3)

        with open("password.txt", "w") as file:
            file.write(encrypted)

        print("Password is strong.")
        print("Encrypted password:", encrypted)
        print("Encrypted password stored in password.txt")

    else:
        print("Password is weak.")