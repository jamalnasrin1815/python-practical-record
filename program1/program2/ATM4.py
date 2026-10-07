# ATM with Withdrawal Limit

balance = 15000
daily_limit = 10000
withdrawn = 0

while True:
    print("\n===== ATM SYSTEM =====")
    print("1. Balance Inquiry")
    print("2. Deposit")
    print("3. Withdrawal")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Available Balance:", balance)

    elif choice == 2:
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            balance += amount
            print("Deposit successful.")
            print("New Balance:", balance)
        else:
            print("Invalid deposit amount.")

    elif choice == 3:
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Invalid withdrawal amount.")

        elif amount > balance:
            print("Insufficient balance.")

        elif withdrawn + amount > daily_limit:
            print("Daily withdrawal limit exceeded.")

        else:
            balance -= amount
            withdrawn += amount
            print("Please collect your cash.")
            print("Remaining Balance:", balance)
            print("Withdrawn Today:", withdrawn)

    elif choice == 4:
        print("Thank you for using our ATM.")
        break

    else:
        print("Invalid choice.")