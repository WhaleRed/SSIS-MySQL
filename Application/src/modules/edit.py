import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user = "root",
  password="jupiter'sfear",
  database="ssis"
  )

mycursor = db.cursor()

def editStudent(student):
  mycursor.execute("UPDATE student SET student_id = %s, first_name = %s, last_name = %s, year_level = %s, gender = %s, program_code = %s WHERE student_id =%s", student)
  db.commit()

def editProgram(program):
  mycursor.execute("UPDATE program SET program_code = %s, program_name = %s, college_code = %s WHERE program_code =%s", program)
  db.commit()

def editCollege(college):
  mycursor.execute("UPDATE college SET college_code = %s, college_name = %s WHERE college_code = %s", college)
  db.commit()