SELECT AVG(gr.grade) AS average_grade
FROM grades gr
JOIN subjects sb ON gr.subject_id = sb.subject_id
JOIN students s ON gr.student_id = s.student_id
WHERE sb.teacher_id = 2 AND s.student_id = 4;
