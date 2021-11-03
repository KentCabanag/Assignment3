def getAmmount():
    _amt = float(input("Enter the ammount of money you have: "))
    return _amt

def getAplprice():
    _aplprice = float(input("Enter the price of an apple: "))
    return _aplprice

def getnapple(_amtmoney, apl_price):
    _napple = int(_amtmoney//apl_price)
    return _napple

def getchange(amtmoney, aplprice):
    _change = amtmoney%aplprice
    return _change

ammount = getAmmount()
appleprice = getAplprice()
napple = getnapple(ammount, appleprice)
change = getchange(ammount, appleprice)

print(f"You can buy {napple} apples and your change is {change:.2f} pesos.")