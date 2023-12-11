<?php
include'connect.php';

// sql to create table
$sql = "CREATE TABLE users (
  id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  voted VARCHAR(45) NULL,
  role VARCHAR(45) NOT NULL DEFAULT 'member',
  username VARCHAR(50) NOT NULL UNIQUE,
  email VARCHAR(50) NOT NULL UNIQUE,
  firstname VARCHAR(50) NOT NULL,
  lastname VARCHAR(50) NOT NULL,
  password VARCHAR(255) NOT NULL,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);";

if ($conn->query($sql) === TRUE) {
  echo "Table users created successfully";
} else {
  echo "Error creating table: " . $conn->error;
}

$sql = "CREATE TABLE vote (
  id INT NOT NULL PRIMARY KEY,
  yes INT,
  no INT,
  );";
if ($conn->query($sql) === TRUE) {
  echo "Table vote created successfully";
} else {
  echo "Error creating table: " . $conn->error;
}


$conn->close();
?>