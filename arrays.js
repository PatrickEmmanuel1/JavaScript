let fruits = ["Watermelon", "Mango","Banana","Grapes","Tangerines"];
//Log each fruit
for(let i = 0; i < fruits.length; i++){

    console.log(fruits[i]);
}
// adding an item and removing the first item
fruits.push("Cherries");
fruits.shift();
console.log("Updated list:", fruits);

//finding index of a specific item
let fruitfind = "Mango";
let index = fruits.indexOf(fruitfind);
if(index !== -1){
    console.log('The item "Mango" is found at index:');

} else {
    console.log('The item "Mango" is not found.');
}
