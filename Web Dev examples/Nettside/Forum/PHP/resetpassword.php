<?php
session_start();
session_unset();
session_destroy();

include'/var/opt/safe/connect.php';

$username = $_POST['username'];
$email = $_POST['email'];
$password = $_POST['pasw'];
$passwordhash = password_hash($password, PASSWORD_DEFAULT);

$sql = "SELECT id, username, email, password FROM users WHERE username='$username'";
$result = $conn->query($sql);

if (isset($username)) {
  if ($row = $result->fetch_assoc()) {
    if (password_verify($password, $row['password'])) {
      session_start();
      $_SESSION['error'] = "This is your current password";
      header("Location: ../HTML/resetpass.php");
    } else {
        if ($row['email'] == "$email") {
          $sql = "UPDATE users SET password='$passwordhash' WHERE username='$username'";
          if ($conn->query($sql) === TRUE) {
          header('location: ../HTML/login.php');
        } 
        } else {
          session_start();
          $_SESSION['error'] = "Email is incorrect!";
          header("Location: ../HTML/resetpass.php");
      }
    }
  } else {
    session_start();
    $_SESSION['error'] = "This is username is not registered!";
    header("Location: ../HTML/resetpass.php");
  }
}

?>