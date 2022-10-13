--
-- File generated with SQLiteStudio v3.3.3 on vie. oct. 7 13:44:40 2022
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: user
CREATE TABLE user (
    id       INTEGER       PRIMARY KEY
                           NOT NULL,
    usuario  VARCHAR (110) NOT NULL,
    password CHAR (110)    NOT NULL,
    nombre   VARCHAR (110) NOT NULL
);

INSERT INTO user (
                     id,
                     usuario,
                     password,
                     nombre
                 )
                 VALUES (
                     1087113476,
                     'equipo14mintic@gmail.com',
                     'pbkdf2:sha256:260000$bc5zFLzCFpik6ccw$d6273ac886dd0b72ec6ed7a227826e5388866e48b6fb4a98e62e147d9d686ef5',
                     'Segundo Arboleda'
                 );


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
