class BankAccount:

#initialisation
    def _init_(self, account_number, customer_name,initial_balance=0.0):
        self.account_number=account_number
        self.customer_name=customer_name
        self.balance=initial_balance

    def deposit(self, amount):
        self.balance+=amount 
            
    def withdraw(self, amount):
        self.balance-=amount 

account1=BankAccount("123", "Alice", 50.00)
account1.desposit(28)
account1.withdraw(10)
