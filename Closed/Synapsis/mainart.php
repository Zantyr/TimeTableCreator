<!DOCTYPE html>
<html>
<head>
<title>The Lair of Arioch</title>
<meta content="text/html" charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" type="text/css" href="index.css">
</head>

<body>

<div id="center"><h1><a href="index.php">
The Lair Of Arioch
</a></h1></div>

<div id="menu">
<?php
include "menu.php";
?>
</div>

<br>
<div id="column">
<?php

$servername = "localhost";
$username = "16813096_main";
$passwrd = "Zantyr321";
$conn = new mysqli($servername, $username, $passwrd);
if (mysqli_connect_error()) {
    die("Connection failed: " . mysqli_connect_error());
}

$sql = "SELECT * FROM 16813096_main.art ORDER BY id DESC";
$result = $conn->query($sql);

if ($result->num_rows > 0) 
{
    while($row = mysqli_fetch_assoc($result))
	{
		{
			echo "<a href='art.php?post=" . $row["id"] . "'>";
			echo $row["title"];
			echo "</a><br>";
			
		}
    	}
}
else
{
die("Cos jeblo, nie ma wyszukiwan<br>");
}

echo "<br>by Zantur";

?>
</div>

<br>

<br>
<div id="footer">
Layout by Arioch
</div>

</body>
</html>


