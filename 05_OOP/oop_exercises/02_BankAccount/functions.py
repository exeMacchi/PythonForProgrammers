def ask_name():
    while True:
        try:
            name = input("Enter your name: ")
        except Exception as e:
            print(f"Error: {e}")
        else:
            if name != "":
                return name
            else:
                print("Error: name cannot be empty.")


def initial_deposit():
    while True:
        try:
            deposit = float(input("Enter the initial deposit: $"))
        except Exception as e:
            print(f"Error: {e}")
        else:
            if deposit > 100:
                return deposit
            else:
                print("Error: deposit must be greater than 100")


def show_menu():
    print("==================================")
    print("1. Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    print("==================================")
    return choose_option()


def choose_option():
    try:
        op = int(input("Choose an option: "))
    except Exception as e:
        print(f"Error: {e}")
        print("Press 'Enter' to continue...")
        input()
        return 0
    else:
        if 1 <= op <= 4:
            return op
        else:
            print("Error: invalid option.")
            print("Press 'Enter' to continue...")
            input()
            return 0
    
    
def ask_deposit():
    success = False
    while True:
        try:
            deposit = float(input("Enter the deposit: $"))
        except Exception as e:
            print(f"Error: {e}")
            print("Press 'Enter' to continue...")
            input()
            break
        else:
            if deposit > 0:
               success = True 
               break
            else:
                print("Error: deposit must be greater than 0")
                print("Press 'Enter' to continue...")
                input()
                break
    if success:
        return deposit
    else:
        return 0


def ask_withdraw():
    success = False
    while True:
        try:
            withdraw = float(input("Enter the withdraw: $"))
        except Exception as e:
            print(f"Error: {e}")
            print("Press 'Enter' to continue...")
            input()
            break
        else:
            if withdraw > 0:
               success = True 
               break
            else:
                print("Error: withdraw must be greater than 0")
                print("Press 'Enter' to continue...")
                input()
                break
    if success:
        return withdraw
    else:
        return 0
