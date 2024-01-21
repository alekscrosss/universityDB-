-- Замени на нужныйе ид 
SELECT s.name, gr.grade
FROM grades gr
JOIN students s ON gr.student_id = s.student_id
WHERE s.group_id = [group_id] AND gr.subject_id = [subject_id];
