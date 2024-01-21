-- Замени на нужный ид
SELECT AVG(gr.grade) AS average_grade
FROM grades gr
JOIN subjects sb ON gr.subject_id = sb.subject_id
WHERE sb.teacher_id = [teacher_id];
