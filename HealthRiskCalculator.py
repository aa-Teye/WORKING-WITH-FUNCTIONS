def calculate_risk(age: float, multiplier: float = 1.5, max_age: float = 120.0):
    # 1. First, we check if the age is valid
    if age > max_age:
        return -1.0
    
