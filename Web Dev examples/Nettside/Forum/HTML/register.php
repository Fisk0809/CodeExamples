<?php 
session_start();
$regerr = $_SESSION['regerr']

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="icon" href="../Images/icon.png">
    <link rel="stylesheet" href="../CSS/login.css">
    <link rel="stylesheet" href="../CSS/nav.css">
    <link href="https://fonts.googleapis.com/css2?family=Dancing+Script&display=swap" rel="stylesheet">
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register</title>
</head>
<body>
    <div class="nav">
        <ul class="nav-left">
            <li><a href="../index.html">Home</a></li>
            
        
        </ul>
        
        <ul class="nav-center">
            <li><a href="forum.php">Forum</a></li>
        
        </ul>
        
        <ul class="nav-right">
            <li><a class="active" href="login.php">Login</a></li>
        </ul>
        </div>
        <h2>Sign up</h2>
        <div class="panel">
                <form action="../PHP/safe-insert.php" method="post">
                    <label for="name">Username:</label>
                    <input type="text" id ="name" name="username" class="input" > <br>
                    <label for="email">Email: </label>
                    <input type="text" id="email" name="email" class="input"> <br>
                    <label for="firstname">First Name: </label>
                    <input type="text" id="fname" name="fname" class="input"> <br>
                    <label for="lastname">Last Name:</label>
                    <input type="text" id="lname" name="lname" class="input"> <br>
                    <label for="pw">Password:</label>
                    <input type="password" id="pasw" name="pasw" class="input"> <br>
                    <input type="submit" value="Sign up" class="submit">   
                </form> <br>
                <div class="error">
                    <?php
                    if (!empty($regerr)) {
                        print_r($regerr);
                    }
                    ?>
                </div>

                <p>
                    Already have an account? <br> <a href="login.php">
                        Sign in here.
                    </a>
                </p>
            </div>
            <script src="../JS/cleanup-input.js"></script>
</body>
</html>