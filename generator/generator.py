import random

class generate:
    def __init__(self):
        self.first_names = ["Patrick", "Angus", "Oliver", "William", "Noah", "Liam"]
        self.last_names = ["Stewart", "Miller", "Johson", "Willson", "Moore", "Davis"]
        self.emails = ["proton.me", "gmail.com", "mail.proton.me", "outlook.com.au", "outlook.com"]

    def name(self):
        first_name = random.choice(self.first_names)
        last_name = random.choice(self.last_names)
        return f"{first_name} {last_name}"
    
    def email(self, name=None):
        if name is None:
            name = self.name()
        name = name.replace(" ", ".").lower()
        email = random.choice(self.emails)
        return f"{name}@{email}"
    
    def phone(self):
        area_code = random.randint(100, 999)
        first_part = random.randint(100, 999)
        second_part = random.randint(1000, 9999)
        return f"({area_code}) {first_part}-{second_part}"
