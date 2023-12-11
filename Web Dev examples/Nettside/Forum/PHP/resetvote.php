<?php
session_start();

include'rolereq.php';
include'/var/opt/safe/connect.php';

$sql = "UPDATE vote SET yes = '0', no = '0' WHERE id ='1'";
    if ($conn->query($sql) === TRUE) {
        $sql = "UPDATE users SET voted = NULL ";
        if ($conn->query($sql) === TRUE) {
            $_SESSION['confirm'] = "Vote reset";
            header("location: ../HTML/forum.php");
        }
    }

?>
