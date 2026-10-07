# ATM with PIN Verification

correct_pin = 1234
balance = 10000

pin = int(input("Enter your PIN: "))

if pin == correct_pin:

    while True:
        print("\n===== ATM MENU =====")
        print("1. Balance Inquiry")
        print("2. Deposit")
        print("3. Withdrawal")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Your balance is:", balance)

        elif choice == 2:
            amount = float(input("Enter deposit amount: "))

            if amount > 0:
                balance += amount
                print("Deposit successful.")
                print("Updated balance:", balance)
            else:
                print("Invalid amount.")

        elif choice == 3:
            amount = float(input("Enter withdrawal amount: "))

            if amount > 0 and amount <= balance:
                balance -= amount
                print("Withdrawal successful.")
                print("Remaining balance:", balance)
            elif amount > balance:
                print("Insufficient balance.")
            else:
                print("Invalid amount.")

        elif choice == 4:
            print("Thank you. Please collect your card.")
            break

        else:
            print("Invalid choice.")

else:
    print("Incorrect PIN. Access denied.")