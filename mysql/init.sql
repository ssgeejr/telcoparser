SET GLOBAL time_zone = 'America/Chicago';

USE telco;


create table export(
	dateorig char(32) NOT NULL DEFAULT '',
	timeorig char(32) NOT NULL DEFAULT '',
	origipaddr char(32) NOT NULL DEFAULT '',
	callingparty char(32) NOT NULL DEFAULT ''
);

