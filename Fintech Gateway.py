def calculate_levy(amount:float):
    if amount > 10000: 
        return -1.0
    if amount > 100:
        return (amount * 0.01) + 2
    elif amount < 100:
        return 0
    else:
        return amount * 0.01
    


amount = float(input("Enter the amount: "))
result = calculate_levy(amount)

if result == -1.0:
    print("Transaction amount exceeds the limit for levy calculation.")
else:
    print(f"The levy for this transaction is: {result}")


# Alternate to How A Backend Developer would have done That
