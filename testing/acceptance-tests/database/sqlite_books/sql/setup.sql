CREATE TABLE book
(
    isbn TEXT PRIMARY KEY,
    title TEXT,
    authors TEXT,
    publisher TEXT,
    year INTEGER
);

INSERT INTO book (isbn, title, authors, publisher, year)
    VALUES ('1449355730', 'Learning Python: Powerful Object-Oriented Programming', 'Mark Lutz', 'OReilly', 2013);
INSERT INTO book (isbn, title, authors, publisher, year)
    VALUES ('1593279280', 'Python Crash Course', 'Eric Matthes', 'No Starch Press', 2019);

-- BEGIN TRANSACTION;
-- test_method()
-- ROLLBACK;