implement a class called bank account that represents a class should have private
attributes for account number.account holder name and accounts balance.include methods to. 
deposit money,withdraw money,and display the account balance ensure  that the account balance. 
cannot be accessed directly from outside the class, write a program to create an instance of the. 
bank account class and deposit and withdraw functionality.


  class bank account;

def__init__(self, account_number,account_holder_name, initial_balance=0.0):
       self.__account_number = account_numbe 
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

def deposit (self, amount):
   if amount  >0:
        self.__account_balance += amount
        print ("deposited ₹{}.  New balance:₹{}".format(amount,self.__account_balance))

else:
  print ("Invalid deposit amount. please deposit a positive amount. ")

   def withdrawa(self, amount):
     if amount>0 and amount<= self. __account_balance:
       self. __account_balance-=amount
       print(" withdraw ₹{}.New balance:₹{}".format(amount,self.__account_balance))

else:
  print ("Invalid withdrawal amount or insufficient balance. ")

def display_balance (self):
  print(" account balance for{}(account#{}):₹{}".format(
       self. __ account_holder_name, self. __account_number, 
       self. __ account_balance )) 




#create an instance of the bankaccount class 
account= bankaccount (account_number="123456789", 
                      account_holder_name="Kaviya", 
                      initial_ balance=5000.0) 

#test deposit and withdrawal functionality
account. display_balance () 
account. deposit (500.0)
account. withdraw (200.0)
account. display_balance ()
  def __init__(self, params):
      