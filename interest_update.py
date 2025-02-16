import pprint

# Define an empty dictionary to store account balances
account_balances = {}

# Open the input file and read account balances
with open("account_balances.txt", "r") as file:
    for line in file:
        # Split each line into account number and balance
        account_number, balance = line.strip().split("|")
        # Add the account number and balance to the dictionary
        account_balances[account_number] = float(balance)

# Pretty print the dictionary
pprint.pprint(account_balances)