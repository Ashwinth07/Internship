CREATE TABLE my_schema.students (
    student_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    teacher_id INT REFERENCES my_schema.teachers(teacher_id)
);
INSERT INTO my_schema.students (first_name, last_name, email, teacher_id)
VALUES
    ('Alice', 'Johnson', 'alice@example.com', 1),
    ('Bob', 'Smith', 'bob@example.com', 2),
    ('Eva', 'Garcia', 'eva@example.com', 1);