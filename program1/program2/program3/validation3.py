# Password Validation and Basic Encryption

password = input("Enter your password: ")

if len(password) < 8:
    print("Password is too short.")
else:
    has_upper = any(ch.isupper() for ch in password)
    has_lower = any(ch.islower() for ch in password)
    has_digit = any(ch.isdigit() for ch in password)
    has_special = any(not ch.isalnum() for ch in password)

    if has_upper and has_lower and has_digit and has_special:
        print("Password is strong.")

        encrypted = ""

        for ch in password:
            encrypted += chr(ord(ch) + 3)

        print("Encrypted Password:", encrypted)

    else:
        print("Password is not strong enough.")