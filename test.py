import mysql.connector

def rnss(searched):
  db = mysql.connector.connect(
    host="localhost",
    user = "root",
    password="jupiter'sfear",
    database="ssis"
    )

  mycursor = db.cursor()
  query = "SELECT COUNT(program_code) FROM student WHERE program_code LIKE %s"
  mycursor.execute(query, (f"%{searched}%",))
  num = mycursor.fetchone()[0]
  return num

print(rnss('BSEE'))
