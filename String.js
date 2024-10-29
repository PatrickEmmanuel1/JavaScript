let string = "Patrickstar the starfish";
let uppercaseString = string.toUpperCase();

console.log("Uppercase version:",uppercaseString);

let myString = "Java script is fun to write!";
let extractsub = myString.substring(0, 10);

console.log("Extracted substring is :", extractsub);

//Checking if a string containsa word
 
let sentence = "JavaScript programming is very versatile.";

let wordfind = "versatile";
if(sentence.includes(wordfind)){
    console.log('The word "versatile" is in the sentence.');

} else {
    console.log('The word "versatile" is not found');

}