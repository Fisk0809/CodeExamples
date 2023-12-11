<?php
$password = $_POST["pw"];

include'../DB/adminpw.php';


if (password_verify($password, $adminpw)) {
    session_start();
    $_SESSION['admin'] = TRUE;
    header("Location: admin.php");
    }

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../CSS/header.css">
    <link rel="stylesheet" href="../CSS/login.css">
    <link rel="shortcut icon" href="../Images/favicon.ico" type="image/x-icon">
    <title>Admin Login</title>
</head>
<body>
<div class="container">
    <div class="background">
        <img src="../Images/banner-background-image.svg" alt="">
    </div>
    <div class="header">
            <div class="header-wrapper-upper"></div>
            <div class="header-wrapper-lower-outer">
                <div class="header-wrapper-lower-inner">
                    <div class="header-content">
                        <div class="logo">
                        <a id="hamarlogo" href="/">
                                    <span class="custom-logo">
                                      <img alt="Hamar katedralskole" src="../Images/hamar-katedralskole.svg">
                                    </span>
                                  </a>
                        </div>
                        <div class="navigation">
                            <div class="navigation-buttons">
                            <ul>
                                    <li><a href="retter.php">Retter</a></li>
                                    <li><a href="varer.php">Varer</a></li>
                                    <li><a href="login.php">Administer</a></li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    
    <div class="form">
        <form action="" method="post">
            <label for="pw">Admin passord:</label>
            <input type="password" name="pw" id="pw" class="input">
            <input type="submit" value="Logg inn" class="submit">
        </form>
    </div>
</div>
</body>
</html>