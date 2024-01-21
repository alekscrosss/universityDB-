-- subject_id = 1 - Выбери ид предмета
SELECT student_id, AVG(grade) as avg_grade
FROM grades
WHERE subject_id = 1
GROUP BY student_id
ORDER BY avg_grade DESC
LIMIT 1;
