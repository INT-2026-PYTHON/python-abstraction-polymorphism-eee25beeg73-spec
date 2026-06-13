class CreditCard:
    def __init__(self,name,card_no):
        self.card_no=card_no
        self.name=name
    def pay(self,amount):
        return (f"{self.name} paid {amount} card{self.card_no}")
class UPI:
    def __init__(self,upi_id):
        self.upi_id=upi_id
    def pay(self,amount):
        return (f"{self.upi_id} paud {amount}")
class Cash:
    def __init__(self,name):
        self.name=name
    def pay(self,amount):
        return (f"{self.name} paid {amount} using cag")
def checkout(payment_method,amount):
    return payment_method.pay(amount)
methods = [
    CreditCard("Alice", "4111-1111-1111-1111"),
    UPI("bob@upi"),
    Cash("Carol")
]

for m in methods:
    print(checkout(m, 500))
    