<html>
<body>

<?php
$servername = "localhost";
$username = "16813096_main";
$passwrd = "Zantyr321";
$conn = new mysqli($servername, $username, $passwrd);
if ($_SERVER["REQUEST_METHOD"] == "POST") {
	$lg = $_POST['login'];
	$pss = $_POST['password'];
}
if (mysqli_connect_error()) {
    die("Connection failed: " . mysqli_connect_error());
}

echo "Connected successfully <br> $lg $pss <br>";

$sql = "SELECT * FROM 16813096_main.login";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
        echo "id: " . $row["id"]. " - Name: " . $row["login"]. " " . $row["password"]. "<br>";
    }
} else {
    echo "0 results";
}

mysqli_close($conn);

?>
</body>
</html>