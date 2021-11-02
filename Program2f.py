def apple():
    n_apple = int(input("Number of Apples you want to buy: "))
    return n_apple

def orange():
    n_orange = int(input("Number of Oranges you want to buy: "))
    return n_orange

def price(apl_price, org_price):
    apl_price = apl_price * 20
    org_price = org_price * 25
    t_price = apl_price + org_price
    return t_price

t_apple = apple()
t_orange = orange()
g_total = price (t_apple, t_orange)

print(f"The total ammount is {g_total}.")