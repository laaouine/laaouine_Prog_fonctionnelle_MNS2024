// la variable fruitStock est générique, à mon avis ca prend pas une grand eplace comme j'ai fait avec une Map (HASHSET) en Java
let fruitsStock = [
  { id: 1, name: "Pomme", quantity: 10 },
  { id: 2, name: "Poire", quantity: 5 },
  { id: 3, name: "Ananas", quantity: 8 }
];


// une fonction qui fera juste un traitement sur la variable, on a pas de base de données ouun truc un peu complexe à manipuler
function addFruitToStock(name: string, quantity: number) {
  const existingProduct = fruitsStock.find((p) => p.name === name);

  if (existingProduct) {
    existingProduct.quantity += quantity;
  } else {
    fruitsStock.push({ id: fruitsStock.length + 1, name, quantity });
  }
}


//Une question : Est-ce que on change juste le contenue de la varriable en enlévent la fruit choisie ? ou on recrer une nouvelle variable..
function deleteFruit(name: string) {
  fruitsStock = fruitsStock.filter((p) => p.name !== name);
  console.log(`${name} deleted from stock`);
}


//je pense la meme chose / meme complexité et simplicité que .toString() en java 
function showStock() {
  fruitsStock.forEach((fruit) => {
    console.log(`Fruit : ${fruit.name} | Quantity : ${fruit.quantity}`);
  });
}


// emmm je ne vois pas d'Exception, mais si on a des Exception en Type script. Je pense que de cette maniére de codage (fonctionnelle) on aura des application plus optimale
// mais je ne pense pas qu'on aura des applications compléte. 
function sellFruit(name: string, quantity: number) {
  const fruit = fruitsStock.find((p) => p.name === name);

  if (fruit && fruit.quantity >= quantity) {
    fruit.quantity -= quantity;
    console.log(`${quantity} ${name} sold`);
  } else {
    console.log(`Not enough ${name} or unknown fruit`);
  }
}

addFruitToStock("Pomme", 5);
addFruitToStock("Citron", 10);
sellFruit("Ananas", 2);
showStock();
deleteFruit("Ananas");
showStock();

/*
2 Ananas sold
Fruit : Pomme | Quantity : 15
Fruit : Poire | Quantity : 5
Fruit : Ananas | Quantity : 6
Fruit : Citron | Quantity : 10
Ananas deleted from stock
Fruit : Pomme | Quantity : 15
Fruit : Poire | Quantity : 5
Fruit : Citron | Quantity : 10
*/
