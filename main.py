import re
import random
import string

def check_password_strength(password):
    score = 0

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        print("❌ Password should be at least 8 characters long.")

    # Uppercase & Lowercase
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        print("❌ Include both uppercase and lowercase letters.")

    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        print("❌ Add at least one number (0-9).")

    # Special Characters
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        print("❌ Include at least one special character (!@#$%^&*).")

    # Common Weak Passwords
    weak_passwords = ["password", "12345678", "qwerty", "password123", "admin"]
    if password.lower() in weak_passwords:
        print("❌ This is a commonly used password. Choose something more secure.")
        score = 0  # Force weak if it's common

    # Strength Rating
    if score == 4:
        print("✅ Strong Password!")
    elif score == 3:
        print("⚠️ Moderate Password - Consider adding more security features.")
    else:
        print("❌ Weak Password - Improve it using the suggestions above.")

# Password Generator (Optional Feature)
def suggest_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(length))

# Main Program
user_choice = input("Check (C) a password or Suggest (S) a strong password? ").lower()

if user_choice == 'c':
    password = input("Enter your password: ")
    check_password_strength(password)
elif user_choice == 's':
    strong_password = suggest_password()
    print("🔐 Suggested Strong Password:", strong_password)
else:
    print("Invalid option.")