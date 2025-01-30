# Dictionary to store user information (default values for expenses)
users = {}

def add_user():
    """Function to add users to the dictionary with default expense 0"""
    num_users = int(input("Enter the number of users: "))
    print(f"Number of users: {num_users}")

    for i in range(num_users):
        username = input(f"Enter the name of user {i + 1}: ")
        if username in users:
            print(f"User '{username}' already exists.")
        else:
            users[username] = 0  # Default expense is 0
    display_all_users()
    return get_main_choice()

def display_user():
    """Function to check if a user exists and display their expenses"""
    username = input("Enter username: ")

    if username in users:
        print(f"User '{username}' found with total expenses: {users[username]}")
    else:
        print("User not found.")

 #   display_all_users()
    return get_main_choice()

def display_all_users():
    """Function to display all users and their current expenses"""
    print("\nAll Users and Their Expenses:")
    if not users:
        print("No users found.")
    else:
        for i, (username, expense) in enumerate(users.items(), start=1):
            print(f"User {i}: {username}, Expenses: {expense}")

def add_expenses():
    """Function to add expenses to a user"""
    username = input("Enter the username to add expenses: ")

    if username in users:
        amount = float(input(f"Enter the amount to add for {username}: "))
        users[username] += amount  # Add expense to the user
        print(f"Updated expenses for {username}: {users[username]}")
    else:
        print("User not found. Please add the user first.")

   # display_all_users()
    return get_main_choice()

def get_main_choice():
    """Function to display the menu and handle user choices"""
    print("\nMain Menu")
    print("1. Add User")
    print("2. Display User Specific Transactions")
    print("3. Display All Users")
    print("4. Add Expenses")
    print("5. Exit")

    choice = input("Enter your choice: ")

    match choice:
        case "1":
            return add_user()
        case "2":
            return display_user()
        case "3":
            return display_all_users(), get_main_choice()
        case "4":
            return add_expenses()
        case "5":
            print("Exiting the program.")
            return exit()
        case _:
            print("Invalid choice. Please try again.")
            return get_main_choice()

# Start the program
get_main_choice()

