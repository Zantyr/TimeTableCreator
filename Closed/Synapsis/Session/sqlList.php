CREATE DATABASE PlayGround;
CREATE TABLE Users(id INTEGER, login VARCHAR(32),firstName VARCHAR(32), age SMALLINT, desciptor VARCHAR(64), lastName VARCHAR(32), password VARCHAR(32), about XML, interests MULTISET);
CREATE TABLE Events(id INTEGER);
CREATE TABLE Groups(id INTEGER, admin INTEGER, users MULTISET);


UserObjects:
CREATE TABLE <userId>Feed(id INTEGER, content VARCHAR(4096));
CREATE TABLE <eventId>Feed(id INTEGER, content VARCHAR(4096));
CREATE TABLE <groupId>Feed(id INTEGER, content VARCHAR(4096));
CREATE TABLE <userId>Photos(id INTEGER, description VARCHAR(4096), usersOnPhoto MULTISET);
CREATE TABLE <eventId>Photos(id INTEGER, description VARCHAR(4096), usersOnPhoto MULTISET);
CREATE TABLE <groupId>Photos(id INTEGER, description VARCHAR(4096), usersOnPhoto MULTISET);
