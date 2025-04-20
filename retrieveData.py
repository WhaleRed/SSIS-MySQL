import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user = "root",
  password="jupiter'sfear",
  database="ssis"
  )

mycursor = db.cursor()

def retrieveStudent(studid):
  arr = []
  mycursor.execute("SELECT * FROM student WHERE student_id = %s", studid)
  for row in mycursor:
    arr.append(row[0])
    arr.append(row[1])
    arr.append(row[2])
    arr.append(row[3])
    arr.append(row[4])
    arr.append(row[5])
  return arr

def retrieveProgram(prog_code):
  arr = []
  mycursor.execute("SELECT * FROM program WHERE program_code = %s", prog_code)
  for row in mycursor:
    arr.append(row[0])
    arr.append(row[1])
    arr.append(row[2])
  return arr

def retrieveCollege(col_code):
  arr = []
  mycursor.execute("SELECT * FROM college WHERE college_code = %s", col_code)
  for row in mycursor:
    arr.append(row[0])
    arr.append(row[1])
  return arr