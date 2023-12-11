<?php
session_start();

$role = "banned";
$id = $_POST['id'];
$rank = $_POST['rank'];

include'rolereq.php';

if(!empty($_POST['ban']) || $_POST['ban'] == true) {
    include"/var/opt/safe/connect.php";
    $sql = "UPDATE users SET role='$role' WHERE id='$id'";
    if ($conn->query($sql) === TRUE) {
        $_SESSION['banconf'] = "$id has been banned";
        header("Location: ../HTML/manageusers.php");
    }
}

if(!empty($_POST['rank'])) {
    include"/var/opt/safe/connect.php";
    $sql = "UPDATE users SET role='$rank' WHERE id='$id'";
    if ($conn->query($sql) === TRUE) {
        $_SESSION['rankconf'] = "$id has been updated to $rank";
        header("Location: ../HTML/manageusers.php");
    }
}

?>