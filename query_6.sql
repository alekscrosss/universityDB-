-- Замени [group_id] на ид группы скобки не нужны
SELECT s.name
FROM students s
WHERE s.group_id = [group_id]; -- Напиример [group_id] на 2