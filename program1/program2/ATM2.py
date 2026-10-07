# Basic ATM Simulation

balance = 5000

while True:
    print("\n--- ATM MENU ---")
    print("1. Balance Inquiry")
    print("2. Deposit")
    print("3. Withdrawal")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Current Balance:", balance)

    elif choice == 2:
        amount = float(input("Enter deposit amount: "))
        balance += amount
        print("Amount deposited successfully.")
        print("New Balance:", balance)

    elif choice == 3:
        amount = float(input("Enter withdrawal amount: "))

        if amount <= balance:
            balance -= amount
            print("Please collect your cash.")
            print("Remaining Balance:", balance)
        else:
            print("Insufficient balance.")

    elif choice == 4:
        print("Thank you for using the ATM.")
        break

    else:
        print("Invalid choice. Please try again.")