CREATE SCHEMA my_schema;
CREATE TABLE my_schema.teachers (
    teacher_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100)
);
INSERT INTO my_schema.teachers (first_name, last_name, email)
VALUES
    ('John', 'Doe', 'john.doe@example.com'),
    ('Jane', 'Smith', 'jane.smith@example.com'),
    ('Michael', 'Johnson', 'michael.johnson@example.com');

