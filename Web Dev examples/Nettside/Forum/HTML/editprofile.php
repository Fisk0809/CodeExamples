<?php
// Initialize the session
session_start();
 
include'loginreq.php';
include'/var/opt/safe/connect.php';
$id = $_SESSION['id'];

$sql = "SELECT id, voted, role, username, firstname, lastname, email, password FROM users WHERE id='$id'";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
  if ($row = $result->fetch_assoc()) {
    session_start();
    $_SESSION['loggedin'] = TRUE;
    $_SESSION['username'] = $row['username'];
    $_SESSION['firstname'] = $row['firstname'];
    $_SESSION['lastname'] = $row['lastname'];
    $_SESSION['id'] = $row['id'];
    $_SESSION['email'] = $row['email'];
    $_SESSION['voted'] = $row['voted'];
    $_SESSION['role'] = $row['role'];
  }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <script src="https://kit.fontawesome.com/189155ac78.js" crossorigin="anonymous"></script>
    <link rel="stylesheet" href="../CSS/profile.css">
    <link rel="icon" href="../Images/icon.png">
    <link rel="stylesheet" href="../CSS/nav.css" />
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Profile</title>
    <script>
        // The function below will start the confirmation dialog
        function confirmDelete() {
          let confirmDelete = confirm("Are you sure you want to delete this account?");
          if (confirmDelete) {
            alert("Account has successfully been deleted");
            location.href = '../PHP/deleteuser.php';
          } else {
          }
        }
      </script>
    </head>
    <body>
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
                  <a href="profile.php"><i class="fas fa-user-edit"></i> Edit Profile</a>
                  <a href="../PHP/logout.php"><i class="fas fa-sign-out-alt"></i> Log out</a>
                </div>
              </div>
            </div>
            <div class="panel">
              <div class="user" id="userInfo">
                <!-- Prints role in specified colour based on role -->
                <p> <?php 
                    $role = $_SESSION["role"];
                    if ($role == "member") {                      
                      echo '<i style="color:grey;font-size:15px;">
                      Member</i> ';
                      }
                    if ($role == "basic") {                      
                      echo '<i style="color:lime;font-size:15px;">
                      Basic</i> ';
                      }
                    if ($role == "vip") {                      
                      echo '<i style="color:yellow;font-size:15px;">
                      VIP</i> ';
                      }
                    if ($role == "mvp") {                      
                      echo '<i style="color:aqua;font-size:15px;">
                      MVP</i> ';
                    }
                    if ($role == "mvp++") {
                      echo '<i style="color:magenta;font-size:15px;">
                      MVP++</i> ';
                    }
                    if ($role == "admin") {                      
                    echo '<i style="color:red;font-size:15px;">
                    Admin</i> ';
                    }
                    if ($role == "owner") {
                      echo '<i style="color:orange;font-size:15px;">
                      Owner</i>';
                    }
                    ?>
                </p>
                <p>Username: <?php print_r($_SESSION['username']); ?></p> <br>
                <p>Email: <?php print_r($_SESSION['email']); ?></p> <br>
                <p>Firstname: <?php print_r($_SESSION['firstname']); ?> </p> <br>
                <p>Lastname: <?php print_r($_SESSION['lastname']) ?></p> <br> 
                <button onclick="changeDisplay()" class="editbtn">Edit</button>
              </div> <br>
              <div class="edit" id="editForm" style="display:none;"">
                <form action="../PHP/updateuser.php" method="post">
                <label for="name">Username:</label>
                <input type="text" id ="name" name="username" class="input" > <br>
                <div class="confirm">
                <?php
                    if(!empty($_SESSION['userconf'])){
                    print_r($_SESSION['userconf']);
                    }
                ?>
                </div>
                <br />
                <label for="email">Email: </label>
                <input type="text" id="email" name="email" class="input"> <br>
                <div class="confirm">
                <?php
                    if(!empty($_SESSION['emailconf'])){
                    print_r($_SESSION['emailconf']);
                    }
                ?>
                </div>
                <br />
                <label for="firstname">First Name: </label>
                <input type="text" id="fname" name="fname" class="input"> <br>
                <div class="confirm">
                <?php
                    if(empty(!$_SESSION['firstconf'])){
                    print_r($_SESSION['firstconf']);
                    }
                ?>
                </div>
                <br />
                <label for="lastname">Last Name:</label>
                <input type="text" id="lname" name="lname" class="input"> <br>
                <div class="confirm">
                <?php
                    if(!empty($_SESSION['lastconf'])){
                    print_r($_SESSION['lastconf']);
                    }
                ?>
                </div>
                <br />
                <label for="pw">Password:</label>
                <input type="password" id="pasw" name="pasw" class="input"> <br>
                <div class="confirm">
                <?php
                    if(!empty($_SESSION['passconf'])){
                    print_r($_SESSION['passconf']);
                    }
                ?>
                </div>
                <br />
                <div class="btns">
                  <input type="submit" value="Update" class="submit">
                  <button onclick="changeDisplay()" class="editbtn">Cancel</button>
                </div>               
                </form> <br>
              </div>
              <button onclick="confirmDelete()" class="delete">Delete Account</button>
      </div>
      <script>
        function changeDisplay() {
          var form = document.getElementById("editForm");
          var info = document.getElementById("userInfo");
          if (form.style.display === "none") {
            form.style.display = "block";
            info.style.display = "none";
          } else {
            form.style.display = "none";
            info.style.display = "block";
          }
        }
      </script>
    </body>
  </html>



