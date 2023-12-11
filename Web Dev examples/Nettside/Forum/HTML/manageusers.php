<?php
session_start();
include'../PHP/rolereq.php/';
include'/var/opt/safe/connect.php';
$id = $_SESSION['id'];

$sql = "SELECT id, voted, role, username, firstname, lastname, email FROM users";
$result = $conn->query($sql);

?>

<!DOCTYPE html>
<html lang="en">
<head>  
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Manage users</title>
</head>
<body>
<?php
echo "<table border='1'>
<tr>
<th>User ID</th>
<th>Username</th>
<th>Firstname</th>
<th>Lastname</th>
<th>Email</th>
<th>Vote status</th>
<th>Role</th>
</tr>";

while($row = mysqli_fetch_array($result))
{
echo "<tr>";
echo "<td>" . $row['id'] . "</td>";
echo "<td>" . $row['username'] . "</td>";
echo "<td>" . $row['firstname'] . "</td>";
echo "<td>" . $row['lastname'] . "</td>";
echo "<td>" . $row['email'] . "</td>";
echo "<td>" . $row['voted'] . "</td>";
echo "<td>" . $row['role'] . "</td>";
echo "</tr>";
}
echo "</table>";

mysqli_close($con);
?>

<form action="../PHP/manage.php" method="post">
<input type="text" placeholder="ID" name="id" id="id">
<input type="submit" value="Ban" name="ban" id="ban">
</form>
<?php
if (!empty($_SESSION['banconf'])) {
    print_r($_SESSION['banconf']);
}
?>
<form action="../PHP/manage.php" method="post">
<input type="text" placeholder="ID" name="id" id="id">
<select name="rank" id="rank">
    <option value="member">Member</option>
    <option value="basic">Basic</option>
    <option value="vip">VIP</option>
    <option value="mvp">MVP</option>
    <option value="mvp++">MVP++</option>
    <option value="admin">Admin</option>
    <option value="owner">Owner</option>
</select>
<br> <input type="submit" value="Update">
</form>
<?php 
if (!empty($_SESSION['rankconf'])) {
    print_r($_SESSION['rankconf']);
}
?>
</body>
</html>