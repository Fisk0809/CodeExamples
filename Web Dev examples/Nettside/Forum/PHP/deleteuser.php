<?php
session_start();

include'loginreq.php';
include'/var/opt/safe/connect.php';

$id = $_SESSION['id'];

$sql = $conn->query( "DELETE FROM users WHERE id = '$id'");

header("Location: ../HTML/login.php" );

?>