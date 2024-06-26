# Some_problems_I_was_solving
Some task/problems i have solved
## Sql tasks

### 1) Выведите имя first_name и фамилию last_name каждого учителя из таблицы Teacher, а также количество занятий, в которых он был назначен преподавателем. Если преподаватель не был назначен ни на одно занятие, то выведите 0. 
select first_name, last_name,count(Schedule.subject) as amount_classes from Teacher
left join Schedule on Teacher.id = Schedule.teacher GROUP BY Teacher.first_name, Teacher.last_name;

