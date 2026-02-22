import random
import string

def define_character_set(choice):
    """
    Returns the character set based on user's complexity choice.
    """
    specific_symbols = "@!$,.*#&"
    if choice == 1:
        return string.ascii_letters
    elif choice == 2:
        return string.ascii_letters + string.digits
    else:  # Defaults to full complexity for invalid or no choice
        return string.ascii_letters + string.digits +  specific_symbols

def create_random_password(length, char_set):
    """
    Generates the password string from the specified character set.
    """
    if length <= 0:
        return ""
    
    password = ''.join(random.choice(char_set) for _ in range(length))
    return password

def run_password_tool():
    """
    Main function to guide the user and generate a password.
    """
    print("Welcome to the Secure Password Tool! 🔐")
    
    # 1. Get password length
    try:
        password_length = int(input("\nEnter the desired password length (4-16): "))
        if not 4 <= password_length <= 16:
            print("Password length should be between 4 and 16.")
            return
    except ValueError:
        print("Error: Please enter a valid number.")
        return

    # 2. Get complexity choice
    print("\nHow complex should the password be?")
    print("1. Letters only")
    print("2. Letters & Numbers")
    print("3. Letters, Numbers & Symbols (Recommended)")
    
    try:
        user_choice = int(input("Your choice (1/2/3): "))
    except ValueError:
        print("Invalid choice. Defaulting to full complexity.")
        user_choice = 3

    # 3. Generate and display
    character_set = define_character_set(user_choice)
    new_password = create_random_password(password_length, character_set)

    print(f"\nGenerated Password: {new_password}")

if __name__ == "__main__":
    run_password_tool()
       