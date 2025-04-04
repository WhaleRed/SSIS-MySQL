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
  mycursor.execute("SELECT student_id FROM student")
  ids = []
  for row in mycursor:
    ids.append(row[0])
  if student_id in ids:
    return True
  else:
    return False
  
def programExists(prog_code):
  mycursor.execute("SELECT program_code FROM program")
  codes = []
  for row in mycursor:
    codes.append(row[0])
  if prog_code in codes:
    return True
  else:
    return False

def collegeExists(col_code):
  mycursor.execute("SELECT college_code FROM college")
  codes = []
  for row in mycursor:
    codes.append(row[0])
  if col_code in codes:
    return True
  else:
    return False