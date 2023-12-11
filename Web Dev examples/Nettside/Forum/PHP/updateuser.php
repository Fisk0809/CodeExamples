<?php
session_start();
 

include'loginreq.php';
include'/var/opt/safe/connect.php';

$id = $_SESSION["id"];
$username = $_POST["username"];
$email = $_POST["email"];
$fname = $_POST["fname"];
$lname = $_POST["lname"];
$password = $_POST["pasw"];

$passwordhash = password_hash($password, PASSWORD_DEFAULT);

if (!empty($username)) {
    $sql = "UPDATE users SET username='$username' WHERE id='$id'";

if ($conn->query($sql) === TRUE) {
  $_SESSION['userconf'] = "Username has been updated to $username";
 } else {
  echo "Error updating record: " . $conn->error;
}
}

if (!empty($email)) {
    $sql = "UPDATE users SET email='$email' WHERE id='$id'";

    if ($conn->query($sql) === TRUE) {
      $_SESSION['emailconf'] = "Email has been updated to $email";
    } else {
      echo "Error updating record: " . $conn->error;
    }
}

if (!empty($fname)) {
    $sql = "UPDATE users SET firstname='$fname' WHERE id='$id'";

    if ($conn->query($sql) === TRUE) {
      $_SESSION['firstconf'] = "Firstname has been updated to $fname";
    } else {
      echo "Error updating record: " . $conn->error;
    }
}

if (!empty($lname)) {
    $sql = "UPDATE users SET lastname='$lname' WHERE id='$id'";

    if ($conn->query($sql) === TRUE) {
      $_SESSION['lastconf'] = "Lastname has been updated to $lname";
    } else {
      echo "Error updating record: " . $conn->error;
    }
}

if (!empty($password)) {
    $sql = "UPDATE users SET password='$passwordhash' WHERE id='$id'";

    if ($conn->query($sql) === TRUE) {
      $_SESSION['passconf'] = "Password has been updated";
    } else {
      echo "Error updating record: " . $conn->error;
    } 
}
header("Location: ../HTML/editprofile.php"); 




?>