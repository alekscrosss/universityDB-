SELECT DISTINCT sb.name
FROM subjects sb
JOIN grades gr ON sb.subject_id = gr.subject_id
WHERE gr.student_id = [student_id] AND sb.teacher_id = [teacher_id];