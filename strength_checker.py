import re

def check_password_strength(password):
    # List to store all security issues found
    issues = []

    # Check minimum length requirement
    if len(password) < 8:
        issues.append("Password is shorter than 8 characters")
    # Check for uppercase letters
    if not re.search("[A-Z]", password):
        issues.append("No uppercase letters")
    # Check for lowercase letters
    if not re.search("[a-z]", password):
        issues.append("No lowercase letters")
    # Check for numbers
    if not re.search("[0-9]", password):
        issues.append("No numbers")
    # Check for special characters (anything that's not a letter or number)
    if not re.search("[^A-Za-z0-9]", password):
        issues.append("No special characters")

    # Determine strength: Strong (0 issues), Medium (1-2 issues), Weak (3+ issues)
    strength = "Strong" if not issues else "Medium" if len(issues) <= 2 else "Weak"
    return strength, issues