# Function to save passwords to file
def save_passwords(passwords):
    with open("passwords.txt", "w") as file:
        for account, password in passwords.items():
            file.write(f"{account}: {password}\n")


# Function to load passwords from file
def load_passwords():
    try:
        with open("passwords.txt", "r") as file:
            passwords = {}
            for line in file:
                account, password = line.strip().split(": ")
                passwords[account] = password
    except FileNotFoundError:
        passwords = {}  # If file not found, return an empty dictionary
        print('No such file "passwords.txt" found')
    return passwords


# Load existing passwords from file
psw_list = load_passwords()

while True:
    mode = input("Do you want to add, view, change or remove passwords?q to quit: ")
    if mode == "add":
        new_psw_account = input("What is the account name?: ")
        if new_psw_account in psw_list:
            print("Account already exists with the same password. Please choose a different account name or password.")
            continue
        if len(new_psw_account) < 4:
            print("Too few characters, use at least 4")
            continue
        elif len(new_psw_account) > 12:
            print("Too many characters, use 12 or less")
            continue
        new_psw = input("What is the password for the account?: ")
        if not new_psw.isdigit():
            print("Invalid password, only use numbers")
            continue
        psw_list[new_psw_account] = new_psw
        save_passwords(psw_list)
    elif mode == "view":
        print(psw_list)
    elif mode == "change":
        change_psw_acc = input("Which account's password would you like to change: ")
        if change_psw_acc in psw_list:
            new_psw = input("To what password would you like to change?: ")
            if not new_psw.isdigit():
                print("Invalid password, only use numbers")
                continue
            psw_list[change_psw_acc] = new_psw
            save_passwords(psw_list)
        else:
            print("Account not found. Please enter a valid account name.")
    elif mode == "remove":
        del_psw_account = input("Which account do you want to remove?: ")
        if del_psw_account in psw_list:
            psw_list.pop(del_psw_account)
            save_passwords(psw_list)
    elif mode == "q":
        quit()