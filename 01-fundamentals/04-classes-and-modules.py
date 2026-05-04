from user import User

user = User("Jane Doe", "janedoe@fake.com", 5)
print("-------")
print(user.greet())
print(user.is_senior())

print("-------")
print(f"Email: {user.email}, Years: {user.years_experience}")

user.update_email("jane.new@example.com")
user.gain_experience()
user.gain_experience(3)

print(f"Email: {user.email}, Years: {user.years_experience}")

print("-------")
user2 = User("John Doe", "JD@example.com", 2)
print(f"Are they a senior: {user2.is_senior()}")

user2.promote_to_senior()
print(f"Are they a senior: {user2.is_senior()}")
print(f"Year's of experience: {user2.years_experience}")
