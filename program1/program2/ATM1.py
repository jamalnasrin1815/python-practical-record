# ATM Simulation with PIN Verification

balance = 10000
correct_pin = 1234

pin = int(input("Enter your PIN: "))

if pin == correct_pin:

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

            if amount > 0:
                balance += amount
                print("Amount deposited successfully.")
                print("New Balance:", balance)
            else:
                print("Invalid amount.")

        elif choice == 3:
            amount = float(input("Enter withdrawal amount: "))

            if amount > 0 and amount <= balance:
                balance -= amount
                print("Please collect your cash.")
                print("Remaining Balance:", balance)
            else:
                print("Insufficient balance or invalid amount.")

        elif choice == 4:
            print("Thank you for using the ATM.")
            break

        else:
            print("Invalid choice. Please try again.")

else:
    print("Incorrect PIN. Access Denied.")
