// Function to add two numbers
function add(a, b) {
    return a + b;
  }
  
  // Function to subtract two numbers
  function subtract(a, b) {
    return a - b;
  }
  
  // Function to multiply two numbers
  function multiply(a, b) {
    return a * b;
  }
  
  // Function to divide two numbers
  function divide(a, b) {
    if (b === 0) {
      return "Cannot divide by zero";
    }
    return a / b;
  }
  
  // Function to find the maximum of two numbers
  function findMax(a, b) {
    return Math.max(a, b);
  }
  
  // Function to find the minimum of two numbers
  function findMin(a, b) {
    return Math.min(a, b);
  }
  
  // Function to check if a number is even
  function isEven(num) {
    return num % 2 === 0;
  }
  
  // Function to check if a number is prime
  function isPrime(num) {
    if (num <= 1) {
      return false;
    }
    if (num <= 3) {
      return true;
    }
    if (num % 2 === 0 || num % 3 === 0) {
      return false;
    }
    for (let i = 5; i * i <= num; i += 6) {
      if (num % i === 0 || num % (i + 2) === 0) {
        return false;
      }
    }
    return true;
  }
  
  // Example usage of the functions
  console.log("Addition:", add(5, 3));
  console.log("Subtraction:", subtract(10, 4));
  console.log("Multiplication:", multiply(7, 2));
  console.log("Division:", divide(9, 3));
  console.log("Maximum:", findMax(8, 12));
  console.log("Minimum:", findMin(5, 9));
  console.log("Is 6 even?", isEven(6));
  console.log("Is 7 prime?", isPrime(7));