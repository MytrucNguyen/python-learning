import asyncio
import time

# try/except — Python's try/catch
try:
    10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")


test_dict = {"name": "test"}
try:
    test_dict["age"]
except KeyError:
    print("Item in object does not exist")

try:
    int("hello")
except Exception as error:
    print(f"Something went wrong: {error}")

print("--------")
# Raising your own errors
def withdraw_from_account(balance: float, amount: float) -> float:
    if amount <= 0:
        raise ValueError("Withdrawal amount must be positive")
        
    if amount > balance:
        raise ValueError("Insufficient funds")    
    
    return balance - amount
    
print(withdraw_from_account(200.00, 100.00))

try:
    print(withdraw_from_account(200.00, -1.0))
except ValueError as err:
    print(f"Error: {err}")

try:
    print(withdraw_from_account(200.00, 300.00))
except ValueError as err:
    print(f"Error: {err}")

print("--------")
# async function
async def fetch_user(user_id: int) -> dict:
    await asyncio.sleep(1)
    return {
    "id": user_id,
    "name": f"User_{user_id}",
    }

result = asyncio.run(fetch_user(42))
print(result)

print("--------")
# Multiple async operations in parallel
async def main():
    user1, user2, user3 = await asyncio.gather(fetch_user(1), fetch_user(2), fetch_user(3))
    print(user1, user2, user3)

start = time.time()
asyncio.run(main())
print(f"Total time: {time.time() - start:.2f} seconds")