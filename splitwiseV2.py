# Dictionary to store groups and users within them (users start with 0 expenses)
groups = {}
debts = {}  # Dictionary to track who owes whom

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
    """Function to add and split expenses among selected users within a group"""
    group_name = input("Enter the group name: ")

    if group_name not in groups:
        print(f"Group '{group_name}' does not exist.")
        return get_main_choice()

    payer = input("Enter the name of the user who paid: ")

    if payer not in groups[group_name]:
        print(f"User '{payer}' not found in group '{group_name}'. Please add them first.")
        return get_main_choice()

    amount = float(input(f"Enter the total amount paid by {payer}: "))

    print("\nSelect users to split the amount (Enter 'done' to finish selecting):")
    selected_users = []

    for user in groups[group_name]:
        print(f"- {user}")

    while True:
        member = input("Enter user to split with: ")
        if member.lower() == "done":
            break
        if member in groups[group_name]:
            selected_users.append(member)
        else:
            print(f"User '{member}' not found in group '{group_name}'. Please enter a valid user.")

    if not selected_users:
        print("No users selected for splitting. Expense not recorded.")
        return get_main_choice()

    split_amount = amount / len(selected_users)

    # Update expenses for selected users
    for user in selected_users:
        groups[group_name][user] += split_amount

        # Update debts (who owes whom)
        if user != payer:
            if user not in debts:
                debts[user] = {}
            if payer not in debts[user]:
                debts[user][payer] = 0
            debts[user][payer] += split_amount

    print(f"Amount {amount} split among {len(selected_users)} users. Each owes {split_amount:.2f}")

    return get_main_choice()

def display_debts():
    """Function to display who owes whom"""
    print("\nOutstanding Balances (Who Owes Whom):")
    
    if not debts:
        print("No outstanding debts.")
        return get_main_choice()

    for debtor, creditors in debts.items():
        for creditor, amount in creditors.items():
            print(f"{debtor} owes {creditor}: {amount:.2f}")

    return get_main_choice()

def get_main_choice():
    """Function to display the menu and handle user choices"""
    print("\nMain Menu")
    print("1. Add Group")
    print("2. Add User to Group")
    print("3. Display User Specific Transactions")
    print("4. Display All Users and Groups")
    print("5. Add and Split Expenses")
    print("6. Display Who Owes Whom")
    print("7. Exit")

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
            return display_debts()
        case "7":
            print("Exiting the program.")
            return exit()
        case _:
            print("Invalid choice. Please try again.")
            return get_main_choice()

# Start the program
get_main_choice()
