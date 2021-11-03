def getApple():
    n_apple = int(input("Number of Apples you want to buy: "))
    return n_apple

def getOrange():
    n_orange = int(input("Number of Oranges you want to buy: "))
    return n_orange

def getPrice(apl_num, org_num):
    apl_price = apl_num * 20
    org_price = org_num * 25
    t_price = apl_price + org_price
    return t_price

t_apple = getApple()
t_orange = getOrange()
g_total = getPrice(t_apple, t_orange)

print(f"The total ammount is {g_total}.")