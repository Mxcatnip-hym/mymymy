#创建表
CREATE TABLE user (
    id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    sex VARCHAR(10),
    age INT,
    phone VARCHAR(15) UNIQUE
);

#插入
INSERT INTO user (id, name, sex, age, phone)
VALUES
    (1, '张三', '男', 25, '1234567890'),
    (2, '李四', '女', 22, '9876543210'),
    (3, '王五', '男', 30, '5555555555');

#删除
DELETE FROM user WHERE name LIKE '%张%';

#计算平均年龄
SELECT AVG(age) AS average_age FROM user;

#查询，并按年龄从大到小排序输出
SELECT * FROM user
WHERE age BETWEEN 20 AND 30 AND name LIKE '%张%'
ORDER BY age DESC;

#创建team表
CREATE TABLE team ( 
    id INT AUTO_INCREMENT PRIMARY KEY, 
    teamName VARCHAR(255) NOT NULL
 );

#创建score表
CREATE TABLE score ( 
    id INT AUTO_INCREMENT PRIMARY KEY, 
    teamid INT, 
    userid INT, 
    score INT, 
    FOREIGN KEY (teamid) REFERENCES team(id), 
    FOREIGN KEY (userid) REFERENCES user(id) 
);

#查询teamName为ECNU且年龄小于20
SELECT u.*
FROM user u
JOIN score s ON u.id = s.userid
JOIN team t ON s.teamid = t.id
WHERE t.teamName = 'ECNU' AND u.age < 20;

#查询teamName为ECNU的总分
SELECT COALESCE(SUM(score), 0) AS total_score
FROM score s
JOIN team t ON s.teamid = t.id
WHERE t.teamName = 'ECNU';






