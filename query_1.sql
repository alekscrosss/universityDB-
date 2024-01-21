SELECT s.student_id, s.name, AVG(g.grade) as avg_grade
FROM students s
JOIN grades g ON s.student_id = g.student_id
GROUP BY s.student_id
ORDER BY avg_grade DESC
LIMIT 5;