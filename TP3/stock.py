from typing import Dict


#        Key / Value
Stock = Dict[str, int]



def add_Fruits(stock: Stock, fruit_name: str, fruit_quantite: int) -> Stock:
    new_stock = stock.copy()
    new_stock[fruit_name] = fruit_quantite
    return new_stock


def add_unity(stock: Stock, fruit_name : str, fruit_unitees: int) -> Stock:
    if fruit_name in stock:
        #print("Add unity start in IF")
        new_stock = stock.copy()
        new_stock[fruit_name] += fruit_unitees
        return new_stock
    else:
        #print("add unity jamais rentré dans le IF")
        return stock

def sell_fruit(stock: Stock, fruit_name, fruit_unitees) -> Stock:
    if(fruit_name in stock and stock[fruit_name] >= fruit_unitees):
        new_stock = stock.copy()
        new_stock[fruit_name] -= fruit_unitees
        return new_stock
    else:
        return stock
    
def remove_fruit(stock : Stock, fruit_name) -> Stock:
    if(fruit_name in stock):
        new_stock = stock.copy()
        del new_stock[fruit_name]
        return new_stock
    else:
        return stock
    
def printStock(stock: Stock):
    print("Le Stock Actuelle est : ")
    for fruit, quantite in stock.items():
        print("Fruit : ", fruit, ", Quantitées : ",quantite)









laaouine_stock = {}

laaouine_stock = add_Fruits(laaouine_stock, "Pomme", 12)
laaouine_stock = add_Fruits(laaouine_stock, "Banane", 15)
laaouine_stock = add_Fruits(laaouine_stock, "Ananas", 60)

printStock(laaouine_stock)

laaouine_stock = add_unity(laaouine_stock,"Ananas", 170)


printStock(laaouine_stock)


laaouine_stock = remove_fruit(laaouine_stock, "Ananas")

printStock(laaouine_stock)

