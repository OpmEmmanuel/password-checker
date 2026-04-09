import re

def check_password(password):
    score = 0

    # Length check
    if len(password) >= 8:
        score += 1

    # Uppercase check
    if re.search(r"[A-Z]", password):
        score += 1

    # Number check
    if re.search(r"[0-9]", password):
        score += 1

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    # Strength rating
    if score == 4:
        return "Strong"
    elif score == 3:
        return "Medium"
    else:
        return "Weak"

password = input("Enter a password: ")
result = check_password(password)

print("Password strength:", result)