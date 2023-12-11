<?php
include'/var/opt/safe/connect.php';

$sql = "CREATE DATABASE forumDB";
if ($conn->query($sql) === TRUE) {
    echo"Database forumDB successfully created";
} else {
    echo"Error creating database" . $conn->error;
}

$sql = "CREATE TABLE forumDB.page (
    id INT(10) UNSIGNED,
    title VARCHAR(40),
    author_id INT(10) UNSIGNED,
    created DATETIME,
    modified DATETIME
)";
if ($conn->query($sql) === TRUE) {
    echo"Table page successfully created";
} else {
    echo"Error creating table" . $conn->error;
}


$sql = "CREATE TABLE forumDB.page_body (
    id INT(10) UNSIGNED,
    body TEXT
)";
if ($conn->query($sql) === TRUE) {
    echo"Table page_body successfully created";
} else {
    echo"Error creating table" . $conn->error;
}



$conn->close();
?>