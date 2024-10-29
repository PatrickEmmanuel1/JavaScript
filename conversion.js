//String representing a number
let numberString = "20";
//Converting the string to a number using Number() function
let actualNumber = Number(numberString);
//Add 10
let result = actualNumber + 10;
//Log result
console.log("Result :", result);

// Declare two variables with initial values
let a = 5; // Replace with your first value
let b = 10; // Replace with your second value

// Log original values
console.log("Before swapping: a =", a, ", b =", b);

// Swap the values using arithmetic operations
a = a + b; // a now holds the sum of both values
b = a - b; // b is assigned the original value of a
a = a - b; // a is assigned the original value of b

// Log swapped values
console.log("After swapping: a =", a, ", b =", b);