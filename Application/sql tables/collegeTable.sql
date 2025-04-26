CREATE TABLE college (
	college_code VARCHAR(10),
    college_name VARCHAR(128), 
    
    PRIMARY KEY	(college_code),
    UNIQUE (college_name) 
);