print("-------")
# First list
tech_stack: list[str] = ["TypeScript", "Python", "JavaScript", "Flutter"]

print(tech_stack)
print(tech_stack[0])
print(tech_stack[-1])
print(len(tech_stack))

print("-------")
# Modify the list
tech_stack.append("React Native")
tech_stack.pop(0)
tech_stack.insert(1, "Go")

print(tech_stack)

print("-------")
# Slicing
print(tech_stack[0:2])    # "Python", "Go", 
print(tech_stack[1:])     # "Go", "JavaScript", "Flutter", "React Native"
print(tech_stack[:2])     # "Python", "Go", 
print(tech_stack[-2:])    # "FLutter", "Reactive Native"
print(tech_stack[::-1])   # React Native', 'Flutter', 'JavaScript', 'Go', 'Python'

print("-------")
# Dict
user = {
    "name" : "Hello World",
    "role" : "Developer",
    "years_experience" : 5,
    "is_remote": False,
}

print(user)
print(user["name"])
print(user["role"])
print(user.keys())
print(user.values())

print("-------")
# Modify and access dicts
user["company"] = "Microsoft"
user["years_experience"] = 6
del user["is_remote"]

print(user.get("is_remote"))

print("-------")
# Looping through dicts
for key in user:
    print(key)

for value in user.values():
    print(value)

for key, value in user.items():
    print(f'{key}: {value}')

print("-------")
# A list of dicts
teams = [
    {"name" : "Jane Doe", "role" : "PM", "years_experience" : 10},
    {"name" : "John Doe", "role" : "QA", "years_experience" : 2},
    {"name" : "Ash Ketchum", "role" : "Traveler", "years_experience" : 30}
]

print(teams)
print(teams[1]["name"])

for user in teams:
    print(f'{user["name"]} - {user["role"]}')

count = 0
for user in teams:
    if user["years_experience"] > 3:
        count += 1

print(count)

# List comprehensions (Python's superpower)
# List of just the names:
names = [ user["name"] for user in teams ]

print(names)

seniors = [ user["name"] for user in teams if user["years_experience"] > 3]

print(seniors)
