<?php
session_start();
session_unset();
session_destroy();


include'/var/opt/safe/connect.php';

$username = $_POST['username'];
$password = $_POST['pasw'];

$sql = "SELECT id, voted, role, username, firstname, lastname, email, password FROM users WHERE username='$username'";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
  if ($row = $result->fetch_assoc()) {
    if (password_verify($password, $row['password'])) {
      session_start();
      $_SESSION['loggedin'] = TRUE;
      $_SESSION['username'] = $username;
      $_SESSION['firstname'] = $row['firstname'];
      $_SESSION['lastname'] = $row['lastname'];
      $_SESSION['id'] = $row['id'];
      $_SESSION['email'] = $row['email'];
      $_SESSION['voted'] = $row['voted'];
      $_SESSION['role'] = $row['role'];
      header("Location: ../HTML/forum.php");
    } else {
      session_start();
      $_SESSION['passerror'] = 'Password is incorrect!';
      header("Location: ../HTML/login.php");
    }
  }
} else {
  session_start();
  $_SESSION['usererror'] = 'Username is invalid!';
  header("Location: ../HTML/login.php");
}
$conn->close();
?> 