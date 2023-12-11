<?php
include 'connect.php';

$fornavn = $_POST["fname"];
$etternavn = $_POST["ename"];
$email = $_POST["email"];
$passord = $_POST["pw"];

$sql = "INSERT INTO MyGuests (firstname, lastname, email, password)
VALUES ('$fornavn', '$etternavn', '$email', '$passord')";

if ($conn->query($sql) === TRUE) {
  echo "New record created successfully";
} else {
  echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>s