# Create a budget class that can instantiate an object based on Food, clothing and entertainment
class Budget:
    def __init__(self, name, amount):
        self.name=name    
        self.amount=amount

# Depositing funds to each of the categories
    def deposit (self, amount):
        print("*****Deposit*****")
        self.amount=self.amount+amount
        return f"you have deposited {amount}, your current balance for {self.name} is {self.amount}"

# Withdrawing funds from each category
    def withdraw (self, amount):
        print("*****Withdrawal*****")
        if amount>self.amount:
            return f"Insufficient funds, your balance for {self.name} is {self.amount}"
        else:
            self.amount=self.amount-amount
            return f"you have withdrawn {amount}, you have {self.amount} remaining for {self.name}"

# Computing category balance
    def balance (self):
        print("*****Check you balance*****")
        current_balance= f"Your current balance for {self.name} is {self.amount} "
        return current_balance

# Transferring Balance amounts between categories
    def balance_transfer(self,amount,recipient):
        print("*****Balance Transfer*****")
        if amount>self.amount:
            return f"Insufficient funds, your balance for {self.name} is {self.amount}"
        else:
            self.amount=self.amount-amount
            recipient.amount=recipient.amount+amount
            transaction= f'You transferred {amount} from {self.name} to {recipient.name}\n'
            transaction+= f'Your current balance for {self.name} is {self.amount}\n'
            transaction+= f'Your current balance for {recipient.name} is {recipient.amount}'
            return transaction

budgets=list()

def create_budget():
    print("*****Budget Creation*****")
    budget_name=input("Enter the name of the budget you want to create: ")
    budget_amount=int(input("Enter the amount you want to allocate to the budget: "))
    new_budget=Budget(budget_name, budget_amount)
    budgets.append(new_budget)
    print("\n\n")
    budget_app()

def choose_budget():
    if len(budgets)==0:
        print("There are currently no budget created\nCreate a budget")
        print("\n\n")
        create_budget()
    print("*****BUDGET CATEGORIES*****")
    for items in budgets:
        position=budgets.index(items)+1
        print(f"{position}: {items.name}, {items.amount}")
    
    choice= int(input("Select your preferred budget: "))
    items=budgets[choice-1]
    print("\n\n")
    budget_menu(items)

def budget_menu(items):
    print("*****Budget Menu*****")
    print(f"You have selected {items.name} Budget category ")
    print(""" What do you want to do?
    1. Deposit
    2. Withdrawal
    3. Transfer
    4. Check Balance
    5. Return to main menu
    """)
    choice=int(input("Enter your answer==> "))
    if choice==1:
        amount_to_deposit=int(input("Enter the amount you want to deposit: "))
        print(items.deposit(amount_to_deposit))
        print("\n\n")

        choose_budget()
    elif choice==2:
        amount_to_withdraw=int(input("Enter the amount you want to withdraw: "))
        print(items.withdraw(amount_to_withdraw))
        print("\n\n")
        choose_budget()
    elif choice==3:
        amount_to_transfer=int(input("Enter the amount you want to transfer: "))
        print("The following categories are available")
        
        for category in budgets:
            position=budgets.index(category)
            print(f"{position+1}. {category.name}, {category.amount}")
        choice= int(input("Select the budget you want to transfer to: "))
        category=budgets[choice-1]
        receiving_category= category
        print(items.balance_transfer(amount_to_transfer,receiving_category))
        print("\n\n")
        choose_budget()
    elif choice==4:
        print("\n\n")
        print(items.balance())
        print("\n\n")
        choose_budget()
    elif choice==5:
        print("\n\n")
        budget_app()
    else:
        print("Invalid option selected")
        print("\n\n")
        budget_menu(items)

def budget_app():
    selected_option=int(input("You can perform the following budget transactions:\nSelect '1' Create Budget\nSelect '2' to Choose a budget category\nSelect '3' to exit\n"))
    if selected_option==1:
        print("\n\n")
        create_budget()
    elif selected_option==2:
        print("\n\n")
        choose_budget()
    elif selected_option==3:
        print("Goodbye")
        print("\n\n")
        exit()
    else:
        print('invalid option selected')
        print("\n\n")
        budget_app()


budget_app()