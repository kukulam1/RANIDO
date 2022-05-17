
CREATE TABLE Jobs (
    name varchar(255) NOT NULL PRIMARY  KEY,
    salary int
);

CREATE TABLE Persons (
    id SERIAL PRIMARY KEY,
    name varchar(255) NOT NULL,
    age int,
    job varchar(255) NOT NULL,
    FOREIGN KEY (job) REFERENCES Jobs(name)
);

INSERT INTO Jobs VALUES
    ('IT', 5000),
    ('Seller', 10000),
    ('Manager', 20000)
;

INSERT INTO Persons ( name, age, job) VALUES
    ('Matej', 24, 'IT'),
    ('Jan', 17, 'Seller'),
    ('Anna', 35, 'Manager'),
    ('Hana', 62, 'IT')
;



