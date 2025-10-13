class BankAccount:
    def __init___(self,balance):
        self.balance= balance

    def get_balance(self):
        return self.__balance
    

    def set_balance(self,amount):
        if amount >= 0:
            self.balance = amount
        else:
            print("Invalid amount. Balance cannot be negative.")
