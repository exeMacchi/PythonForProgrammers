class BankAccount:
    def __init__(self, owner, balance):
        self.__owner = owner
        self.__balance = balance
    
    
    def to_deposit(self, deposit):
        if deposit > 0:
            self.__balance += deposit
            print(f"Your new balance: ${self.__balance}")
            print("Press 'Enter' to continue...")
            input()
    
    
    def to_withdraw(self, withdraw):
        if withdraw > 0:
            if (self.__balance - withdraw) >= 0:
                self.__balance -= withdraw
                print(f"Your new balance: ${self.__balance}")
                print("Press 'Enter' to continue...")
                input()
            else:
                print(f"Error: can't withdraw more money than is in the account.")
                print("Press 'Enter' to continue...")
                input()
    
    
    def show_balance(self):
        print(f"Your current balance: ${self.__balance}")
        print("Press 'Enter' to continue...")
        input()
