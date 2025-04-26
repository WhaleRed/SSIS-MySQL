CREATE TABLE student (
	student_id VARCHAR(10) NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    year_level INT NOT NULL,
    gender VARCHAR(50) NOT NULL,
    program_code VARCHAR(10),
    
    PRIMARY KEY (student_id),
	FOREIGN KEY (program_code) REFERENCES program(program_code) ON DELETE SET NULL ON UPDATE CASCADE 
);