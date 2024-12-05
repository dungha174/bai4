print ("Hà Mạnh Dũng")
print("235752021610006")
def calculate_balance(transactions):
    balance = 0
    for transaction in transactions:
        type, amount = transaction.split()
        amount = int(amount)
        if type == 'D':
            balance += amount
        elif type == 'W':
            balance -= amount
    return balance
transactions = []
while True:
    transaction = input("Nhập nhật ký giao dịch (hoặc gõ 'q' để kết thúc): ")
    if transaction.lower() == 'q':
        break
    transactions.append(transaction)
balance = calculate_balance(transactions)
print("Số tiền thực của tài khoản là:", balance)
