# Default parameter values
def greet(name: str, greeting: str = "Hello") -> str:
    return f'{greeting}, {name}'

print(greet("World"))
print(greet("World", "Hi"))
print(greet(name="World", greeting="Hey"))

print("-------")
# *args and **kwargs
def summarize_team(team_name: str, *members: str, **details):
    print(team_name)

    for member in members:
        print(member)

    for key, value in details.items():
        print(f'{key}: {value}')

summarize_team(
    "Frontend Squad",
    "Jane",
    "John",
    "Ash",
    location="Remote",
    size=3,
    active=True,
)

print("-------")
# Multiple return values (Python's tuple superpower)
def analyze_numbers(numbers: list[int]) -> tuple: 
    low: int = min(numbers)
    high: int = max(numbers)
    total: int = sum(numbers)
    length_of_list: int = len(numbers)
    avg: float = total // length_of_list

    return low, high, avg

low, high, avg = analyze_numbers([10, 20, 30, 40, 50])

print(low)
print(high)
print(avg)

print("-------")
# Control flow — if/elif/else + and/or/not
def categorize_engineer(years: int) -> str:
    if years < 1:
        return "Intern"
    elif years < 3:
        return "Junior"
    elif years < 6:
        return "Mid"
    elif years < 10:
        return "Senior"
    else:
        return "Staff"
    
print(categorize_engineer(0)) 
print(categorize_engineer(2))
print(categorize_engineer(5))
print(categorize_engineer(8))
print(categorize_engineer(15))

print("-------")
# boolean operators
def can_apply_to_role(years_experience: int, has_degree: bool, is_remote_friendly: bool) -> bool:
    return years_experience >= 5 and (has_degree or years_experience >= 8) and is_remote_friendly

print(can_apply_to_role(5, True, True))    # should be True
print(can_apply_to_role(5, True, False))   # should be False (not remote)
print(can_apply_to_role(8, False, False))  # should be False (not remote)
print(can_apply_to_role(3, True, True))    # should be False (not enough experience)

print("-------")
# The match statement (Python's switch, but better)
def permission_level(role: str) -> str:
    match role:
        case "admin":
            return "full access"
        case "editor":
            return "can read and write"
        case "viewer":
            return "can read only"
        case _:
            return "no access"

print(permission_level("admin"))
print(permission_level("editor"))
print(permission_level("viewer"))
print(permission_level("unknown"))

print("-------")
# Wrap-up program
team = [
    {"name": "Selene", "role": "Director of Engineering", "years_experience": 30},
    {"name": "Nikki", "role": "Product Manager", "years_experience": 15},
    {"name": "Vi", "role": "Developer", "years_experience": 10},
    ]

def team_analyzer(team: list[dict]) -> tuple:
    senior_count: int = 0
    years_combined: int = 0
    
    for member in team:
        category = categorize_engineer(member["years_experience"])

        if category in ("Senior", "Staff"):
            senior_count += 1

        years_combined += member["years_experience"]

    avg_years_between_team: float = years_combined / len(team)

    return senior_count, avg_years_between_team

senior_count, avg_years_between_team = team_analyzer(team)


print(f'Seniors: {senior_count}')
print(f'Average years: {avg_years_between_team:.1f}')

def print_team_summary(team: list[dict]) -> None:
    for member in team:
        member_name: str = member["name"]
        member_role: str = member["role"]
        member_category: str = categorize_engineer(member["years_experience"])
        member_years_exp: int = member["years_experience"]
        
        print(f'{member_name} - {member_role} ({member_category}, {member_years_exp} years)')

print_team_summary(team)