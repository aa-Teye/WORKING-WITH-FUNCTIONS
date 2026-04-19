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
# 1. We add 'tax_rate', 'fee', and 'limit' as default settings ⚙️
def calculate_levy(amount: float, tax_rate: float = 0.01, fee: float = 2.0, limit: float = 10000.0):
    
    if amount > limit: 
        return -1.0, -1.0 # Return two flags for the two expected values
    
    # 2. Add an extra tier: Transactions > 1000 pay a higher service fee
    if amount > 1000:
        current_fee = fee + 3.0  # Total fee becomes 5 GHS
    else:
        current_fee = fee

    # 3. Logic for the levy
    if amount > 100:
        levy = amount * tax_rate
    else:
        levy = 0.0
    
    # 4. Calculate total cost
    total_with_charges = amount + levy + current_fee
    
    return levy, total_with_charges

# --- Execution ---
amount = float(input("Enter the amount: "))

# We 'unpack' the two values coming back from the function
levy_res, total_res = calculate_levy(amount)

if levy_res == -1.0:
    print("❌ Transaction amount exceeds the limit.")
else:
    print(f"📊 Levy: {levy_res} GHS")
    print(f"💰 Total to be deducted: {total_res} GHS")