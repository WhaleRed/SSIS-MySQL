#This is for my delete and edit operations
#There is a case where I try to delete or edit a non existent row and the edit and delete still runs

import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user = "root",
  password="jupiter'sfear",
  database="ssis"
  )

mycursor = db.cursor()

def studentExists(student_id):
  studentId = []
  studentId.append(student_id)
  check = []
  mycursor.execute("SELECT student_id FROM student WHERE student_id = %s", studentId)
  for row in mycursor:
    check.append(row)
  if not check:
    return False
  else:
    return True
  
def programExists(prog_code):
  progCode = []
  progCode.append(prog_code)
  check = []
  mycursor.execute("SELECT program_code FROM program WHERE program_code = %s", progCode)
  for row in mycursor:
    check.append(row)
  if not check:
    return False
  else:
    return True

def programNameExists(prog_name):
  progName = []
  progName.append(prog_name)
  check = []
  mycursor.execute("SELECT program_code FROM program WHERE program_name = %s", progName)
  for row in mycursor:
    check.append(row)
  if not check:
    return False
  else:
    return True

def collegeExists(col_code):
  colCode = []
  colCode.append(col_code)
  check = []
  mycursor.execute("SELECT college_code FROM college WHERE college_code = %s", colCode)
  for row in mycursor:
    check.append(row)
  if not check:
    return False
  else:
    return True
  
def collegeNameExists(college_name):
  colName = []
  colName.append(college_name)
  check = []
  mycursor.execute("SELECT college_name FROM college WHERE college_name = %s", colName)
  for row in mycursor:
    check.append(row)
  if not check:
    return False
  else:
    return True