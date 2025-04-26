import mysql.connector

def deleteStudent(idnum):           #Dapat Array I Pass
  db = mysql.connector.connect(
  host="localhost",
  user = "root",
  password="jupiter'sfear",
  database="ssis"
  )
  mycursor = db.cursor()

  mycursor.execute("DELETE FROM student WHERE student_id = %s", idnum)
  db.commit()
  db.close()

def deleteProgram(program_code):    #Dapat Array I Pass
  db = mysql.connector.connect(
  host="localhost",
  user = "root",
  password="jupiter'sfear",
  database="ssis"
  )
  mycursor = db.cursor()

  mycursor.execute("DELETE FROM program WHERE program_code = %s", program_code)
  db.commit()
  db.close()

def deleteCollege(college_code):    #Dapat Array I Pass
  db = mysql.connector.connect(
  host="localhost",
  user = "root",
  password="jupiter'sfear",
  database="ssis"
  )
  mycursor = db.cursor()

  mycursor.execute("DELETE FROM college WHERE college_code = %s", college_code)
  db.commit()
  db.close()
