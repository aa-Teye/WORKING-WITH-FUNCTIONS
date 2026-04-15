def calculate_levy(amount:float):
    if amount > 100:
        return amount * 0.01
    else:
        return 0
    

amount = float(input("Enter the amount: "))
result = calculate_levy(amount)
print(f"The levy for this transaction is : {result}")