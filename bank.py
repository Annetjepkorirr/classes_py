# class Account:
#     interestrate = 400.0
    
# def __init__(self,account_name,account_number,balance):
#     self.account_name=account_name
#     self.account_number = account_number
#     self.balance = balance
    
# def withdraw(self):
#     return f" The bank account under the name {self.account_name} has withdrwn some cash"

# def deposit(self, amount):
#     balance+=amount
#     return f"You have deposited{amount} and your balance is{sel}"

# def balance(self):
#     return f"My balance in my account amounts to{self.balance}"




# Create a file in the classes directory, bank.py. Define the following classes 
# in the module respectively. 
# Account
# The class should have one class attribute and three instance variables.

# Add attributes deposits and withdrawals in the init method which are empty lists 
# by default and another attribute loan_balance which is zero by default.    

# Add a method check_balance which returns the account’s balance

# Update the deposit method to append each withdrawal transaction to the deposits list. Each 
# transaction should be in the form of a dictionary like this  
# {
#    "amount": amount,
#    "narration": “deposit”
# }

# Update the withdrawal method to append each withdrawal transaction to the withdrawals list. Each 
# transaction should be in the form of a dictionary like like this 
# {
#    "amount": amount,
#    "narration": “withdrawal”
# }

# Add a new method  print_statement which combines both deposits and withdrawals into one list and, 
# using a for loop, prints each transaction in a new line like this
# deposit - 1000
# withdrawal - 500


# Add a borrow_loan method which allows a customer to borrow if they meet these conditions:
# Account has no outstanding loan
# Loan amount requested is more than 100
# Customer has made at least 10 deposits.
# Amount requested is less than or equal to 1/3 of their total sum of all deposits.
# A successful loan increases the loan_balance by requested amount


# Add a repay_loan method with this functionality
# A customer can repay a loan to reduce the current loan_balance
# Overpayment of a loan increases the acots current balance







  
class Account:
    def __init__(self,account_name):
        self.account_name = account_name
        self.balance = 0
        self.deposits =[]
        self.withdrawals =[]
        loan_balance = 0
        
    def deposit(self,amount):
        self.balance +=amount
        transaction={
            "amount": amount,
            "narration":"deposit"
            
        }
        self.deposits.append(transaction)
        return f"You have deposited {amount} your new balance is {self.balance}"
      
    def withdraw(self,amount):
        if self.balance <=amount :
            self.balance -= amount
            return f" You have withdrawn {amount} your new balance is {self.balance} "
        else:
            f"Your balance is {self.balance} you cannot withdraw {amount}"
            
        transaction ={
                "amount":amount,
                "narration":"deposit"
            }
             
        self.withdrawals.append(transaction)
            
            
            
    def check_balance(self):
        return f" Your balance is {self.balance}"
    
    def print_statement(deposits, withdrawals):
        transaction = self.deposits + self.withdrwals
        for transaction in transactions:
            print(f"transaction['narration'] - transaction['amount']")
            
    def borrow_loan(self, amount):
        if self.loan_balance == 0 and amount > 100 and len(self.deposits) >= 10 and amount <= self.total_deposits() / 3:
            self.loan_balance += amount
        else:
            print("Loan not approved")
        account.borrow_loan(200)   
        
        
    def repay_loan(self,amount):
        if self.loan_balance > 0:
            if amount <= self.loan_balance:
                self.loan_balance -= amount
                print("THe loan repayment is successful!")
            else:
                overpayment = amount - self.loan_balance
                self.loan_balance = 0
                self.balance += overpayment
                print("Overpaid loan")
        else:
            print("There is nooutstanding loan to repay.")        
        
                            



