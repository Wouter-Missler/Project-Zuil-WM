/* tabel voor verschillende stations */
CREATE TABLE station (
	naam varchar(50) NOT NULL, 
	land varchar(2) NOT NULL,
	ovFiets boolean NOT NULL,
	lift boolean NOT NULL,
	wc boolean NOT NULL,
	parkerenPlusRijden boolean NOT NULL,
	
	PRIMARY KEY (naam)
);

/* tabel voor moderatoren */
CREATE TABLE moderator (
	moderatorNummer serial NOT NULL,
	wachtwoord varchar(255) NOT NULL,
	email varchar(255) NOT NULL,
	naam varchar(255) NOT NULL,
	
	PRIMARY KEY (moderatorNummer)
);

/* tabel voor berichten */
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

/* station inserts */
INSERT INTO station (
    stad, land, ovFiets, lift, wc, parkerenPlusRijden)
VALUES
    ('Arnhem', 'NL', true, false, true, false),
    ('Almere', 'NL', false, true, false, true),
    ('Amersfoort', 'NL', true, false, true, false),
    ('Almelo', 'NL', false, true, false, true),
    ('Alkmaar', 'NL', true, false, true, false),
    ('Apeldoorn', 'NL', false, true, false, true),
    ('Assen', 'NL', true, false, true, false),
    ('Amsterdam', 'NL', false, true, false, true),
    ('Boxtel', 'NL', true, false, true, false),
    ('Breda', 'NL', false, true, false, true),
    ('Dordrecht', 'NL', true, false, true, false),
    ('Delft', 'NL', false, true, false, true),
    ('Deventer', 'NL', true, false, true, false),
    ('Enschede', 'NL', false, true, false, true),
    ('Gouda', 'NL', true, false, true, false),
    ('Groningen', 'NL', false, true, false, true),
    ('Den Haag', 'NL', true, false, true, false),
    ('Hengelo', 'NL', false, true, false, true),
    ('Haarlem', 'NL', true, false, true, false),
    ('Helmond', 'NL', false, true, false, true),
    ('Hoorn', 'NL', true, false, true, false),
    ('Heerlen', 'NL', false, true, false, true),
    ('Den Bosch', 'NL', true, false, true, false),
    ('Hilversum', 'NL', false, true, false, true),
    ('Leiden', 'NL', true, false, true, false),
    ('Lelystad', 'NL', false, true, false, true),
    ('Leeuwarden', 'NL', true, false, true, false),
    ('Maastricht', 'NL', false, true, false, true),
    ('Nijmegen', 'NL', true, false, true, false),
    ('Oss', 'NL', false, true, false, true),
    ('Roermond', 'NL', true, false, true, false),
    ('Roosendaal', 'NL', false, true, false, true),
    ('Sittard', 'NL', true, false, true, false),
    ('Tilburg', 'NL', false, true, false, true),
    ('Utrecht', 'NL', true, false, true, false),
    ('Venlo', 'NL', false, true, false, true),
    ('Vlissingen', 'NL', true, false, true, false),
    ('Zaandam', 'NL', false, true, false, true),
    ('Zwolle', 'NL', true, false, true, false),
    ('Zutphen', 'NL', false, true, false, true);

/* moderator insert */
INSERT INTO moderator (
	naam, email, wachtwoord)
VALUES
	('Wouter Missler', 'woutermissler.missler@student.hu.nl', '1234')