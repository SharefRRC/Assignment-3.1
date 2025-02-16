import random

# Define menu options
menu_options = ["D", "W", "Q"]

# Generate a random initial balance between -1,000 and 10,000
balance = random.randint(-1000, 10000)

# Format the balance as currency
formatted_balance = f"${balance:,.2f}"

# Display the selection menu
print("*" * 40)
print("PIXELL RIVER FINANCIAL".center(40))
print("ATM Simulator".center(40))
print()
print(f"Balance: {formatted_balance}".center(40))
print()
print("Deposit: D".center(40))
print("Withdraw: W".center(40))
print("Quit: Q".center(40))
print("*" * 40)

# Get user input
user_choice = input("Enter your selection: ").strip().upper()

# Validate user input
if user_choice in menu_options:
    if user_choice == "D":
        # Deposit logic
        deposit_amount = float(input("Enter the transaction amount: "))
        if deposit_amount > 0:
            balance += deposit_amount
            print("\n" + "*" * 40)
            print(f"Balance: ${balance:,.2f}".center(40))
            print("*" * 40)
        else:
            print("\n" + "*" * 40)
            print("INVALID TRANSACTION".center(40))
            print("*" * 40)
    elif user_choice == "W":
        # Withdraw logic
        withdraw_amount = float(input("Enter the transaction amount: "))
        if withdraw_amount > 0:
            if balance >= withdraw_amount:
                balance -= withdraw_amount
                print("\n" + "*" * 40)
                print(f"Balance: ${balance:,.2f}".center(40))
                print("*" * 40)
            else:
                print("\n" + "*" * 40)
                print("INSUFFICIENT FUNDS".center(40))
                print("*" * 40)
        else:
            print("\n" + "*" * 40)
            print("INVALID TRANSACTION".center(40))
            print("*" * 40)
    elif user_choice == "Q":
        # Quit the program
        print("\nThank you for using PIXELL RIVER FINANCIAL. Goodbye!")
else:
    # Handle invalid selection
    print("\n" + "*" * 40)
    print("INVALID SELECTION".center(40))
    print("*" * 40)

#Adding main loop for multiple transaction
import time
import os

# Define menu options
menu_options = ["D", "W", "Q"]

# Generate a random initial balance between -1,000 and 10,000
balance = random.randint(-1000, 10000)

# Define a variable to control the main loop
running = True

# Main program loop
while running:
    # Format the balance as currency
    formatted_balance = f"${balance:,.2f}"

    # Display the selection menu
    print("*" * 40)
    print("PIXELL RIVER FINANCIAL".center(40))
    print("ATM Simulator".center(40))
    print()
    print(f"Balance: {formatted_balance}".center(40))
    print()
    print("Deposit: D".center(40))
    print("Withdraw: W".center(40))
    print("Quit: Q".center(40))
    print("*" * 40)

    # Get user input
    user_choice = input("Enter your selection: ").strip().upper()

    # Validate user input
    if user_choice in menu_options:
        if user_choice == "D":
            # Deposit logic
            deposit_amount = float(input("Enter the transaction amount: "))
            if deposit_amount > 0:
                balance += deposit_amount
                print("\n" + "*" * 40)
                print(f"Balance: ${balance:,.2f}".center(40))
                print("*" * 40)
            else:
                print("\n" + "*" * 40)
                print("INVALID TRANSACTION".center(40))
                print("*" * 40)
        elif user_choice == "W":
            # Withdraw logic
            withdraw_amount = float(input("Enter the transaction amount: "))
            if withdraw_amount > 0:
                if balance >= withdraw_amount:
                    balance -= withdraw_amount
                    print("\n" + "*" * 40)
                    print(f"Balance: ${balance:,.2f}".center(40))
                    print("*" * 40)
                else:
                    print("\n" + "*" * 40)
                    print("INSUFFICIENT FUNDS".center(40))
                    print("*" * 40)
            else:
                print("\n" + "*" * 40)
                print("INVALID TRANSACTION".center(40))
                print("*" * 40)
        elif user_choice == "Q":
            # Quit the program
            print("\nThank you for using PIXELL RIVER FINANCIAL. Goodbye!")
            running = False
    else:
        # Handle invalid selection
        print("\n" + "*" * 40)
        print("INVALID SELECTION".center(40))
        print("*" * 40)

    # Pause for 3 seconds and clear the screen
    if running:
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')