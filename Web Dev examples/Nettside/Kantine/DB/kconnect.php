<?php
$servername = "localhost";
$username = "fstadt";
$password = 'F1$k0809';
$dbname = "kantineDB";

// Create connection
$kconn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($kconn->connect_error) {
  die("Connection failed: " . $kconn->connect_error);
}

?>