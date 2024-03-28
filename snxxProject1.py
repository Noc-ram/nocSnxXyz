import time
import random
import string

def welcome_message(username):
    print(f"Welcome {username}!")
    time.sleep(5)

def get_username():
    while True:
        username = input("MAKE YOURSELF AN USERNAME: ")
        if len(username) < 3:
            print("Username must be at least 3 characters long.")
        elif len(username) > 20:
            print("Username must not exceed 20 characters.")
        elif not username.isalnum():
            print("Username must contain only alphanumeric characters.")
        else:
            return username

def snxx_spam():
    while True:
        print("SNXXYZ ON TOP")
        time.sleep(0.1)

def snxx_spam_rainbow():
    colors = ["\033[91m", "\033[92m", "\033[93m", "\033[94m", "\033[95m", "\033[96m"]
    while True:
        color = random.choice(colors)
        print(color + "SNXXYZ ON TOP")
        time.sleep(0.1)

def main():
    print("WELCOME USER")
    username = get_username()
    welcome_message(username)
    
    print("1. -SNXX SPAM")
    print("2. -SNXX SPAM RAINBOW")
    choice = input("Choose an option: ")
    
    if choice == '1':
        snxx_spam()
    elif choice == '2':
        snxx_spam_rainbow()
    else:
        print("Invalid choice. Please choose 1 or 2.")

if __name__ == "__main__":
    main()
