DROP TABLE IF EXISTS works;
DROP TABLE IF EXISTS museums;

CREATE TABLE museums (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  address VARCHAR(255)
);

CREATE TABLE works (
  id SERIAL PRIMARY KEY,
  title VARCHAR(255) NOT NULL,
  artist VARCHAR(255) NOT NULL,
  museum_id INT REFERENCES museums(id),
  year INT
);


INSERT INTO museums (name, address) VALUES ('Scottish National Gallery of Modern Art', '75 Belford Rd, EH4 3DR');
INSERT INTO museums (name, address) VALUES ('Scottish National Portrait Gallery', '1 Queen Street, EH2 1DJ');

INSERT INTO works (title, artist, year, museum_id) VALUES ('The Aficionado', 'Pablo Picasso', 1936, 1); 
INSERT INTO works (title, artist, year, museum_id) VALUES ('Lobster Telephone', 'Salvador Dali', 1905, 1); 
INSERT INTO works (title, artist, year, museum_id) VALUES ('Wild Shore', 'Frances Walker', 1905, 1); 
INSERT INTO works (title, artist, year, museum_id) VALUES ('Tutti Frutti', 'John Byrne', 1985, 2); 
INSERT INTO works (title, artist, year, museum_id) VALUES ('Romance', 'Cecile Walton', 1859, 2); 

