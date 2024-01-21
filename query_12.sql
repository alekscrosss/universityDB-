SELECT s.name, gr.grade
FROM grades gr
JOIN students s ON gr.student_id = s.student_id
WHERE s.group_id = 3 AND gr.subject_id = 1 
AND gr.date_received = (
    SELECT MAX(date_received)
    FROM grades
    WHERE subject_id = 1
);
