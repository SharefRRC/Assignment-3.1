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