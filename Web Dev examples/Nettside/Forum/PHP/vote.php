<?php
session_start();
unset($_SESSION['error']);
unset($_SESSION['confirm']);


include'/var/opt/safe/connect.php';

$id = $_SESSION['id'];

echo $_SESSION['voted'];

if(isset($_SESSION["voted"]) || $_SESSION["voted"] == 'voted'){
    session_start();
    $_SESSION['error'] = "This account has already voted!";
    header("location: ../HTML/forum.php");
    exit;
}

session_start();

$yes = $_POST["yes"];
$no = $_POST["no"];

$sql = "SELECT id, yes, no FROM vote WHERE id=1";
$result = $conn->query($sql);


if($row = $result->fetch_assoc()){
    $yesid = $row["yes"];
    $noid = $row["no"];

    if (isset($yes)){
        $sql = "UPDATE vote SET yes=$yesid+1 WHERE id=1";
        if ($conn->query($sql)===TRUE){

        $sql2 = "UPDATE users SET voted='voted' WHERE id='$id'";
        $conn->query($sql2);
        $_SESSION['voted']='voted';
        header("location: ../HTML/forum.php");
        }
        }

        
    if (isset($no)){
        $sql = "UPDATE vote SET no=$noid+1 WHERE id=1";
        if ($conn->query($sql)===TRUE){

        $sql2 = "UPDATE users SET voted='voted' WHERE id='$id'";
        $conn->query($sql2);
        $_SESSION['voted']='voted';
        header("location: ../HTML/forum.php");
        }
        }
}

?>