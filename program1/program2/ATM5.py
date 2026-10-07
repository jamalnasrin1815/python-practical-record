# Complete ATM Simulation System

balance = 10000
pin = 1234

print("================================")
print("       WELCOME TO ATM")
print("================================")

entered_pin = int(input("Enter your PIN: "))

if entered_pin == pin:

    while True:
        print("\n--------- ATM MENU ---------")
        print("1. Balance Inquiry")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        print("----------------------------")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("\nYour current balance is ₹", balance)

        elif choice == 2:
            amount = float(input("Enter amount to deposit: "))

            if amount > 0:
                balance = balance + amount
                print("₹", amount, "deposited successfully.")
                print("Current balance: ₹", balance)
            else:
                print("Please enter a valid amount.")

        elif choice == 3:
            amount = float(input("Enter amount to withdraw: "))

            if amount <= 0:
                print("Please enter a valid amount.")

            elif amount > balance:
                print("Insufficient balance.")

            else:
                balance = balance - amount
                print("Please collect your cash.")
                print("₹", amount, "withdrawn successfully.")
                print("Remaining balance: ₹", balance)

        elif choice == 4:
            print("\n================================")
            print("Thank you for using our ATM!")
            print("Please collect your card.")
            print("================================")
            break

        else:
            print("Invalid choice. Please select 1-4.")

else:
    print("Incorrect PIN.")
    print("Transaction cancelled.")