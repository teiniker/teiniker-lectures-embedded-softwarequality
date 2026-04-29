DROP TABLE IF EXISTS messages;

CREATE TABLE messages
(
    address  INTEGER PRIMARY KEY,
    priority INTEGER NOT NULL,
    data     TEXT    NOT NULL
);

INSERT INTO messages (address, priority, data) VALUES (1123, 2, 'voltage=3.4V');
INSERT INTO messages (address, priority, data) VALUES (1124, 2, 'voltage=1.3V');
INSERT INTO messages (address, priority, data) VALUES (1125, 1, 'voltage=-1.7V');
