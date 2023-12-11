<?php

if(!isset($_SESSION["admin"]) || $_SESSION["admin"] !== true){
    header("location: ../HTML/login.php");
    exit;
}


?>