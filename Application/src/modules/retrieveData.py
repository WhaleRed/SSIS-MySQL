import mysql.connector

#For edit
def retrieveStudent(studid):
  db = mysql.connector.connect(
    host="localhost",
    user = "root",
    password="jupiter'sfear",
    database="ssis"
    )

  mycursor = db.cursor()

  arr = []
  mycursor.execute("SELECT * FROM student WHERE student_id = %s", studid)
  for row in mycursor:
    arr.append(row[0])
    arr.append(row[1])
    arr.append(row[2])
    arr.append(row[3])
    arr.append(row[4])
    arr.append(row[5])
  db.close()
  return arr

def retrieveProgram(prog_code):
  db = mysql.connector.connect(
    host="localhost",
    user = "root",
    password="jupiter'sfear",
    database="ssis"
    )

  mycursor = db.cursor()

  arr = []
  mycursor.execute("SELECT * FROM program WHERE program_code = %s", prog_code)
  for row in mycursor:
    arr.append(row[0])
    arr.append(row[1])
    arr.append(row[2])
  db.close()
  return arr

def retrieveCollege(col_code):
  db = mysql.connector.connect(
    host="localhost",
    user = "root",
    password="jupiter'sfear",
    database="ssis"
    )

  mycursor = db.cursor()

  arr = []
  mycursor.execute("SELECT * FROM college WHERE college_code = %s", col_code)
  for row in mycursor:
    arr.append(row[0])
    arr.append(row[1])
  db.close()
  return arr

#For Table Population of Student

def retrieveNumberOfStudents():
  db = mysql.connector.connect(
    host="localhost",
    user = "root",
    password="jupiter'sfear",
    database="ssis"
    )

  mycursor = db.cursor()

  mycursor.execute("SELECT COUNT(student_id) FROM student")
  num = mycursor.fetchone()[0]
  db.close()
  return num

def retrieveStudentsIdSort(page, rows):
  db = mysql.connector.connect(
    host="localhost",
    user = "root",
    password="jupiter'sfear",
    database="ssis"
    )

  mycursor = db.cursor()

  offset = []
  off = (page-1) * rows
  offset.append(off)
  arr = []
  mycursor.execute("SELECT * FROM student ORDER BY student_id ASC LIMIT 50 OFFSET %s", offset)
  for row in mycursor:
    arr.append(row)
  db.close()
  return arr

def retrieveStudentsFnameSort(page, rows):
  db = mysql.connector.connect(
    host="localhost",
    user = "root",
    password="jupiter'sfear",
    database="ssis"
    )

  mycursor = db.cursor()

  offset = []
  off = (page-1) * rows
  offset.append(off)
  arr = []
  mycursor.execute("SELECT * FROM student ORDER BY first_name ASC LIMIT 50 OFFSET %s", offset)
  for row in mycursor:
    arr.append(row)
  db.close()
  return arr

def retrieveStudentsLnameSort(page, rows):
  db = mysql.connector.connect(
    host="localhost",
    user = "root",
    password="jupiter'sfear",
    database="ssis"
    )

  mycursor = db.cursor()

  offset = []
  off = (page-1) * rows
  offset.append(off)
  arr = []
  mycursor.execute("SELECT * FROM student ORDER BY last_name ASC LIMIT 50 OFFSET %s", offset)
  for row in mycursor:
    arr.append(row)
  db.close()
  return arr

def retrieveStudentsYearSort(page, rows):
  db = mysql.connector.connect(
    host="localhost",
    user = "root",
    password="jupiter'sfear",
    database="ssis"
    )

  mycursor = db.cursor()

  offset = []
  off = (page-1) * rows
  offset.append(off)
  arr = []
  mycursor.execute("SELECT * FROM student ORDER BY year_level ASC LIMIT 50 OFFSET %s", offset)
  for row in mycursor:
    arr.append(row)
  db.close()
  return arr

def retrieveStudentsGenderSort(page, rows):
  db = mysql.connector.connect(
    host="localhost",
    user = "root",
    password="jupiter'sfear",
    database="ssis"
    )

  mycursor = db.cursor()

  offset = []
  off = (page-1) * rows
  offset.append(off)
  arr = []
  mycursor.execute("SELECT * FROM student ORDER BY gender ASC LIMIT 50 OFFSET %s", offset)
  for row in mycursor:
    arr.append(row)
  db.close()
  return arr

def retrieveStudentsProgramSort(page, rows):
  db = mysql.connector.connect(
    host="localhost",
    user = "root",
    password="jupiter'sfear",
    database="ssis"
    )

  mycursor = db.cursor()

  offset = []
  off = (page-1) * rows
  offset.append(off)
  arr = []
  mycursor.execute("SELECT * FROM student ORDER BY program_code ASC LIMIT 50 OFFSET %s", offset)
  for row in mycursor:
    arr.append(row)
  db.close()
  return arr

#For table population of Program
def retrieveProgramCode():
  db = mysql.connector.connect(
    host="localhost",
    user = "root",
    password="jupiter'sfear",
    database="ssis"
    )

  mycursor = db.cursor()
  arr = []
  mycursor.execute("SELECT program_code FROM program ")
  for row in mycursor:
    arr.append(row)
  db.close()
  return arr

def retrieveNumberOfProgram():
  db = mysql.connector.connect(
    host="localhost",
    user = "root",
    password="jupiter'sfear",
    database="ssis"
    )

  mycursor = db.cursor()

  mycursor.execute("SELECT COUNT(program_code) FROM program")
  num = mycursor.fetchone()[0]
  db.close()
  return num

def retrieveProgramCodeSort(page, rows):
  db = mysql.connector.connect(
    host="localhost",
    user = "root",
    password="jupiter'sfear",
    database="ssis"
    )

  mycursor = db.cursor()

  offset = []
  off = (page-1) * rows
  offset.append(off)
  arr = []
  mycursor.execute("SELECT * FROM program ORDER BY program_code ASC LIMIT 25 OFFSET %s", offset)
  for row in mycursor:
    arr.append(row)
  db.close()
  return arr

def retrieveProgramNameSort(page, rows):
  db = mysql.connector.connect(
    host="localhost",
    user = "root",
    password="jupiter'sfear",
    database="ssis"
    )

  mycursor = db.cursor()

  offset = []
  off = (page-1) * rows
  offset.append(off)
  arr = []
  mycursor.execute("SELECT * FROM program ORDER BY program_name ASC LIMIT 25 OFFSET %s", offset)
  for row in mycursor:
    arr.append(row)
  db.close()
  return arr

def retrieveProgramCollegeSort(page, rows):
  db = mysql.connector.connect(
    host="localhost",
    user = "root",
    password="jupiter'sfear",
    database="ssis"
    )

  mycursor = db.cursor()

  offset = []
  off = (page-1) * rows
  offset.append(off)
  arr = []
  mycursor.execute("SELECT * FROM program ORDER BY college_code ASC LIMIT 25 OFFSET %s", offset)
  for row in mycursor:
    arr.append(row)
  db.close()
  return arr

#For table population of College
def retrieveCollegeCode():
  db = mysql.connector.connect(
    host="localhost",
    user = "root",
    password="jupiter'sfear",
    database="ssis"
    )

  mycursor = db.cursor()
  arr = []
  mycursor.execute("SELECT college_code FROM college ")
  for row in mycursor:
    arr.append(row)
  db.close()
  return arr

def retrieveNumberOfCollege():
  db = mysql.connector.connect(
    host="localhost",
    user = "root",
    password="jupiter'sfear",
    database="ssis"
    )

  mycursor = db.cursor()

  mycursor.execute("SELECT COUNT(college_code) FROM college")
  num = mycursor.fetchone()[0]
  db.close()
  return num

def retrieveCollegeCodeSort(page, rows):
  db = mysql.connector.connect(
    host="localhost",
    user = "root",
    password="jupiter'sfear",
    database="ssis"
    )

  mycursor = db.cursor()

  offset = []
  off = (page-1) * rows
  offset.append(off)
  arr = []
  mycursor.execute("SELECT * FROM college ORDER BY college_code ASC LIMIT 10 OFFSET %s", offset)
  for row in mycursor:
    arr.append(row)
  db.close()
  return arr

def retrieveCollegeNameSort(page, rows):
  db = mysql.connector.connect(
    host="localhost",
    user = "root",
    password="jupiter'sfear",
    database="ssis"
    )

  mycursor = db.cursor()

  offset = []
  off = (page-1) * rows
  offset.append(off)
  arr = []
  mycursor.execute("SELECT * FROM college ORDER BY college_name ASC LIMIT 10 OFFSET %s", offset)
  for row in mycursor:
    arr.append(row)
  db.close()
  return arr

#For search
def rnss(searched):
  db = mysql.connector.connect(
    host="localhost",
    user = "root",
    password="jupiter'sfear",
    database="ssis"
    )

  mycursor = db.cursor()
  query = "SELECT COUNT(program_code) FROM student WHERE student_id LIKE %s OR first_name LIKE %s OR last_name LIKE %s OR year_level LIKE %s OR gender LIKE %s OR program_code LIKE %s"
  mycursor.execute(query, (f"%{searched}%", f"%{searched}%", f"%{searched}%", f"%{searched}%", f"%{searched}%", f"%{searched}%",))
  num = mycursor.fetchone()[0]
  return num

def rnsp(searched):
  db = mysql.connector.connect(
    host="localhost",
    user = "root",
    password="jupiter'sfear",
    database="ssis"
    )

  mycursor = db.cursor()
  query = "SELECT COUNT(program_code) FROM program WHERE program_code LIKE %s OR program_name LIKE %s OR college_code LIKE %s"
  mycursor.execute(query, (f"%{searched}%", f"%{searched}%", f"%{searched}%",))
  num = mycursor.fetchone()[0]
  return num

def rnsc(searched):
  db = mysql.connector.connect(
    host="localhost",
    user = "root",
    password="jupiter'sfear",
    database="ssis"
    )

  mycursor = db.cursor()
  query = "SELECT COUNT(college_code) FROM program WHERE college_code LIKE %s OR college_name LIKE %s"
  mycursor.execute(query, (f"%{searched}%", f"%{searched}%",))
  num = mycursor.fetchone()[0]
  return num
  
def retrieveSearchStudent(searched, page):
  db = mysql.connector.connect(
    host="localhost",
    user = "root",
    password="jupiter'sfear",
    database="ssis"
    )

  mycursor = db.cursor()

  pattern = f"%{searched}%"
  search = []
  for i in range(6):
    search.append(pattern)
  offset = (page-1) * 50
  search.append(offset)
  arr = []
  if searched.isdigit() and len(searched) == 1:
        mycursor.execute("SELECT * FROM student WHERE year_level LIKE %s ORDER BY student_id ASC LIMIT 50 OFFSET %s", (pattern, offset))
  else:
    mycursor.execute("SELECT * FROM student WHERE student_id LIKE %s OR first_name LIKE %s OR last_name LIKE %s OR year_level LIKE %s OR gender LIKE %s OR program_code LIKE %s ORDER BY student_id ASC LIMIT 50 OFFSET %s", search)
  for row in mycursor:
    arr.append(row)
  db.close()
  return arr

def retrieveSearchProgram(searched, page):
  db = mysql.connector.connect(
    host="localhost",
    user = "root",
    password="jupiter'sfear",
    database="ssis"
    )

  mycursor = db.cursor()

  pattern = f"%{searched}%"
  search = []
  for i in range(3):
    search.append(pattern)
  offset = (page-1) * 25
  search.append(offset)
  arr = []
  mycursor.execute("SELECT * FROM program WHERE program_code LIKE %s OR program_name LIKE %s OR college_code LIKE %s ORDER BY program_code ASC LIMIT 25 OFFSET %s", search)
  for row in mycursor:
    arr.append(row)
  db.close()
  return arr

def retrieveSearchCollege(searched, page):
  db = mysql.connector.connect(
    host="localhost",
    user = "root",
    password="jupiter'sfear",
    database="ssis"
    )

  mycursor = db.cursor()

  pattern = f"%{searched}%"
  search = []
  for i in range(2):
    search.append(pattern)
  offset = (page-1) * 10
  search.append(offset)
  arr = []
  mycursor.execute("SELECT * FROM college WHERE college_code LIKE %s OR college_name LIKE %s ORDER BY college_code ASC LIMIT 10 OFFSET %s", search)
  for row in mycursor:
    arr.append(row)
  db.close()
  return arr
