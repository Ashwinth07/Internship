SELECT *
FROM my_schema.teachers AS t
INNER JOIN my_schema.students AS s ON t.teacher_id = s.teacher_id;
