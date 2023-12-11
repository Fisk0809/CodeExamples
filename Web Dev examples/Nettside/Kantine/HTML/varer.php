<?php
session_start();


include'../PHP/adminreq.php';
include'../DB/kconnect.php';
$vsql = "SELECT id, vare, pris FROM kantineDB.varer";
$vresult = $kconn->query($vsql);

$vnumrows = $vresult->num_rows;
$vnumrows = (int)$vnumrows;

$rsql = "SELECT id, rett, pris, dag FROM kantineDB.retter";
$rresult = $kconn->query($rsql);

$rnumrows = $rresult->num_rows;
$rnumrows = (int)$rnumrows;

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../CSS/style.css">
    <link rel="stylesheet" href="../CSS/header.css">
    <link rel="shortcut icon" href="../Images/favicon.ico" type="image/x-icon">
    <title>Kantine</title>
</head>
<body>
    <div class="container">
        <div class="background">
        <img src="../Images/banner-background-image.svg" alt="">
          </div>
          <div class="header">
            <div class="header-wrapper-upper"></div>
            <div class="header-wrapper-lower-outer">
                <div class="header-wrapper-lower-inner">
                    <div class="header-content">
                        <div class="logo">
                        <a id="hamarlogo" href="/">
                                    <span class="custom-logo">
                                      <img alt="Hamar katedralskole" src="../Images/hamar-katedralskole.svg">
                                    </span>
                                  </a>
                        </div>
                        <div class="navigation">
                            <div class="navigation-buttons">
                            <ul>
                                    <li><a href="retter.php">Retter</a></li>
                                    <li><a href="varer.php">Varer</a></li>
                                    <li><a href="login.php">Administer</a></li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
<div class="varer">
    <table border="2">
    <tr>
        <td>Sr.No.</td>
        <td>Vare</td>
        <td>Pris</td>
        <td>Edit</td>
        <td>Delete</td>
    </tr>
  
        <?php
        while($vdata = mysqli_fetch_array($vresult)) {
        ?>
        <div class="info" id="info">
        <tr>
            <td><?php echo $vdata['id']; ?></td>
            <td><?php echo $vdata['vare']; ?></td>
            <td><?php echo $vdata['pris']; ?></td>
            <td><a href="../PHP/edit.php?id=<?php echo $vdata['id']; ?>">Edit</a></td>
            <td><a href="../PHP/delete.php?id=<?php echo $vdata['id']; ?>">Delete</a></td>
        </tr>
        </div>
    <?php
    }
    ?>
    </table>
  </div>
</div>
</body>
</html>