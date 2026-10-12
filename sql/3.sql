-- Teacher and Student

CREATE TABLE teacher(
    Id INT PRIMARY KEY, 
    Name VARCHAR(30) NOT NULL,
    Subject VARCHAR(30) NOT NULL,
    Salary INT DEFAULT 25000
);

CREATE TABLE student(
    Id INT PRIMARY KEY, 
    Name VARCHAR(30) NOT NULL,
    Age INT,
    Subject VARCHAR(30), 
    TeacherID INT,
    FOREIGN KEY (TeacherID) REFERENCES Teacher(ID)
);

-- Insert 30 Teachers
INSERT INTO teacher (Id, Name, Subject, Salary) VALUES
(101, 'Rahim', 'Math', 30000),
(102, 'Karim', 'Physics', 32000),
(103, 'Salma', 'Chemistry', 28000),
(104, 'Tariq', 'English', 25000),
(105, 'Nasrin', 'Biology', 29000),
(106, 'Imran', 'History', 26000),
(107, 'Farhana', 'Geography', 27000),
(108, 'Kamal', 'Computer Science', 35000),
(109, 'Nusrat', 'Economics', 31000),
(110, 'Jahangir', 'Accounting', 29500),
(111, 'Sabina', 'Art', 24000),
(112, 'Ashraf', 'Physical Education', 25000),
(113, 'Moumita', 'Math', 30500),
(114, 'Tanvir', 'Physics', 33000),
(115, 'Roksana', 'Chemistry', 28500),
(116, 'Monir', 'English', 26000),
(117, 'Shahnaz', 'Biology', 29500),
(118, 'Rubel', 'History', 27000),
(119, 'Sumaiya', 'Geography', 28000),
(120, 'Faisal', 'Computer Science', 34000),
(121, 'Taslima', 'Economics', 32000),
(122, 'Al-Amin', 'Accounting', 30000),
(123, 'Sultana', 'Art', 24500),
(124, 'Belal', 'Physical Education', 25500),
(125, 'Farida', 'Math', 31000),
(126, 'Shahid', 'Physics', 31500),
(127, 'Nazma', 'Chemistry', 29000),
(128, 'Zakir', 'English', 26500),
(129, 'Parveen', 'Biology', 30000),
(130, 'Anis', 'Computer Science', 36000);

-- Insert 30 Students (with matching TeacherIDs)
INSERT INTO student (Id, Name, Age, Subject, TeacherID) VALUES
(101, 'Alice', 18, 'Math', 101),
(102, 'Bob', 19, 'Physics', 102),
(103, 'Charlie', 17, 'Chemistry', 103),
(104, 'Diana', 18, 'English', 104),
(105, 'Evan', 20, 'Biology', 105),
(106, 'Fiona', 19, 'History', 106),
(107, 'George', 18, 'Geography', 107),
(108, 'Hannah', 17, 'Computer Science', 108),
(109, 'Ian', 21, 'Economics', 109),
(110, 'Julia', 18, 'Accounting', 110),
(111, 'Kevin', 19, 'Art', 111),
(112, 'Laura', 18, 'Physical Education', 112),
(113, 'Michael', 20, 'Math', 113),
(114, 'Nora', 17, 'Physics', 114),
(115, 'Oscar', 19, 'Chemistry', 115),
(116, 'Penny', 18, 'English', 116),
(117, 'Quincy', 21, 'Biology', 117),
(118, 'Rachel', 18, 'History', 118),
(119, 'Steve', 19, 'Geography', 119),
(120, 'Tracy', 17, 'Computer Science', 120),
(121, 'Victor', 20, 'Economics', 121),
(122, 'Wanda', 18, 'Accounting', 122),
(123, 'Xavier', 19, 'Art', 123),
(124, 'Yvonne', 18, 'Physical Education', 124),
(125, 'Zach', 17, 'Math', 125),
(126, 'Amy', 19, 'Physics', 126),
(127, 'Brian', 20, 'Chemistry', 127),
(128, 'Cathy', 18, 'English', 128),
(129, 'Derek', 19, 'Biology', 129),
(130, 'Elena', 18, 'Computer Science', 130);


SELECT * FROM teacher;

SELECT COUNT(Id) as totalTeachers
FROM teacher;

SELECT COUNT(Id) as totalStudents
FROM student;

-- Group BY

SELECT TeacherID, COUNT(Id) 
FROM student
GROUP BY TeacherId, Id;

