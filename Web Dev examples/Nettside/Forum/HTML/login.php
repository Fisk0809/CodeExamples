<?php
session_start();

$usererror = $_SESSION['usererror'];
$passerror = $_SESSION['passerror'];
?>

<!DOCTYPE html>
<html lang="en">
  <head>
    <link rel="icon" href="../Images/icon.png" />
    <link rel="stylesheet" href="../CSS/login.css" />
    <link rel="stylesheet" href="../CSS/nav.css" />
    <link
      href="https://fonts.googleapis.com/css2?family=Dancing+Script&display=swap"
      rel="stylesheet"
    />
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Login</title>
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
        <li><a class="active" href="register.php">Sign up</a></li>
      </ul>
    </div>
    <h2>Log in</h2>
    <div class="panel">
      <form action="../PHP/login.php" method="post">
        <label for="name">Username:</label>
        <input type="text" id="name" name="username" class="input" />
        <div class="error">
          <?php 
              if(!empty($usererror)){
              print_r($usererror);
              }       
          ?>
        </div>
        <br />
        <label for="pw">Password:</label>
        <input type="password" id="pasw" name="pasw" class="input" />
        <div class="error">
          <?php 
              if(!empty($passerror)){
              print_r($passerror);
              }       
          ?>
        </div>
        <br />
        <input type="submit" value="Log in" class="submit" />
      </form>
      <p>
        Don't have an account? <br />
        <a href="register.php">Sign up now</a>.
      </p>
      <p>
        Forgot password? <br />
        <a href="resetpass.php">Click to reset</a>.
      </p>
    </div>
  </body>
</html>
