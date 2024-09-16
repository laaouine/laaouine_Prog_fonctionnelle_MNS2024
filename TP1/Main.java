public class Main {
    public static void main(String[] args) {
        Stock stock = new Stock();

        // Étape 1 : Constitution d'un stock
        stock.add_Fruit(new Fruit("Pomme", 10));
        stock.add_Fruit(new Fruit("Poire", 5));
        stock.add_Fruit(new Fruit("Ananas", 8));


        //2 -- Ajout de Plus
        stock.add_unites("Pomme", 5);

        
        stock.add_unites("Poire", 8);

        // Vérification du Stock
        stock.printStock();

        // vente de deux Ananas
        stock.sell_Fruit("Ananas", 2);
        
        // vérification du Stock
        stock.printStock();

        
        stock.remove_Fruit("Ananas");

        
        stock.printStock();


        //Pour Tester les Exceptions.
        // stock.sell_Fruit("Poire", 25);

        // stock.sell_Fruit("Poire", 2);

        // stock.printStock();

    }
}
