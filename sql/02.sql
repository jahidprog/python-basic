USE college;

INSERT INTO user
(ID, Name, Age, Email)
VALUES
(101, "Alice", 27, "alice@gmail.com"),
(102, "Bob", 27, "bob@gmail.com"),
(103, "Chi", 27, "chi@gmail.com"),
(104, "Dog", 27, "dog@gmail.com");

INSERT INTO user
(ID, Name, Age, Email, Followers, Following)
VALUES
(111, "Liam", 26, "liam@gmail.com", 450, 150),
(112, "Mia", 28, "mia@gmail.com", 890, 420),
(113, "Noah", 22, "noah@gmail.com", 1500, 310),
(114, "Olivia", 25, "olivia@gmail.com", 320, 95),
(115, "Paul", 29, "paul@gmail.com", 780, 540),
(116, "Quinn", 24, "quinn@gmail.com", 650, 210),
(117, "Ruby", 27, "ruby@gmail.com", 410, 180),
(118, "Sam", 31, "sam@gmail.com", 2300, 890),
(119, "Tina", 23, "tina@gmail.com", 120, 340),
(120, "Uma", 26, "uma@gmail.com", 990, 450),
(121, "Vince", 33, "vince@gmail.com", 3400, 1100),
(122, "Wendy", 20, "wendy@gmail.com", 55, 120),
(123, "Xander", 27, "xander@gmail.com", 1450, 670),
(124, "Yara", 25, "yara@gmail.com", 820, 230),
(125, "Zack", 29, "zack@gmail.com", 610, 490),
(126, "Amber", 22, "amber@gmail.com", 310, 150),
(127, "Blake", 26, "blake@gmail.com", 950, 410),
(128, "Chloe", 24, "chloe@gmail.com", 1200, 380),
(129, "David", 30, "david@gmail.com", 430, 290),
(130, "Ella", 21, "ella@gmail.com", 760, 180),
(131, "Felix", 28, "felix@gmail.com", 1890, 620),
(132, "Grace", 23, "grace@gmail.com", 240, 90),
(133, "Harry", 27, "harry@gmail.com", 1100, 530),
(134, "Ivy", 25, "ivy@gmail.com", 670, 310),
(135, "Jack", 32, "jack@gmail.com", 2900, 980),
(136, "Kara", 22, "kara@gmail.com", 430, 210),
(137, "Leo", 26, "leo@gmail.com", 1340, 450),
(138, "Maya", 24, "maya@gmail.com", 890, 270),
(139, "Nate", 29, "nate@gmail.com", 520, 380),
(140, "Piper", 21, "piper@gmail.com", 180, 110);

SELECT * FROM user;

SELECT ID, Name, Age, Followers, Following, COUNT(*) OVER() as TotalUser FROM user
WHERE Followers >= 200
LIMIT 10;

SELECT ID, Name, Age, Email 
FROM user
WHERE Age NOT IN  (21, 24);


SELECT MAX(followers)
FROM user;

SELECT ID, Name, Followers 
FROM user 
ORDER BY Followers DESC
LIMIT 10;


SELECT age, MAX(Followers) as max_followers
FROM user
GROUP BY age
ORDER BY max_followers DESC;

SELECT age, MAX(Followers) as max_followers
FROM user
GROUP BY age 
HAVING max_followers > 2500;


UPDATE user
SET City = "DHK"
WHERE Followers > 1000;

ALTER TABLE user
ADD COLUMN City VARCHAR(30) DEFAULT "CTG";


ALTER TABLE instaUser
RENAME TO user;

ALTER TABLE user
CHANGE COLUMN Followers Subscriber INT DEFAULT 0;


SELECT * FROM user;

