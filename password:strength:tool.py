import re

def assess_password_strength(password):
    
    feedback = []
    length_criteria = len(password) >= 8
    uppercase_criteria = any(char.isupper() for char in password)
    lowercase_criteria = any(char.islower() for char in password)
    digit_criteria = any(char.isdigit() for char in password)
    special_char_criteria = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

    # Check criteria and provide feedback
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not uppercase_criteria:
        feedback.append("Password should include at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Password should include at least one lowercase letter.")
    if not digit_criteria:
        feedback.append("Password should include at least one digit.")
    if not special_char_criteria:
        feedback.append("Password should include at least one special character (!@#$%^&* etc.).")

    # Determine strength based on the number of criteria met
    criteria_met = sum([length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, special_char_criteria])
    if criteria_met == 5:
        strength = "Strong"
    elif 3 <= criteria_met < 5:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, feedback


def main():
    print("Password Strength Assessment Tool")
    
    while True:
        password = input("\nEnter a password to assess (or type 'exit' to quit): ").strip()
        if password.lower() == "exit":
            print("Goodbye!")
            break
        
        strength, feedback = assess_password_strength(password)
        print(f"\nPassword Strength: {strength}")
        if feedback:
            print("Suggestions to improve your password:")
            for suggestion in feedback:
                print(f"- {suggestion}")


if __name__ == "__main__":
    main()
