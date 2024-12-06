
transaction_records = []


net_balance = 0

num_transactions = int(input("Enter the number of transactions: "))

for i in range(num_transactions):
    transaction = input("Enter transaction (Deposit/Withdraw and amount): ")
    
    transaction_type, amount = transaction.split()
    amount = int(amount)

    if transaction_type.lower() == "deposit":
        net_balance += amount  # Add amount to net balance
        transaction_records.append(f"Deposit {amount}")  # Add transaction record
    
    elif transaction_type.lower() == "withdraw":
        net_balance -= amount  # Subtract amount from net balance
        transaction_records.append(f"Withdraw {amount}")  # Add transaction record
    
    else:
        print("Invalid transaction type. Please use 'Deposit' or 'Withdraw'.")
        continue

print("\nTransaction Records:")
for record in transaction_records:
    print(record)

print("\nNet Balance:", net_balance)
