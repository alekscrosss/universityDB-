-- [subject_id] = ид предмета, замени [subject_id] на 1 или 2 или 3 ....
SELECT g.group_name, AVG(gr.grade) AS average_grade
FROM grades gr
JOIN students s ON gr.student_id = s.student_id
JOIN groups g ON s.group_id = g.group_id
WHERE gr.subject_id = [subject_id]
GROUP BY g.group_id;