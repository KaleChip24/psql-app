DROP TABLE IF EXISTS memes;

CREATE TABLE memes (
  id SERIAL PRIMARY KEY,
  bottomText VARCHAR(255),
  image VARCHAR(255),
  name VARCHAR(255),
  rank INTEGER,
  tags VARCHAR(255),
  topText VARCHAR(255)
);