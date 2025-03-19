CREATE TABLE lectures (
    id INTEGER,
    title TEXT NOT NULL,
    ects INTEGER NOT NULL,
    sws INTEGER NOT NULL,
    PRIMARY KEY(id)
);

INSERT INTO lectures (id,title,ects,sws) VALUES (1, 'Mathematical Methods in Test Engineering', 6, 4);
INSERT INTO lectures (id,title,ects,sws) VALUES (2, 'Software Environments and Programming', 6, 4);
INSERT INTO lectures (id,title,ects,sws) VALUES (3, 'Digital Electronics', 6, 4);
INSERT INTO lectures (id,title,ects,sws) VALUES (4, 'Mixed-Signal Electronics', 6, 4);
INSERT INTO lectures (id,title,ects,sws) VALUES (5, 'System Requirements and Testing', 6, 4);
