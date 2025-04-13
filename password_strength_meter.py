import streamlit as st
import re

def check_password_strength(password):
    score = 0
    feedback = []
    
    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")
    
    # Strength Rating
    if score == 4:
        feedback.append("✅ Strong Password!")
    elif score == 3:
        feedback.append("⚠️ Moderate Password - Consider adding more security features.")
    else:
        feedback.append("❌ Weak Password - Improve it using the suggestions above.")

    return feedback

# streamlit ui
#password = input("Enter your password: ")
#check_password_strength(password)

st.title("Password strength Meter")
st.write("Enter your Passwordto check its strenght")

user_name = st.text_input("Enter your username")
password = st.text_input("Enter your password", type="password")

if st.button("Check password strength"):
    result = check_password_strength (password)
    for line in result :
        st.write(line)
#result = enter_your_password (value, unit_from, unit_to)


