# Class
class User:
    def __init__(self, name: str, email: str, years_experience: int):
        self.name = name
        self.email = email
        self.years_experience = years_experience

    def greet(self) -> str:
        return f"Hi, I'm {self.name}"
    
    def is_senior(self) -> bool:
        return self.years_experience >= 5
    
    # Methods that change instance state
    def update_email(self, new_email: str) -> None: 
        self.email = new_email

    def gain_experience(self, years: int = 1) -> None:
        self.years_experience += years

    def promote_to_senior(self) -> None:
        if self.is_senior():
            return
        
        self.years_experience = 5

if __name__ == "__main__":
    test = User("Test", "Test@example.com", 3)
    print(test.greet())
    print(test.is_senior())