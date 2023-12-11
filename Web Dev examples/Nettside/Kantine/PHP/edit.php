<?php 
include'../DB/kconnect.php';

$id = $_GET['id'];
$update = $_POST['update'];
$vare = $_POST['vare'];
$pris = $_POST['pris'];

if ($update == TRUE) {
    if (!empty($vare)) {
        $sql = "UPDATE varer SET vare='$vare' WHERE id='$id'";

        if ($kconn->query($sql) === TRUE) {
        }
    }

    if (!empty($pris)) {
        $pris = $pris . "kr";
        $sql = "UPDATE varer set pris='$pris' WHERE id='$id'";

        if ($kconn->query($sql) === TRUE) {
            }
        } 
    header("Location: admin.php");
    } else {
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Edit</title>
</head>
<body>
    <form method="post">
    <label for="vare">Vare</label>
    <input type="text" class="input" name="vare">
    <label for="pris">Pris</label>
    <input type="text" class="input" name="pris">
    <input type="submit" value="Update" name="update">
    </form>
    
</body>
</html>