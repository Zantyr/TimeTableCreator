<?php

session_start();

$dbAddress = "";
$dbLogin = "";
$dbPassword = "";
$dbDatabase = "";

$dbConn = new mysqli($dbAddress, $dbLogin, $dbPassword, $dbDatabase);
if($dbConn->connect_errno)
{
	die "No connection.<br>";
}

$sqlList = array();
$sqlList[] = "First SQL";
$sqlList[] = "Second SQL";
$sqlList[] = "Third SQL";

$nonProcessedSql = array();

foreach($sqlList as $sql)
{
	if($dbConn->query($sql) === true)
	{
		echo ("SQL query correct: " . $sql . "<br>");
	}
	else
	{
		echo ("ERROR when executing query: " . $sql . "<br>");
		$nonProcessedSql[] = $sql;
	}
}

?>
