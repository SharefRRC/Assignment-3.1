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

# Iterate through the dictionary and calculate interest
for account_number, balance in account_balances.items():
    if balance >= 5000:
        # 5.0% interest for balances >= $5000
        interest = balance * 0.05 / 12
    elif balance >= 1000:
        # 2.5% interest for balances >= $1000 and < $5000
        interest = balance * 0.025 / 12
    elif balance > 0:
        # 1.0% interest for balances > $0 and < $1000
        interest = balance * 0.01 / 12
    elif balance < 0:
        # 10.0% interest charge for negative balances
        interest = balance * 0.10 / 12
    else:
        # No interest for zero balance
        interest = 0

    # Update the balance with the calculated interest
    account_balances[account_number] += interest

# Pretty print the updated dictionary
pprint.pprint(account_balances)

# Define the output filename with initials (e.g., FL for First Last)
output_filename = "updated_balances_SI.csv"

# Write the updated account balances to the CSV file
with open(output_filename, "w") as file:
    # Write the header
    file.write("Account,Balance\n")
    # Write each account and balance to the file
    for account_number, balance in account_balances.items():
        file.write(f"{account_number},{balance:.6f}\n")