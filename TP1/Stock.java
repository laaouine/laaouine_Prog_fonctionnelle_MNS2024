import java.util.HashMap;
import java.util.Map;

public class Stock {
    private Map<String, Fruit> fruits = new HashMap<>();

    
    public void add_Fruit(Fruit fruit) {
        fruits.put(fruit.getName(), fruit);
        System.out.println(fruit.getName() + " ajouté au stock.");
    }

    
    public void add_unites(String name, int units) {
        Fruit fruit = fruits.get(name);
        if (fruit != null) {
            fruit.setQuantity(fruit.getQuantity() + units);
            System.out.println(units + " unités de " + name + " ajoutées.");
        } else {
            System.out.println(name + " n'existe pas dans le stock.");
        }
    }

    
    public void sell_Fruit(String name, int units)  {
        Fruit fruit = fruits.get(name);
        try {
            if (fruit == null) {
                throw new Exception("Fruit non trouvé.");
            }
            if (fruit.getQuantity() < units) {
                throw new Exception("Stock insuffisant pour " + name + ".");
            }
            fruit.setQuantity(fruit.getQuantity() - units);
            System.out.println(units + " " + name + " vendus.");
            System.out.println("Le stock de " + name + " est maintenant de " + fruit.getQuantity() + ".");
        } catch (Exception e) {
            System.out.println("Erreur : " + e.getMessage());
        }
    }

    
    public void remove_Fruit(String name) {
        fruits.remove(name);
        System.out.println(name + " supprimé du stock.");
    }

    // Afficher le stock
    public void uc01_displayStock() {
        System.out.println("Stock actuel :");
        for (Fruit fruit : fruits.values()) {
            System.out.println(fruit);
        }
    }
}
