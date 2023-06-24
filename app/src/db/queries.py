SALES = '''SELECT cars.car_name AS car,
                        suppliers.supplier_name AS supplier,
                        price AS price
                FROM sales
                JOIN cars
                        ON sales.car_id = cars.car_id
                JOIN suppliers
                        ON sales.supplier_id = suppliers.supplier_id'''

CARS = "SELECT * FROM cars"

SUPPLIERS = "SELECT * FROM suppliers"