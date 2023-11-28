CREATE VIEW my_schema.students_info AS
SELECT 
    student_id,
    first_name,
    last_name,
    email
FROM my_schema.students;
SELECT * FROM my_schema.students_info;

