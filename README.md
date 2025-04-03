# SSIS-MySQL
SSIS with MySQL

# TABLES

```
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



CREATE TABLE program (
	program_code VARCHAR(10) NOT NULL,
    program_name VARCHAR(128)NOT NUlL,
    college_code VARCHAR(10),
    
    PRIMARY KEY (program_code),
    FOREIGN KEY (college_code) REFERENCES college(college_code) ON DELETE SET NULL ON UPDATE CASCADE,
    UNIQUE (program_name)
);



CREATE TABLE college (
	college_code VARCHAR(10),
    college_name VARCHAR(128), 
    
    PRIMARY KEY	(college_code),
    UNIQUE (college_name) 
);
```