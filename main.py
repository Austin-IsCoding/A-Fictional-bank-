# BAnking Apication 
'''
Fundamental Features:
1 Create a new account
  User can create an account by providing the name of the account holder, number, etc.
  User can select the amount type (Saving or Current account).
  They can also provide an initial amount more than or equal to 500.
2 view account holders record.
  Withdraws and deposit amount with the balance inquiry.     
3. Closing an account
4. edit account details.
  He/She can modify their account detail and type if they want to.


Steps 
1. need to have a welcome message

2. Show menu and make sure its valid
MAIN MENU
1. NEW ACCOUNT
2. DEPOSIT AMOUNT
3. WITHDRAW AMOUNT { Enter acc Number && ammount}
4. BALANCE ENQUIRY
5. ALL ACCOUNT HOLDER LIST { AccuntNumber | Name  | type | Balance}
6. CLOSE AN ACCOUNT
7. MODIFY AN ACCOUNT
8. EXIT
Select Your Option (1-8)

3. There are 2 type of accounts Savings and Current 

-  Account Class
 - Type = S|C
 - Name = Owner name
 - Balance
 - transactions [] string
 : withdraw 
 : deposit
 : edit_info


- Bank 
 - Accouts Array - List of all accounts
 - Name 
 :list_all_accounts
 :close_an_account
 :modify_an_account
 :create_new_account
 :diposit 
 :withdraw
''' 
class Account:
  def __init__ (self,typeOfAcc,name,balance,number):
    self.type = typeOfAcc
    self.name = name 
    self.balance = balance
    self.transactions = []
    self.number = number

  def modify_an_account(self):
    which = input("Choose What You Want To Change Name/Type (N or T)")
    if which == "N":
      change_name = input("What Is The New Name Of The Account")
      self.name = change_name
    elif which == "T":
      change_type = input("What Type Of Account Are You Changing To S/C")
      self.type =  change_type
      
  def withdraw(self, ammount):
    # Logic to take money out of the bank 
    pass

  def diposit(self, ammount):
    # Logic to put money in of the bank 
    pass

class Bank:
  accounts = [] # the list 
  def __init__(self,name):
    self.name = name
    print("Some message to welcome users")

  def create_new_account(self):    
    typeOfAcc = input("What Type Of Account Are You Making S/C: ")
    name = input("What Will Be The Name Of The Account: ")
    balance = float(input("What Will Be The Balance Of The Account: "))
    number = int(input("What Will Be The Number Of Your Account: "))
    account = Account(typeOfAcc,name,balance,number)
    self.accounts.append(account)

  def modify_an_account(self):
    # Logic to modify account information
    modify_number = int(input("What Is The Account Number"))
    accountIndex = self.find_account(modify_number)
    if(accountIndex):
      account = self.accounts[accountIndex]
      account.modify_an_account()
    else:
      print("Invalid Account Number!")
      
# [a , b , c]
# c -> d
    

  def close_an_account(self):
    print("Closing account ", self.number )
    print("Hi")
    pass

  def withdraw(self):
    # Logic to take money out of the bank 
    pass

  def diposit(self):
    # Logic to put money in of the bank 
    pass
    
  def listAllAccounts(self):
    pass
  

  def find_account(self,accountNumber):
    for index, account in enumerate(self.accounts):
      if (account.number == accountNumber):
        return index
    


bank = Bank("Bank")
bank_open = True
while bank_open:
  choise = int(input("MAIN MENU\n 1. NEW ACCOUNT\n 2. DEPOSIT AMOUNT\n 3. WITHDRAW AMOUNT { Enter acc Number && ammount}\n 4. BALANCE ENQUIRY\n 5. ALL ACCOUNT HOLDER LIST { AccuntNumber | Name  | type | Balance}\n 6. CLOSE AN ACCOUNT\n 7. MODIFY AN ACCOUNT\n 8. EXIT\nSelect Your Option (1-8)"))
  if(choise == 1):
    bank.create_new_account()
  elif (choise == 2):
    pass
  elif (choise == 8):
    bank_open = False
  else:
    print("Invalid Choise!!")





  
    



