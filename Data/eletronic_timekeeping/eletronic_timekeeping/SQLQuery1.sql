CREATE DATABASE EletronicTimekeeping;

CREATE TABLE tbEmployees
( 
	employee_number     int            NOT NULL    IDENTITY(1,1),
	employee_name              varchar(100)   NOT NULL,
	job_title           varchar(20),
	hire_date           date,
	CONSTRAINT pktbEmployees PRIMARY KEY(employee_number)
);

CREATE TABLE tbTimeRecords
(
	id_record            int          NOT NULL   IDENTITY(2001,1),
	employee_number      int          NOT NULL,
	date_record          date         NOT NULL,
	start_time           time         NOT NULL,
	lunch_start          time         NOT NULL,
	lunch_end            time         NOT NULL,
	end_time             time         NOT NULL,
	hours_worked         time         NOT NULL,
	CONSTRAINT pktbTimeRecords PRIMARY KEY(id_record),
	CONSTRAINT fktbTimeRecords FOREIGN KEY(employee_number)
	REFERENCES tbEmployees(employee_number)
);

-- Rodei para ajustar os nomes das colunas
EXEC sp_rename 'tbEmployees.[name]', 'employee_name', 'COLUMN';
EXEC sp_rename 'tbTimeRecords.[date]', 'date_record', 'COLUMN';

INSERT INTO tbEmployees (employee_name, job_title, hire_date)
VALUES 
('Andréia Barbosa', 'Engenheira Dados I', '2025/03/20'),
('Felipe Carvalho', 'Artista Tecnico III', '2024/02/18');

SELECT * FROM tbEmployees;
SELECT * FROM tbTimeRecords;

BULK INSERT dbo.tbTimeRecords
FROM 'C:\Users\TheWinterWitch\Documents\Estudos_programacao\Python\electronic_timekeeping_system\data\AdataNew.csv'
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDTERMINATOR = ';',
    ROWTERMINATOR = '0x0a',
    TABLOCK
);

CREATE TABLE #TestTimeRecords
(
	employee_number      int          NOT NULL,
	date_record          date         NOT NULL,
	start_time           time         NOT NULL,
	lunch_start          time         NOT NULL,
	lunch_end            time         NOT NULL,
	end_time             time         NOT NULL,
	hours_worked         time         NOT NULL,
);


SELECT * FROM #TestTimeRecords;

BULK INSERT dbo.#TestTimeRecords
FROM 'C:\Users\TheWinterWitch\Documents\Estudos_programacao\Python\electronic_timekeeping_system\data\AdataNew.csv'
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDTERMINATOR = ';',
    ROWTERMINATOR = '0x0a',
    TABLOCK
);

INSERT INTO tbTimeRecords (employee_number, date_record,start_time, lunch_start, lunch_end, end_time,hours_worked)
SELECT employee_number, date_record,start_time, lunch_start, lunch_end, end_time,hours_worked
FROM #TestTimeRecords;


-- AJUSTAR AS HORAS
ALTER TABLE tbTimeRecords
ALTER COLUMN start_time TIME(0);

ALTER TABLE tbTimeRecords
ALTER COLUMN lunch_start TIME(0);

ALTER TABLE tbTimeRecords
ALTER COLUMN lunch_end TIME(0);

ALTER TABLE tbTimeRecords
ALTER COLUMN end_time TIME(0);

ALTER TABLE tbTimeRecords
ALTER COLUMN hours_worked TIME(0);