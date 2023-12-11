<?php 
include'/var/opt/safe/connect.php';

$sql = "CREATE DATABASE kantineDB";
if ($conn->query($sql) === TRUE) {
    echo'Database kantineDB created';
} else {
    echo'Error creating kantineDB' . $conn->error();
}

$sql = "CREATE TABLE kantineDB.varer (
    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    vare VARCHAR(45) NOT NULL,
    pris INT NOT NULL,
    image BLOB
    )
    ";
if ($conn->query($sql) === TRUE) {
    echo'Table kantine created';
} else {
    echo'Error creating table kantine' . $conn->error();
}

$sql = "CREATE TABLE kantineDB.retter (
    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    rett VARCHAR(45) NOT NULL,
    pris INT NOT NULL,
    dag VARCHAR(45) NOT NULL)
    ";
if ($conn->query($sql) === TRUE) {
    echo'Table kantine created';
} else {
    echo'Error creating table kantine' . $conn->error();
}

?>