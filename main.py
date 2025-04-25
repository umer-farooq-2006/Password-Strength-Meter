import streamlit as st
import re
import random
import string

# Function to check password strength
def check_password_strength(password):
    score = 0
    messages = []

    if len(password) >= 8:
        score += 1
    else:
        messages.append("❌ Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        messages.append("❌ Include both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        messages.append("❌ Add at least one number (0-9).")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        messages.append("❌ Include at least one special character (!@#$%^&*).")

    weak_passwords = ["password", "12345678", "qwerty", "password123", "admin"]
    if password.lower() in weak_passwords:
        messages.append("❌ This is a commonly used password. Choose something more secure.")
        score = 0

    return score, messages

# Function to suggest strong password
def suggest_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(length))

# Streamlit App UI
st.title("🔐 Password Strength Checker")

option = st.radio("Choose an option:", ["Check Password", "Suggest Password"])

if option == "Check Password":
    password = st.text_input("Enter your password", type="password")
    if password:
        score, messages = check_password_strength(password)
        for msg in messages:
            st.error(msg)
        if score == 4:
            st.success("✅ Strong Password!")
        elif score == 3:
            st.warning("⚠️ Moderate Password - Consider improving it.")
        else:
            st.error("❌ Weak Password - Follow suggestions above.")
elif option == "Suggest Password":
    length = st.slider("Password length", min_value=8, max_value=24, value=12)
    st.write("🔐 Suggested Strong Password:")
    st.code(suggest_password(length))
