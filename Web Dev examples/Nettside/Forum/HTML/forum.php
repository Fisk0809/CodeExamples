<?php
// Initialize the session
session_start();

include'../PHP/loginreq.php';
include'/var/opt/safe/connect.php';

$sql = "SELECT id, yes, no FROM vote WHERE id=1";
$result = $conn->query($sql);
$row = $result->fetch_assoc();
$error = $_SESSION['error'];
$confirm = $_SESSION['confirm']
?>

<!DOCTYPE html>
<html lang="en">
  <head>
  <script src="https://kit.fontawesome.com/189155ac78.js" crossorigin="anonymous"></script>
    <link rel="icon" href="../Images/icon.png" />
    <link rel="stylesheet" href="../CSS/style.css" />
    <link rel="stylesheet" href="../CSS/nav.css" />
    <link rel="stylesheet" href="../CSS/forum.css">
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Astrophysic Forum</title>
  </head>
  <body>
    <div class="nav">
      <ul class="nav-left">
        <li><a href="../index.html"><i class="fas fa-home"></i> Home</a></li>
      </ul>

      <ul class="nav-center">
        <li><a href="forum.php">Forum</a></li>
      </ul>

      <div class="dropdown">
        <button class="dropbtn">
        <i class="fas fa-user"></i> Profile
          <i class="fa fa-caret-down"></i>
        </button>
        <div class="dropdown-content">
          <a href="editprofile.php"><i class="fas fa-user-edit"></i> Edit Profile</a>
          <a href="../PHP/logout.php"><i class="fas fa-sign-out-alt"></i> Log out</a>
          <?php if ($_SESSION['role'] == "admin" OR $_SESSION['role'] == "owner") : ?>
            <a href="../HTML/manageusers.php"><i class="fas fa-users-cog"></i> Manage</a>
          <?php endif; ?>
        </div>
      </div>
    </div>
   <div class="panel">
    <div class="tables">
      <div class="table">
        <table>
          <tr>
            <th>Yes</th>
          </tr>    
          <tr>
            <td><?php
              print_r($row['yes'])
           ?></td>
          </tr>
        </table>
          </table>
      </div>
      <div class="table">
        <table>
          <tr>
            <th>No</th>
          </tr>
          <tr>
            <td><?php
              print_r($row['no'])
           ?></td>
          </tr>
        </table>
      </div>
    </div>
      
  <br>
    <h4>Should we continue exploring the solar system?</h4> <br>
    <form action="../PHP/vote.php" method="post">
      <div class="flex">
        <input type="submit" class="flex-child" id="yes" name ="yes" value="Yes">
        <input type="submit" class="flex-child" id="no"  name="no" value="No">
    </div>

      </form> <br>
      <div class="error">
          <?php 
              if(!empty($error)){
              print_r($error);
              }       
          ?>
        </div>
        <?php if ($_SESSION['role'] == "admin" OR $_SESSION['role'] == "owner") : ?>
        <form action="../PHP/resetvote.php" method="post">
          <input type="submit" value="Reset" class="reset">
        </form>
        <br>
        <div class="confirm">
        <?php
        if(!empty($confirm)){
        print_r($confirm);
        }
        ?>
        </div>
        

    <?php endif; ?>
  </div>
  </body>
</html>
