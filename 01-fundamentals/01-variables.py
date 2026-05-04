# 01 - Variables and types
name = "World"
print(name)

# Variables of different types
age = 109
hourly_rate = 65.05
is_engineer = True
nothing = None

print(age)
print(hourly_rate)
print(is_engineer)
print(nothing)

# f-strings (Python's template literals)
weekly_rate = hourly_rate * 40

print(f'Hello, {name}. You are {age} years old.')
print(f'My rate is ${hourly_rate} per hour')
print(f'My rate is ${weekly_rate} per week')

# Type hints (Python's TypeScript)
age: int = 109
hourly_rate: float = 65.05
is_engineer: bool = True
nothing: None = None

# A real calculation
annual_income: float = weekly_rate * 52
take_home_income: float = annual_income * .75

print(f'Hourly: ${hourly_rate}')
print(f'Annual: ${annual_income}')
print(f'Take-home: ${take_home_income}')

def calculate_take_home(hourly_rate: float, tax_rate: float) -> float:
    weekly_rate = hourly_rate * 40
    annual_income = weekly_rate * 52
    take_home_income: float = annual_income * (1 - tax_rate)

    return take_home_income

print(f'Take-home: ${calculate_take_home(65.05, 0.25):.2f}')