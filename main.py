import re

def check_password_strength(password):
    # Initialize criteria tracking
    score = 0
    feedback = []
    
    # 1. Check Length
    if len(password) >= 12:
        score += 1
    elif len(password) >= 8:
        feedback.append("• Increase length to 12+ characters for maximum security.")
    else:
        feedback.append("• Critical: Password must be at least 8 characters long.")
        
    # 2. Check Uppercase Letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("• Add at least one uppercase letter (A-Z).")
        
    # 3. Check Lowercase Letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("• Add at least one lowercase letter (a-z).")
        
    # 4. Check Digits
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("• Add at least one number (0-9).")
        
    # 5. Check Special Characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("• Add at least one special character (e.g., !, @, #, $, %).")

    # Determine strength rating based on final score
    if len(password) < 8:
        strength = "Very Weak (Too Short)"
    elif score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"
        
    return strength, score, feedback


def main():
    print("=" * 40)
    print("     PASSWORD STRENGTH CHECKER     ")
    print("=" * 40)
    
    user_password = input("Enter a password to test: ").strip()
    
    if not user_password:
        print("\n[!] Error: Password cannot be blank.")
        return
        
    strength, score, feedback = check_password_strength(user_password)
    
    print("\n" + "-" * 40)
    print(f"Results for: {user_password}")
    print(f"Strength Rating : {strength}")
    print(f"Criteria Score  : {score}/5")
    print("-" * 40)
    
    if feedback:
        print("\nSuggestions to improve your password:")
        for tip in feedback:
            print(tip)
    else:
        print("\n🎉 Excellent! Your password meets all security recommendations.")
    print("=" * 40)

if __name__ == "__main__":
    main()
