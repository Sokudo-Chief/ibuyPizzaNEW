CREATE TABLE IF NOT EXISTS burgeri (
    id INTEGER PRIMARY KEY,
    photo BLOB NOT NULL,
    name TEXT NOT NULL,
    description TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS bulochki (
    id INTEGER PRIMARY KEY,
    photo BLOB NOT NULL,
    name TEXT NOT NULL,
    description TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS reviews (
    id INTEGER PRIMARY KEY,
    review TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS zakaz_bulochki (
    id INTEGER PRIMARY KEY,
    eda_id INTEGER NOT NULL,
    adress TEXT NOT NULL,
    name TEXT NOT NULL,
    number INTEGER NOT NULL,
    comment TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS zakaz_burgeri (
    id INTEGER PRIMARY KEY,
    eda_id INTEGER NOT NULL,
    adress TEXT NOT NULL,
    name TEXT NOT NULL,
    number INTEGER NOT NULL,
    comment TEXT NOT NULL
);