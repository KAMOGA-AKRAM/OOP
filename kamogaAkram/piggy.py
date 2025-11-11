
class PiggyBank:
    def __init__(self,coins):
        self._coins = coins
        self.put_in(coins)

    def put_in(self,amount):
        if amount <=0:
            raise ValueError('cant add 0 money')
        self._coins +=amount

    def take_out(self,amount):
        if amount <= 0:
            raise ValueError('cant take out 0 money')
        if amount > self.coins:
            raise ValueError('not enough money')
        self._coins -= amount    

    def how_much(self):
        return self._coins        

akram = PiggyBank(100)
akram.put_in(300)
print("akram's box has:",akram.how_much(), 'coins')