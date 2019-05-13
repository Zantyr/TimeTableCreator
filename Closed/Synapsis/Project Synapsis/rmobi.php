<?php
echo("<html><head><title>Productivity Knight!</title><meta content='text/html' charset='utf-8'></head><body>");
$servername = "localhost";
$username = "16813096_main";
$passwrd = "Zantyr321";
$conn = new mysqli($servername, $username, $passwrd);
if (mysqli_connect_error()) {
    die("Connection failed: " . mysqli_connect_error());
}

if($_POST["logout"] != "")
{
	$_POST["login"] == "";
}
if($_POST["register"]!="")
{
	if($_POST["passwd"] != $_POST["repeat"])
	{
		die("Passwords are not identical! Press back!");
	}
	$_POST["login"]=$_POST["register"];
	$sql = "INSERT INTO 16813096_main.users VALUES ('".$_POST["register"]."', 0, 1,'".$_POST["passwd"]."')";
	$result = $conn->query($sql);
}
if($_POST["logen"] != "")
{
	$sql = "SELECT * FROM 16813096_main.users WHERE name = '". $_POST["logen"] . "'";
	$result = $conn->query($sql);
	if ($result->num_rows > 0) 
	{
	    while($row = mysqli_fetch_assoc($result))
		{
			if($row["name"] == $_POST["logen"])
			{
				if($row["pswd"] != $_POST["passwd"])
				{
					die("Password not valid!");
				}
			}
			$_POST["login"] = $_POST["logen"];
	    	}
	}
	else
	{
	die("User not found!<br>");
	}
}
if($_POST["login"] == "")
{
	die("<p><form action='rmobi.php' method='POST'>Log in: <div><input type='text' name='logen'><br><input type='password' name='passwd'></div><div><input type='submit' value='Log me in'></div></form></p><p><form action='rmobi.php' method='POST'>Register: <div><input type='text' name='register'><br><input type='password' name='passwd'><br><input type='password' name='repeat'></div><div><input type='submit' value='I want to begin the quest'></div></form></p>");
}

$name = $_POST["login"];
$sql = "SELECT * FROM 16813096_main.users WHERE name = '". $name . "'";
$result = $conn->query($sql);
if ($result->num_rows > 0) 
{
    while($row = mysqli_fetch_assoc($result))
	{
		if($row["name"] == $name)
		{
			$lvl = $row["lvl"];
			$xp = $row["xp"];
		}
    	}
}
else
{
die("No such hero!<br>");
}

$avance = false;
$added = false;

if($_POST["quest"] != "")
{
$qid = 0;
$sql = "SELECT * FROM 16813096_main.act";
$result = $conn->query($sql);
    while($row = mysqli_fetch_assoc($result))
	{
		if($row["id"] > $qid)
		{
			$qid = $row["id"];
		}
    	}
	$qid = $qid + 1;	
$sql = "INSERT INTO 16813096_main.act VALUES (".$qid.", '". $_POST["quest"] ."', '" . $name . "', " . $_POST["exp"] . ")";
$result = $conn->query($sql);
$added = true;
}

if($_POST["rid"] != "")
{
	$sql = "SELECT * FROM 16813096_main.act WHERE user = '" . $name . "'";
	$result = $conn->query($sql);
	if ($result->num_rows > 0) 
	{
	    while($row = mysqli_fetch_assoc($result))
		{
		if($row["id"] == $_POST["rid"])
			{
				$xp = $xp - $row["xp"];
				$sql = "DELETE FROM 16813096_main.act WHERE id = " . $_POST["rid"];
				$res = $conn->query($sql);
				$sql = "UPDATE 16813096_main.users SET lvl = ".$lvl.", xp = ".$xp." WHERE name = '" . $name . "'";
				$res = $conn->query($sql);
			}
	    	}
	}
	else
	{
	die("Some kind of error.<br>");
	}
	
}

if($_POST["id"] != "")
{
	$sql = "SELECT * FROM 16813096_main.act WHERE user = '" . $name . "'";
	$result = $conn->query($sql);
	if ($result->num_rows > 0) 
	{
	    while($row = mysqli_fetch_assoc($result))
		{
		if($row["id"] == $_POST["id"])
			{
				$xp = $xp + $row["xp"];
				if($xp > 10*$lvl)
				{
					$xp = $xp - (10*$lvl);
					$lvl = $lvl + 1;
					$avance = true;
				}
				$sql = "DELETE FROM 16813096_main.act WHERE id = " . $_POST["id"];
				$res = $conn->query($sql);
				$sql = "UPDATE 16813096_main.users SET lvl = ".$lvl.", xp = ".$xp." WHERE name = '" . $name . "'";
				$res = $conn->query($sql);
			}
	    	}
	}
	else
	{
	die("Some kind of error.<br>");
	}
	
}

echo("<p>Name: " . $name . "<br>Level: " . $lvl . "<br>Experience points: " . $xp . "<br></p>");
if($avance)
{
	echo("Congrats, you just advanced to the next level!<br><br>");
}
if($added)
{
	echo("A new quest added!<br><br>");
}
$sql = "SELECT * FROM 16813096_main.act WHERE user = '" . $name . "'";
$result = $conn->query($sql);

if ($result->num_rows > 0) 
{
    while($row = mysqli_fetch_assoc($result))
	{
		echo "<table><tr><td><form action=\"remind.php\" method=\"POST\"><input type='hidden' name='login' value='" . $name . "'><input type=\"hidden\" name=\"rid\" value=\"". $row["id"] ."\"><input type=\"submit\" value=\"Forfeit\"></form></td><td><form action=\"remind.php\" method=\"POST\"><input type='hidden' name='login' value='" . $name . "'><input type=\"hidden\" name=\"id\" value=\"". $row["id"] ."\"><input type=\"submit\" value=\"Done!\">&nbsp;&nbsp;[" . $row["xp"] . "]&nbsp;" . $row["text"] . "</form></td></tr></table>";
    	}
}
else
{
echo("No quests pending. Quickly, find a dragon to slay!<br><br>");
}



echo("<form action=\"rmobi.php\" method=\"POST\"><input type='hidden' name='login' value='" . $name . "'>Quest content: <input name='quest' type='text'><br>Experience to gain:<input name='exp' type='text'><br><input type=\"submit\" value=\"Gain a new quest!\"></form>");

echo("<form action=\"rmobi.php\" method=\"POST\"><input type='hidden' name='logout' value='true'><input type='submit' value='Logout'></form></body>
</html>");
?>
