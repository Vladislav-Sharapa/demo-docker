CREATE TABLE cars(
    car_id serial PRIMARY KEY,
    car_name VARCHAR(30) NOT NULL
);

CREATE TABLE suppliers(
    supplier_id serial PRIMARY KEY,
    supplier_name VARCHAR(30) NOT NULL
);

CREATE TABLE sales (
	id serial PRIMARY KEY,
	car_id INT NOT NULL REFERENCES cars(car_id) ON DELETE CASCADE,
	supplier_id INT NOT NULL REFERENCES suppliers(supplier_id) ON DELETE CASCADE,
	price INT NOT NULL
);

INSERT INTO cars(
    car_name 
)
VALUES
    ('BMW'),
    ('Volvo'),
    ('Geely');

INSERT INTO suppliers(
    supplier_name
)
VALUES
    ('Logistics'),
    ('Via Motors'),
    ('Brunmers');


INSERT INTO sales(
    car_id,
    supplier_id,
    price
)
VALUES
    (1, 1, 350),
    (1, 2, 325),
    (2, 3, 285),
    (3, 1, 300),
    (2, 1, 320),
    (2, 2, 330);