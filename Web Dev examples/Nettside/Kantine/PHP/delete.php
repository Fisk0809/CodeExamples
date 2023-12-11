<?php
include'../DB/kconnect.php';

$id = $_GET['id'];

$sql = $kconn->query( "DELETE FROM varer WHERE id = '$id'");

header("Location: ../HTML/admin.php" );

?>