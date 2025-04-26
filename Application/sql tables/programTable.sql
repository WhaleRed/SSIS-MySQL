CREATE TABLE program (
	program_code VARCHAR(10) NOT NULL,
    program_name VARCHAR(128)NOT NUlL,
    college_code VARCHAR(10),
    
    PRIMARY KEY (program_code),
    FOREIGN KEY (college_code) REFERENCES college(college_code) ON DELETE SET NULL ON UPDATE CASCADE,
    UNIQUE (program_name)
);