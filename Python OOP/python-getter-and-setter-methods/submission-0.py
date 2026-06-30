class BankAccount:
    def __init__(self, balance: int):
        # Add private balance
        self._balance=balance

    # TODO: Add getter method for balance
    def get_balance(self)->int:
        return self._balance

    # TODO: Add setter method for balance
    def set_balance(self,new_balance:int)->None:
        if new_balance<0:
            print("Cannot set negative balance!")
            return
        self._balance=new_balance



# Don't modify the code below this line
account = BankAccount(1000)
print(account.get_balance())
account.set_balance(-100)
print(account.get_balance())
account.set_balance(100)
print(account.get_balance())
account.set_balance(0)
print(account.get_balance())
