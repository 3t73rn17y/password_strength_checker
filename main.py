# Import functions from other modules
from strength_checker import check_password_strength
from report import generate_report

def main():
    # Display application header
    print("- -" * 20)
    print("Password Strength Checker")
    print("- -" * 20)
    
    # Main program loop - runs until user quits
    while True:
        # Get password input from user
        password = input("\nEnter a password to check (or 'quit' to exit):\n> ")
        
        # Check if user wants to exit
        if password.lower() in ['quit', 'exit', 'q']:
            print("\nGoodbye!")
            break
        
        # Skip empty input
        if not password:
            print("Please enter a password.")
            continue
        
        # Check password strength and get results
        strength, issues = check_password_strength(password)
        # Display results
        print(f"\nPassword Strength: {strength}")
        print(generate_report(strength, issues))
        print("=" * 50)

# Run the program when executed directly
if __name__ == "__main__":
    main()