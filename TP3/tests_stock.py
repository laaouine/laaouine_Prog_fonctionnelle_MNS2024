# Import Minimal, pour récupérer seulement les fonction dont je vais faire des tests
from stock import add_Fruits, add_unity, sell_fruit, remove_fruit


def test_Add_Fruits():
        stock = {}
        stock = add_Fruits(stock, "Pomme", 10)
        assert stock["Pomme"] == 10



def test_Add_Unitee():
        stock = {"Pomme" : 25, "Ananas" : 8}
        stock = add_unity(stock, "Ananas", 8)
        assert stock["Ananas"] == 16

def test_sell_Fruit():
        stock = {"Ananas" : 125}
        stock = sell_fruit(stock, "Ananas", 25)
        assert stock["Ananas"] ==100

def test_Remove_Fruit():
        stock = {"Ananas" : 6, "Pomme" : 16, "Zebi" : 99999999999999}
        stock = remove_fruit(stock, "Zebi")
        assert "Zebi" not in stock