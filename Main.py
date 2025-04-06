import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

#Manage Windows for Student
class addStudentWindow(QMainWindow):
  def __init__(self):
    super(addStudentWindow, self).__init__()
    loadUi("addStudentWindow.ui", self)

class deleteStudentWindow(QMainWindow):
  def __init__(self):
    super(deleteStudentWindow, self).__init__()
    loadUi("deleteStudentWindow.ui", self)

class editStudentWindow(QMainWindow):
  def __init__(self):
    super(editStudentWindow, self).__init__()
    loadUi("editStudentWindow1.ui", self)


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
    self.window = editStudentWindow()
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

    #Fix Table Ratio       
    self.programTable.setColumnWidth(0,145) 
    self.programTable.setColumnWidth(1, 730)
    self.programTable.setColumnWidth(2,145)
    self.programTable.setRowCount(10)          
  
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

    #Fix Table Ratio       
    self.collegeTable.setColumnWidth(0,145) 
    self.collegeTable.setColumnWidth(1, 875)
    self.collegeTable.setRowCount(10) 

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
