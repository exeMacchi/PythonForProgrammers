# 2) Create a class called "BankAccount" that has attributes "owner" and "balance". 
#    Add methods called "deposit" and "withdraw" that allow the balance to be modified. 
#    Make sure that you can't withdraw more money than is in the account. Then, create 
#    an object of type "BankAccount" and perform some deposit and withdrawal operations.
from bank_account import BankAccount
from functions import ask_name, initial_deposit, show_menu, ask_deposit, ask_withdraw

def main():
    bank_user = BankAccount(ask_name(), initial_deposit())

    op = 0
    while True:
        if op == 0:
            op = show_menu()

        elif op == 1:
            bank_user.show_balance()
            op = 0

        elif op == 2:
            bank_user.to_deposit(ask_deposit())
            op = 0

        elif op == 3:
            bank_user.to_withdraw(ask_withdraw())
            op = 0
        
        elif op == 4:
            print("Exiting the program...")
            break


if __name__ == '__main__':
    main()
