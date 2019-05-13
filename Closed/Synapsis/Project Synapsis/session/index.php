<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"></meta>
<title>Nowy Layout Bloga Ariocha</title>
<link rel="stylesheet" type="text/css" href="main.css">
</head>
<body>
<div class="menu" width="100%">
	<div class="left-menu">
		<a><p>Strona Gówna Pejsbuka</p></a>
		<div class="menu-content">
			<a href="profile.html"><p>Profile</p></a>
			<a href="#"><p>My Files</p></a>
		</div>
	</div>
	<div class="center-menu">
		<form method="POST" action="#">
			<table><tr>
			<td class="search-input"><input type="text" name="query" placeholder="Wszystko tutaj to mock-upy!" required></td>
			<td class="search-submit"><input type="submit" name="input" value="search"></td>
			</tr></table>
		</form>
	</div> 
	<div class="right-menu">
		<a href="#"><p>Logout</p></a>
		<div class="menu-content">
			<div class="menu-account">
				<div class="menu-account-image-block">
					<img src="rip.jpg" class="menu-account-image" alt="Twój portret" title="To Ty, chujku">
				</div>
				<div class="menu-account-name-block">
					<p class="menu-account-name"><b>Paweł Tomasik</b></p>
					<p class="menu-account-status"><i>Webmaster i mistrz świata</i></p>
				</div>
			</div>
			<a href="#"><p>Settings</p></a>
			<a href="#"><p>Log the fuck out</p></a>
		</div>
	</div>	
</div>
<div class="content" width="100%">
	<div class="post-form">
		<form class="post" method="POST" action="#">
			<div class="post-textarea-fake" contenteditable name="content">Ten mock-up nie działa</div>
			<input class="post-submit" type="submit" name="input" value="Tostuj"></td>			
		</form>
	</div>
<?php
$servername = "localhost";
$username = "16813096_main";
$passwrd = "Zantyr321";
$conn = new mysqli($servername, $username, $passwrd);
if (mysqli_connect_error()) {
    die("Connection failed: " . mysqli_connect_error());
}

$sql = "SELECT * FROM 16813096_main.blong ORDER BY id DESC";
$result = $conn->query($sql);

if ($result->num_rows > 0) 
{
    while($row = mysqli_fetch_assoc($result))
	{
		$title = $row["title"];
		$text = $row["text"];
		echo "	<div class=\"feed\">
		<div class=\"feed-element\">
			<div class=\"feed-element-author\"><b>";
		echo $title;
		echo "			</b></div>";
		echo $text;
		echo "			<div class=\"feed-element-like-comment-rip\">
			<a href=\"#\">Like</a>&middot;
			<a href=\"#\">Comment</a>&middot;
			<a href=\"#\">Subscrub</a>
			</div>
		</div>
	</div>";
    	}
}
else
{
die("Cos jeblo, nie ma wyszukiwan<br>");
}
?>

</div>
</body>
</html>
