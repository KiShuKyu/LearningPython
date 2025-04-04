# password checker

password = "LearningPython123"

if len(password) <= 6:
    print("Your Password is too weak.")
elif 7 <= len(password) <= 10:
    print("Your Password is Medium.")
elif len(password) >= 11:
    print("Your password is quite strong.")

# or (better)
if len(password) <= 6:
    strength = "Weak"
elif 7 <= len(password) <= 10:
    strength = "medium"
elif len(password) >= 11:
    strength = "Strong"

print(f"Password strength is: {strength}")
