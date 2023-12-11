<?php 
include'../DB/kconnect.php';

$id = $_POST['id'];
$update = $_POST['update'];
$vare = $_POST['vare'];
$vpris = $_POST['vpris'];

if ($update == TRUE) {
    if (!empty($vare)) {
        $sql = "UPDATE varer SET vare='$vare' WHERE id='$id'";

        if ($kconn->query($sql) === TRUE) {
            echo':)';
        }
    }

    if (!empty($vpris)) {
        $sql = "UPDATE varer set pris=''$vpris'kr' WHERE id='$id'";

        if ($kconn->query($sql) === TRUE) {
            echo'._.';
        }
    }
} elseif ($new == TRUE) {

} elseif ($delte == TRUE) {

} else {
}

?>