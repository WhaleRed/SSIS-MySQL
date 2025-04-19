import sys
import add
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog


#Manage Windows for Student
class addStudentWindow(QMainWindow):
  def __init__(self):
    super(addStudentWindow, self).__init__()
    loadUi("addStudentWindow.ui", self)

    #Connect
    self.addStudentSubmit.clicked.connect(self.submit)
  
  def submit(self):
    student = []
    student.append(self.idAdd.text())
    student.append(self.fnameAdd.text())
    student.append(self.lnameAdd.text())
    student.append(self.ylvlAdd.currentText())
    student.append(self.genderAdd.currentText())
    student.append(self.programAdd.text())
    
    add.addStudent(student)
    self.close()
    
class deleteStudentWindow(QMainWindow):
  def __init__(self):
    super(deleteStudentWindow, self).__init__()
    loadUi("deleteStudentWindow.ui", self)

    #Connect Button
    self.deleteStudentSubmit.clicked.connect(self.warning)

  def warning(self):
    self.warning = deleteWarning()
    self.warning.show()

class editStudentWindow1(QMainWindow):
  def __init__(self):
    super(editStudentWindow1, self).__init__()
    loadUi("editStudentWindow1.ui", self)

    #Connect
    self.editingStudent.clicked.connect(self.editWindow2)

  def editWindow2(self):
    self.window = editStudentWindow2()
    self.window.show()

class editStudentWindow2(QMainWindow):
  def __init__(self):
    super(editStudentWindow2, self).__init__()
    loadUi("editStudentWindow2.ui", self) 

    #Connect
    self.submitStudent.clicked.connect(self.warning)
  
  def warning(self):
    self.warning = editWarning()
    self.warning.show()

#Manage Windows for Program
class addProgramWindow(QMainWindow):
  def __init__(self):
    super(addProgramWindow,self).__init__()
    loadUi("addProgramWindow.ui", self)

    #Connect
    self.addProgramSubmit.clicked.connect(self.submit)
  
  def submit(self):
    program = []
    program.append(self.programCodeAdd.text())
    program.append(self.programNameAdd.text())
    program.append(self.collegeCodeAdd.text())

    add.addProgram(program)
    self.close()

class deleteProgramWindow(QMainWindow):
  def __init__(self):
    super(deleteProgramWindow,self).__init__()
    loadUi("deleteProgramWindow.ui", self)

    #Connect
    self.deleteProgramSubmit.clicked.connect(self.warning)

  def warning(self):
    self.warning = deleteWarning()
    self.warning.show()

class editProgramWindow1(QMainWindow):
  def __init__(self):
    super(editProgramWindow1, self).__init__()
    loadUi("editProgramWindow1.ui", self)

    #Connect
    self.editingProgram.clicked.connect(self.editWindow2)

  def editWindow2(self):
    self.window = editProgramWindow2()
    self.window.show()

class editProgramWindow2(QMainWindow):
  def __init__(self):
    super(editProgramWindow2, self).__init__()
    loadUi("editProgramWindow2.ui", self)

    #Connect
    self.submitProgram.clicked.connect(self.warning)
  
  def warning(self):
    self.warning = editWarning()
    self.warning.show()

#Manage Windows for College
class addCollegeWindow(QMainWindow):
  def __init__(self):
    super(addCollegeWindow,self).__init__()
    loadUi("addCollegeWindow.ui", self)

    #Connect
    self.addCollegeSubmit.clicked.connect(self.submit)

  def submit(self):
    college = []
    college.append(self.collegeCodeAdd.text())
    college.append(self.collegeNameAdd.text())

    add.addCollege(college)
    self.close()

class deleteCollegeWindow(QMainWindow):
  def __init__(self):
    super(deleteCollegeWindow, self).__init__()
    loadUi("deleteCollegeWindow.ui", self)

    #Conncect
    self.deleteCollegeSubmit.clicked.connect(self.warning)

  def warning(self):
    self.warning = deleteWarning()
    self.warning.show()
    
class editCollegeWindow1(QMainWindow):
  def __init__(self):
    super(editCollegeWindow1, self).__init__()
    loadUi("editCollegeWindow1.ui", self)

    #Connect
    self.editingCollege.clicked.connect(self.editWindow2)
  
  def editWindow2(self):
    self.window = editCollegeWindow2()
    self.window.show()

class editCollegeWindow2(QMainWindow):
  def __init__(self):
    super(editCollegeWindow2, self).__init__()
    loadUi("editCollegeWindow2.ui", self)

    #Connect
    self.submitCollege.clicked.connect(self.warning)
  
  def warning(self):
    self.warning = editWarning()
    self.warning.show()

#Warnings
class deleteWarning(QDialog):
  def __init__(self):
    super(deleteWarning, self).__init__()
    loadUi("deleteWarning.ui", self)

class editWarning(QDialog):
  def __init__(self):
    super(editWarning, self).__init__()
    loadUi("editWarning.ui", self)

class dneWarning(QDialog):
  def __init__(self):
    super(dneWarning, self).__init__()
    loadUi("dneWarning.ui", self)

class aeWarning(QDialog):
  def __init__(self):
    super(aeWarning, self).__init__()
    loadUi("aeWarning.ui", self)


#The 3 Main windows
class studentWindow(QMainWindow):
  def __init__(self):
    super(studentWindow, self).__init__()
    loadUi("studentWindow.ui", self)

    #Conneect Menu
    self.viewPrograms.triggered.connect(self.programView)
    self.viewColleges.triggered.connect(self.collegeView)
    self.addStudent.triggered.connect(self.addWindow)
    self.deleteStudent.triggered.connect(self.deleteWindow)
    self.editStudent.triggered.connect(self.editWindow1)

    #Fix Table Ratio
    self.studentTable.setColumnWidth(0,145)        
    self.studentTable.setColumnWidth(1, 260)        
    self.studentTable.setColumnWidth(2, 260)
    self.studentTable.setColumnWidth(3, 100)
    self.studentTable.setRowCount(10)

  def addWindow(self):
    self.window = addStudentWindow()
    self.window.show()  

  def deleteWindow(self):
    self.window = deleteStudentWindow()
    self.window.show()  
  
  def editWindow1(self):
    self.window = editStudentWindow1()
    self.window.show()  

  def programView(self):
    widget.setWindowTitle("Program Window")               
    widget.setCurrentIndex(widget.currentIndex()+1)
  
  def collegeView(self):
    widget.setWindowTitle("College Window")               
    widget.setCurrentIndex(widget.currentIndex()+2)


class programWindow(QMainWindow):
  def __init__(self):
    super(programWindow, self).__init__()
    loadUi("programWindow.ui", self)
    
    #Connect Menu
    self.viewStudents.triggered.connect(self.studentView)
    self.viewColleges.triggered.connect(self.collegeView)
    self.addProgram.triggered.connect(self.addWindow)
    self.deleteProgram.triggered.connect(self.deleteWindow)
    self.editProgram.triggered.connect(self.editWindow1)

    #Fix Table Ratio       
    self.programTable.setColumnWidth(0,145) 
    self.programTable.setColumnWidth(1, 730)
    self.programTable.setColumnWidth(2,145)
    self.programTable.setRowCount(10) 

  def addWindow(self):
    self.window = addProgramWindow()
    self.window.show()

  def deleteWindow(self):
    self.window = deleteProgramWindow()
    self.window.show()

  def editWindow1(self):
    self.window = editProgramWindow1()
    self.window.show()         
  
  def studentView(self):
    widget.setWindowTitle("Student Window")               
    widget.setCurrentIndex(widget.currentIndex()-1)
  
  def collegeView(self):
    widget.setWindowTitle("College Window") 
    widget.setCurrentIndex(widget.currentIndex()+1)


class collegeWindow(QMainWindow):
  def __init__(self):
    super(collegeWindow, self).__init__()
    loadUi("collegeWindow.ui", self)

    #Connect Menu
    self.viewStudents.triggered.connect(self.studentView)
    self.viewPrograms.triggered.connect(self.programView)
    self.addCollege.triggered.connect(self.addWindow)
    self.deleteCollege.triggered.connect(self.deleteWindow)
    self.editCollege.triggered.connect(self.editWindow1)

    #Fix Table Ratio       
    self.collegeTable.setColumnWidth(0,145) 
    self.collegeTable.setColumnWidth(1, 875)
    self.collegeTable.setRowCount(10) 
  
  def addWindow(self):
    self.window = addCollegeWindow()
    self.window.show()

  def deleteWindow(self):
    self.window = deleteCollegeWindow()
    self.window.show()
  
  def editWindow1(self):
    self.window = editCollegeWindow1()
    self.window.show()

  def studentView(self):
    widget.setWindowTitle("Student Window")               
    widget.setCurrentIndex(widget.currentIndex()-2)
  
  def programView(self):
    widget.setWindowTitle("Program Window") 
    widget.setCurrentIndex(widget.currentIndex()-1)


if __name__ == "__main__":
  app = QApplication(sys.argv)

  widget = QtWidgets.QStackedWidget()

  studentwindow = studentWindow()
  programwindow = programWindow()
  collegewindow = collegeWindow()
  addstuudentwindow = addStudentWindow()

  widget.addWidget(studentwindow)
  widget.addWidget(programwindow)
  widget.addWidget(collegewindow)
  widget.setFixedHeight(597)               
  widget.setFixedWidth(1065)
  widget.setWindowTitle("Student Window")               
  widget.show()

  try:
    sys.exit(app.exec_())
  except:
    print("Exiting")
