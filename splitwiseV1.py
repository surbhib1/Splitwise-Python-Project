# Dictionary to store groups and users within them (users start with 0 expenses)
groups = {}

def add_group():
    """Function to add a new group"""
    group_name = input("Enter the group name: ")
    
    if group_name in groups:
        print(f"Group '{group_name}' already exists.")
    else:
        groups[group_name] = {}  # Create an empty dictionary for users in the group
        print(f"Group '{group_name}' added successfully.")

    return get_main_choice()

def add_user():
    """Function to add users under a group"""
    group_name = input("Enter the group name to add users: ")

    if group_name not in groups:
        print(f"Group '{group_name}' does not exist. Please add the group first.")
        return get_main_choice()

    num_users = int(input("Enter the number of users: "))

    for i in range(num_users):
        username = input(f"Enter the name of user {i + 1}: ")
        
        if username in groups[group_name]:
            print(f"User '{username}' already exists in '{group_name}'.")
        else:
            groups[group_name][username] = 0  # Default expense is 0
            print(f"User '{username}' added to group '{group_name}'.")

    display_all_users()
    return get_main_choice()

def display_user():
    """Function to check if a user exists in a group and show their expenses"""
    group_name = input("Enter the group name: ")

    if group_name not in groups:
        print(f"Group '{group_name}' does not exist.")
        return get_main_choice()

    username = input("Enter username: ")

    if username in groups[group_name]:
        print(f"User '{username}' found in '{group_name}' with total expenses: {groups[group_name][username]}")
    else:
        print(f"User '{username}' not found in group '{group_name}'.")

    return get_main_choice()

def display_all_users():
    """Function to display all groups, users, and their expenses"""
    print("\nAll Groups, Users, and Their Expenses:")

    if not groups:
        print("No groups found.")
        return

    for group, users in groups.items():
        print(f"\nGroup: {group}")
        if not users:
            print("  No users in this group.")
        else:
            for username, expense in users.items():
                print(f"  {username}: Expenses: {expense}")

def add_expenses():
    """Function to add expenses to a user within a group"""
    group_name = input("Enter the group name: ")

    if group_name not in groups:
        print(f"Group '{group_name}' does not exist.")
        return get_main_choice()

    username = input("Enter the username to add expenses: ")

    if username in groups[group_name]:
        amount = float(input(f"Enter the amount to add for {username}: "))
        groups[group_name][username] += amount  # Add expense to the user
        print(f"Updated expenses for {username} in '{group_name}': {groups[group_name][username]}")
    else:
        print(f"User '{username}' not found in group '{group_name}'. Please add them first.")

    return get_main_choice()

def get_main_choice():
    """Function to display the menu and handle user choices"""
    print("\nMain Menu")
    print("1. Add Group")
    print("2. Add User to Group")
    print("3. Display User Specific Transactions")
    print("4. Display All Users and Groups")
    print("5. Add Expenses")
    print("6. Exit")

    choice = input("Enter your choice: ")

    match choice:
        case "1":
            return add_group()
        case "2":
            return add_user()
        case "3":
            return display_user()
        case "4":
            return display_all_users(), get_main_choice()
        case "5":
            return add_expenses()
        case "6":
            print("Exiting the program.")
            return exit()
        case _:
            print("Invalid choice. Please try again.")
            return get_main_choice()

# Start the program
get_main_choice()

