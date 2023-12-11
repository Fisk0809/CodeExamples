<?php 
include'../DB/kconnect.php';

$dag = $_POST['dag'];
$rett = $_POST['rett'];
$pris = $_POST['pris'];
$submit = $_POST['submit'];


if (!empty($rett)) {
    $sql = "UPDATE retter SET rett='$rett' WHERE dag='$dag'";
    if ($kconn->query($sql) === TRUE) {
        header("Location: ../HTML/admin.php");
    } else {
    echo "Error updating record: " . $kconn->error;
    }
}

if (!empty($pris)) {
    $pris = $pris . "kr";
    $sql = "UPDATE retter SET pris='$pris' WHERE dag='$dag'";
    if ($kconn->query($sql) === TRUE) {
       header("Location: ../HTML/admin.php");
    } else {
    echo "Error updating record: " . $kconn->error;
    }
}

?>