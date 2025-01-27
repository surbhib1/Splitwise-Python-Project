from pickle import NONE

usernames = []

def adduser1():
  user = int(input("Enter the number of users: "))
  print(f"Number of users: {user}")
  for i in range(user):
    username = input(f"Enter the name of user {i + 1}: ")
    usernames.append(username)
  print("\nAll Users:")
  for i, username in enumerate(usernames, start=1):
        print(f"User {i}: {username}")
  return get_main_choice()
 # return None

def displayuser1():
          name = input("Enter username :")
          print(name)
          if name in usernames:
            print("User found")
          else:
            print("User not found")
          print("Total users are")
          for i, username in enumerate(usernames, start=1):
              print(f"User {i}: {username}")
          return None

def displayall1():
  return None

def addexpenses1():
  return None


def get_main_choice():
    print("1. Add User")
    print("2. Display User specific transaction")
    print("3. Display All Transactions")
    print("4. Add Expenses")
    print("5. Exit")

    choice = input("Enter your choice: ")
    match choice:
        case "1":
            return adduser1()
        case "2":
            return displayuser1()
        case "3":
            return displayall1()
        case "4":
           #print("1. Enter name of the user who performed transactions")
           #print("2. Enter name of the user who owes money")
           #print("3. Enter amount")
           #print("4. ")
           #print("5. Exit")
            return addexpenses1()
        case "5":
            return exit

        case _:
            print("Invalid choice. Please try again.")
            return exit

result = get_main_choice()
print(result)

#def adduser():
  #return "Add User
