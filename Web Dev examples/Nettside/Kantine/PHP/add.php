<?php 
include'../DB/kconnect.php';

$vare = $_POST['vare'];
$pris = $_POST['pris'];
$submit = $_POST['submit'];

if (!empty($vare)) {
    if (!empty($pris)) {
        $pris = $pris . "kr";
        $sql = $kconn->prepare("INSERT INTO varer (vare, pris) VALUES (?, ?) ");
        $sql->bind_param("ss", $vare, $pris);

        if ($sql->execute() === TRUE) {
            $sql->close();
            $kconn->close();
            header("Location: ../HTML/admin.php");
        }

    } else {
        session_start();
        $_SESSION['error'] = "Pris må være definert";
        header("Location: ../HTML/admin.php");
    }
} else {
    session_start();
    $_SESSION['error'] = "Vare må være definert";
    header("Location: ../HTML/admin.php");
}


?>