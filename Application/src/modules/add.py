import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user = "root",
  password="jupiter'sfear",
  database="ssis"
  )

mycursor = db.cursor()

def addStudent(student):
  mycursor.execute("INSERT INTO student VALUE (%s, %s, %s, %s, %s, %s)", student)
  db.commit()

def addProgram(program):
  mycursor.execute("INSERT INTO program VALUE (%s, %s, %s)", program)
  db.commit()

def addCollege(college):
  mycursor.execute("INSERT INTO college VALUE (%s, %s)", college)
  db.commit()
