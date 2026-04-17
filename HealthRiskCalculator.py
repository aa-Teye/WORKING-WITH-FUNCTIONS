def calculate_risk(age: float, multiplier: float = 1.5, max_age: float = 120.0):
    # 1. First, we check if the age is valid
    if age > max_age:
        return -1.0
    
    # 2. Then, we do the math and return the result
    risk_score = age * multiplier
    return risk_score

# --- Execution ---
user_age = float(input("Enter patient age: "))

# We call the function. It will use 1.5 and 120.0 automatically!
result = calculate_risk(user_age)

if result == -1.0:
    print("Invalid age entered.")
else:
    print(f"Patient Risk Score: {result}")