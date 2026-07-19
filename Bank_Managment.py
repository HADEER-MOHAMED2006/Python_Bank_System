users = {}
current_user = None
login_attempts = 3


def register():
    username = input("Enter the new username : ")
    if username == "":
        print("Username can't be empty")
        return
    elif username in users:
        print("This username is already exist.")
        return

    password = input("Enter the new password : ")
    if password == "":
        print("Password can't be empty")
        return
    elif len(password) < 6:
        print("Password must be 6 letters or more.")
        return
    users[username] = {
        "Password": password,
        "Balance": 0,
        "last_transaction": "No transactions yet",
    }
    print("Account created successfully.")


def login():
    global current_user
    attempts = login_attempts
    while attempts > 0:
        username = input("Enter your username (0 => Login canceled): ")
        if username == "0":
            print("Login is canceled.")
            return
        if username == "":
            print("Username can't be empty")
            attempts -= 1
            print(f"Error, Try again. {attempts} left attempts")
            continue
        elif username not in users:
            print("This username is not exist.")
            attempts -= 1
            print(f"Error, Try again. {attempts} left attempts")
            continue

        password = input("Enter your password : ")
        if password == "0":
            print("Login is canceled.")
            return
        if password == "":
            print("Password can't be empty")
            attempts -= 1
            print(f"Error, Try again. {attempts} left attempts")
            continue
        elif password != users[username]["Password"]:
            print("Wrong password!")
            attempts -= 1
            print(f"Error, Try again. {attempts} left attempts")
            continue

        else:
            print(f"Welcome Back {username}")
            current_user = username
            bank_menu()
            return

    print("The attempts finished.")


def check_balance():
    print(f"Your Balance: ${users[current_user]['Balance']}")



def deposit():
    amount = input("Enter the amount (0 or less => canceled): ")
    if not amount.isdigit():
        print("Invalid amount!")
        return
    else:
        amount = int(amount)

    if amount <= 0:
        print("Operation canceled")
    else:
        users[current_user]['Balance'] += amount
        users[current_user]["last_transaction"] = "Deposit"
        print(f"$ {amount} deposited successfully.")
        print(f"Current Balance : {users[current_user]['Balance']}")


def withdraw():
    amount = input("Enter the amount (0 or less => canceled): ")
    if not amount.isdigit():
        print("Invalid amount!")
        return
    else:
        amount = int(amount)

    if amount <= 0:
        print("Operation canceled")
    elif amount > users[current_user]["Balance"]:
        print(f"You have only ${users[current_user]['Balance']}")
    else:
        users[current_user]['Balance'] -= amount
        users[current_user]["last_transaction"] = "Withdraw"
        print(f"successfully withdrawed ${amount}.")
        print(f"Current Balance : {users[current_user]['Balance']}")

def transfer():
    recipient = input("Enter the recipient (0 => canceled): ")
    if recipient == "0":
        print("Operation cancelled.")
        return
    if recipient == "":
        print("Usrname can't be empty.")
        return
    if recipient not in users:
        print("This user doesn't exist.")
        return
    if recipient == current_user:
        print("Can't transfer to the same account.")
        return
    
    amount = input("Enter the amount : ")
    if amount == "0":
        print("Operation cancelled.")
        return
    if not amount.isdigit():
        print("Invalid input!")
        return
    amount = int(amount)
    if amount <= 0:
        print("Amount must be greater than zero.")
        return
    if amount > users[current_user]["Balance"]:
        print("Insufficient balance.")
        return
    users[current_user]["Balance"] -= amount
    users[recipient]["Balance"] += amount
    users[current_user]["last_transaction"] = f"Transfer of ${amount} to {recipient}"
    users[recipient]["last_transaction"] = f"Received ${amount} from {current_user}"
    print("Transfer successful!")
    

def change_password():
    current_pass = input("Enter current password (0 => canceled): ").strip()
    if current_pass == "0":
        print("Operation cancelled.")
        return
    if current_pass != users[current_user]["Password"]:
        print("Incorrect current password.")
        return
    new_pass = input("Enter new password (0 to cancel): ").strip()
    if new_pass == "0":
        print("Operation cancelled.")
        return
    if len(new_pass) < 6:
        print("New password must be at least 6 characters.")
        return
    users[current_user]["Password"] = new_pass
    print("Password changed successfully!")



def change_username():
    global current_user
    new_username = input("Enter new username (0 => canceled): ").strip()
    if new_username == "0":
        print("Operation cancelled.")
        return
    if new_username == "":
        print("Username cannot be empty.")
        return
    if new_username in users:
        print("Username already exists.")
        return
    users[new_username] = users.pop(current_user)
    print(f"Username changed successfully to {new_username}!")
    current_user = new_username



def show_last_transaction():
    print(f"Last Transaction: {users[current_user]['last_transaction']}")



def bank_menu():
    print("=" * 20, " Bank Menu ", "=" * 20)
    print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Transfer\n5. Change Password\n6. Change Username\n7.Show Last Transaction\n8. Logout")
    choice = input("choose an option : ")
    if not choice.isdigit():
        print("Invalid input!")
        return
    else:
        choice = int(choice)

    global current_user

    if choice == 1:
        check_balance()
    elif choice == 2:
        deposit()
    elif choice == 3:
        withdraw()
    elif choice == 4:
        transfer()
    elif choice == 5:
        change_password()
    elif choice == 6:
        change_username()
    elif choice == 7:
        show_last_transaction()
    elif choice == 8:
        print("Logout successfully.")
        current_user = None
        return



def main():
    while True:
        print("\n========== Welcome To Python Bank ==========")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Thank you for using Python Bank. Goodbye!")
            break
        else:
            print("Invalid menu choice.")

main()