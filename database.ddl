CREATE TABLE station (
	naam varchar(50) NOT NULL, 
	land varchar(2) NOT NULL,
	ovFiets boolean NOT NULL,
	lift boolean NOT NULL,
	wc boolean NOT NULL,
	parkerenPlusRijden boolean NOT NULL,
	
	PRIMARY KEY (naam)
);

CREATE TABLE moderator (
	moderatorNummer serial NOT NULL,
	wachtwoord varchar(255) NOT NULL,
	email varchar(255) NOT NULL,
	naam varchar(255) NOT NULL,
	
	PRIMARY KEY (moderatorNummer)
);

CREATE TABLE bericht (
	berichtNummer serial NOT NULL,
	bericht varchar(255) NOT NULL,
	datum date NOT NULL,
	tijd time NOT NULL,
	naam varchar(255) DEFAULT 'Anoniem',
	station varchar(50) NOT NULL,
	
	PRIMARY KEY (berichtNummer),
	FOREIGN KEY (station) REFERENCES station(naam)
)