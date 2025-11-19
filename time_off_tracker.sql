CREATE DATABASE IF NOT EXISTS time_off_tracker;
USE time_off_tracker;

DROP TABLE IF EXISTS TimeOffRequests;
DROP TABLE IF EXISTS Employees;

CREATE TABLE Employees(
	employee_id INT AUTO_INCREMENT PRIMARY KEY,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL, 
	department VARCHAR(50),
	accrued_days INT DEFAULT 15 NOT NULL
);

CREATE TABLE TimeOffRequests(
	request_id INT AUTO_INCREMENT PRIMARY KEY,
	employee_id INT NOT NULL,
	start_date DATE	NOT NULL,
	end_date DATE NOT NULL,
	request_status VARCHAR(20) DEFAULT 'Pending',
	days_requested INT AS (DATEDIFF(end_date,start_date) + 1) STORED,
	FOREIGN KEY(employee_id)
	REFERENCES Employees(employee_id)
);

INSERT INTO Employees (first_name, last_name, department, accrued_days) VALUES
('Alice', 'Johnson', 'Marketing', 10),
('Bob', 'Smith', 'Sales', 20),
('Charlie', 'Brown', 'Engineering', 15),
('Diana', 'Prince', 'Marketing', 5);


INSERT INTO TimeOffRequests (employee_id, start_date, end_date, request_status) VALUES
(1, '2025-12-01', '2025-12-03', 'Pending'),   -- Alice, 3 days
(2, '2025-11-20', '2025-11-21', 'Approved'),  -- Bob, 2 days
(3, '2025-12-24', '2025-12-26', 'Pending'),   -- Charlie, 3 days
(4, '2025-11-25', '2025-11-25', 'Pending');   -- Diana, 1 day



SELECT employee_id, first_name, last_name, accrued_days FROM Employees;

SELECT
    r.request_id,
    e.first_name,
    e.last_name,
    r.start_date,
    r.days_requested,
    r.request_status
FROM TimeOffRequests AS r
JOIN Employees AS e 
ON r.employee_id = e.employee_id
WHERE r.request_status = 'Pending';


SELECT * FROM Employees WHERE employee_id = 1;

UPDATE TimeOffRequests
SET request_status = 'Approved'
WHERE request_id = 1;

UPDATE Employees AS e
JOIN TimeOffRequests r 
ON e.employee_id = r.employee_id
SET e.accrued_days = e.accrued_days - r.days_requested
WHERE r.request_id = 1;


SELECT * FROM Employees WHERE employee_id = 1;


SELECT first_name, last_name, department, accrued_days
FROM Employees
WHERE accrued_days < 5;


SELECT
    e.department,
    SUM(r.days_requested) AS total_approved_days_taken
FROM Employees e
JOIN TimeOffRequests r ON e.employee_id = r.employee_id
WHERE e.department = 'Marketing' AND r.request_status = 'Approved'
GROUP BY e.department;

