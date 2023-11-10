<?php
// Define variables
$name = "John Doe";
$age = 30;
$city = "New York";

// Create an array
$fruits = array("Apple", "Banana", "Cherry");

// Define a function
function greet($name) {
    echo "Hello, $name!";
}

// Conditional statement
if ($age >= 18) {
    echo "You are an adult.";
} else {
    echo "You are a minor.";
}

// Loop through an array
foreach ($fruits as $fruit) {
    echo "I like $fruit.\n";
}

// Call a function
greet($name);

// Working with dates
$date = date("Y-m-d H:i:s");
echo "Current date and time: $date";

// Database connection (example)
$servername = "localhost";
$username = "username";
$password = "password";
$dbname = "database";

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

echo "Connected to the database successfully.";

// File handling (example)
$myfile = fopen("example.txt", "w");
fwrite($myfile, "This is some text.");
fclose($myfile);

echo "Data written to the file.";

// Handle user input (example)
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $userInput = $_POST["user_input"];
    echo "You entered: $userInput";
}
?>
