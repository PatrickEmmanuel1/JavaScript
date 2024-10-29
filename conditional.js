let number = 12;
if (number % 2 === 0){
    console.log("It is even.");


}else {
    console.log("It is an odd number.");
}

let age = 30;
if( age >= 18){
    console.log("You are eligible to vote.");

}else {
    console.log("You are not eligible to vote.");
}

let score = 80;
let grade;

if(score >=90){
    grade = 'A';
}else if(score >= 80 ){
    grade = 'B';
}else if (score >=70){
   grade = 'C';
}else if (score >=60){
    grade = 'D';
}else {
    grade = 'F';
}

console.log('The letter grade for a score of ${score}, is: ${grade}');