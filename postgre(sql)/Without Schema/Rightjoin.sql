SELECT 
    t.teacher_id AS teacher_id,
    t.first_name AS teacher_first_name,
    t.last_name AS teacher_last_name,
    s.student_id AS student_id,
    s.first_name AS student_first_name,
    s.last_name AS student_last_name
FROM students s
RIGHT JOIN teachers t ON t.teacher_id = s.student_id;
