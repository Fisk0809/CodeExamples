<?php
session_start();
session_unset();
session_destroy();

include'/var/opt/safe/connect.php';


$username = $_POST["username"];
$fname = $_POST["fname"];
$lname = $_POST["lname"];
$password = $_POST["pasw"];
$email = $_POST['email'];
  
// Validate email
if (filter_var($email, FILTER_VALIDATE_EMAIL)) {
    
if (!empty($username)) {
    if(!empty($email)) {
        if(!empty($fname)) {
            if(!empty($lname)) {
                if(!empty($password)) {
                    $password = password_hash($password, PASSWORD_DEFAULT);
                    $sql = $conn->prepare("INSERT INTO users (username, email, firstname, lastname, password) VALUES (?, ?, ?, ?, ?)");
                    $sql->bind_param("sssss", $username, $email, $fname, $lname, $password);

                    if ($sql->execute() === TRUE) {
                        $sql->close();
                        $conn->close();
                        header("Location: ../HTML/login.php");
                    } else {
                        session_start();
                        $_SESSION['regerr'] = "$sql->error";
                        header("Location: ../HTML/register.php");
                    }
                } else {
                    session_start();
                    $_SESSION['regerr'] = "Password cannot be empty!";
                    header("Location: ../HTML/register.php");
                }
            } else {
                session_start();
                $_SESSION['regerr'] = "Lastname cannot be empty!";
                header("Location: ../HTML/register.php");
            }
        } else {
            session_start();
            $_SESSION['regerr'] = "Firstname cannot be empty!";
            header("Location: ../HTML/register.php");
        }
    } else {
        session_start();
        $_SESSION['regerr'] = "Email cannot be empty!";
        header("Location: ../HTML/register.php");
    }
} else {
    session_start();
    $_SESSION['regerr'] = "Username cannot be empty!";
    header("Location: ../HTML/register.php");
}  
} 
else {
    session_start();
    $_SESSION['regerr'] = "$email is not a valid email format";
    header("Location: ../HTML/register.php");
}
  
 
?>


