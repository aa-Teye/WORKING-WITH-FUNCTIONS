def calculate_levy(amount:float):
    if amount > 10000: 
        return "You have exceeded the amount limit for this transaction"
    if amount > 100:
        return (amount * 0.01) + 2
    elif amount < 100:
        return 0
    else:
        return amount * 0.01
    


amount = float(input("Enter the amount: "))
result = calculate_levy(amount)
print(f"The levy for this transaction is : {result}")