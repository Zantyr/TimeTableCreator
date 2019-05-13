<?php
$req_login = "SELECT * FROM ".$db_prefix."Users";
$req_friends = "SELECT * FROM ".$db_prefix.$user_id."UserFriends ORDER BY importance DESC";
$req_feed = "SELECT * FROM ".$db_prefix.$user_id."UserFeed ORDER BY id DESC";
$req_photos = "SELECT * FROM ".$db_prefix.$user_id."UserPhotos ORDER BY id DESC";
$req_photo = "SELECT * FROM ".$db_prefix."Photos WHERE photoId=".$photo_id;

function showUserPhoto()
{
}

function showParticularPhoto()
{
}

function createFeed()
{
	#creates and displays main feed for a user
	$friends = [];
	$result = $conn->query($req_friends);
}

function postFeed()
{
	#posts something on your personal feed
}



?>
