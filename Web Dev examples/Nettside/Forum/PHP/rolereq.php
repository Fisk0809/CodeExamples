<?php 
session_start();
if(!isset($_SESSION["loggedin"]) || $_SESSION["loggedin"] !== true){
    header("location: login.php");
    exit;
}

$role = $_SESSION['role'];
if (!empty($role) || $role == "owner") {
    $role = "admin";
}

if(!isset($_SESSION["role"]) || $role !== "admin"){
    header("location: forum.php");
    exit;
}


?>