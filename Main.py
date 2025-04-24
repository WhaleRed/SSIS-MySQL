import sys
import add
import delete
import exists
import retrieveData
import edit, math
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
    self.addStudentSubmit.clicked.connect(self.close)
  
  def submit(self):
    if exists.studentExists(self.idAdd.text()) == True:
      self.alreadyExist()
      return
    else:
      student = []
      student.append(self.idAdd.text())
      student.append(self.fnameAdd.text())
      student.append(self.lnameAdd.text())
      student.append(self.ylvlAdd.currentText())
      student.append(self.genderAdd.currentText())
      student.append(self.programAdd.text())
      
      if '' in student:
        self.emptyField()
      else:
        add.addStudent(student)
  
  def emptyField(self):
    self.warning = emptyFieldWarning()
    self.warning.show()

  def wrongFormat(self):
    self.warning = wrongInputFormat()
    self.warning.show()

  def alreadyExist(self):
    self.warning = aeWarning()
    self.warning.show()

class deleteStudentWindow(QMainWindow):
  def __init__(self):
    super(deleteStudentWindow, self).__init__()
    loadUi("deleteStudentWindow.ui", self)

    #Connect Button
    self.deleteStudentSubmit.clicked.connect(self.deleteStudent)
    self.deleteStudentSubmit.clicked.connect(self.close)

  def deleteStudent(self):
    if exists.studentExists(self.studentDelete.text()) == False:
      self.doesNotExistWarning()
    else:
      global item 
      item = self.studentDelete.text()
      self.warning()

  def doesNotExistWarning(self):
    self.warning = dneWarning()
    self.warning.show()

  def warning(self):
    self.warning = deleteWarning()
    self.warning.show()
    
class editStudentWindow1(QMainWindow):
  def __init__(self):
    super(editStudentWindow1, self).__init__()
    loadUi("editStudentWindow1.ui", self)

    #Connect
    self.editingStudent.clicked.connect(self.check)
    self.editingStudent.clicked.connect(self.close)

  def check(self):
    if exists.studentExists(self.studentEdit.text()) == False:
      self.doesNotExistWarning()
    else:
      arr = []
      arr.append(self.studentEdit.text())
      global studentData
      studentData = retrieveData.retrieveStudent(arr)
      self.editWindow2()

  def doesNotExistWarning(self):
    self.warning = dneWarning()
    self.warning.show()

  def editWindow2(self):
    self.window = editStudentWindow2()
    self.window.show()

class editStudentWindow2(QMainWindow):
  def __init__(self):
    super(editStudentWindow2, self).__init__()
    loadUi("editStudentWindow2.ui", self) 

    #Connect
    self.submitStudent.clicked.connect(self.editStudent)
    self.submitStudent.clicked.connect(self.close)

    #Setting current data values
    self.idNew.setText(studentData[0])
    self.fnameNew.setText(studentData[1])
    self.lnameNew.setText(studentData[2])
    self.ylvlNew.setCurrentText(str(studentData[3]))
    self.genderNew.setCurrentText(studentData[4])
    self.programNew.setText(studentData[5])
  
  def editStudent(self):
    if exists.studentExists(self.idNew.text()) == True and self.idNew.text() != studentData[0]:
      self.alreadyExist()
    else:
      global item
      item = []
      item.append(self.idNew.text())
      item.append(self.fnameNew.text())
      item.append(self.lnameNew.text())
      item.append(self.ylvlNew.currentText())
      item.append(self.genderNew.currentText())
      item.append(self.programNew.text())
      item.append(studentData[0])

      self.warning()

  def warning(self):
    self.warning = editWarning()
    self.warning.show()

  def alreadyExist(self):
    self.warning = aeWarning()
    self.warning.show()

#Manage Windows for Program
class addProgramWindow(QMainWindow):
  def __init__(self):
    super(addProgramWindow,self).__init__()
    loadUi("addProgramWindow.ui", self)

    #Connect
    self.addProgramSubmit.clicked.connect(self.submit)
    self.addProgramSubmit.clicked.connect(self.close)
  
  def submit(self):
    if exists.programExists(self.programCodeAdd.text()) == True:
      self.alreadyExist()
    else:
      program = []
      program.append(self.programCodeAdd.text())
      program.append(self.programNameAdd.text())
      program.append(self.collegeCodeAdd.text())

      if '' in program:
        self.emptyField()
      else:
        add.addProgram(program)

  def emptyField(self):
    self.warning = emptyFieldWarning()
    self.warning.show()

  def wrongFormat(self):
    self.warning = wrongInputFormat()
    self.warning.show()
  
  def alreadyExist(self):
    self.warning = aeWarning()
    self.warning.show()

class deleteProgramWindow(QMainWindow):
  def __init__(self):
    super(deleteProgramWindow,self).__init__()
    loadUi("deleteProgramWindow.ui", self)

    #Connect
    self.deleteProgramSubmit.clicked.connect(self.deleteProgram)
    self.deleteProgramSubmit.clicked.connect(self.close)
  
  def deleteProgram(self):
    if exists.programExists(self.programDelete.text()) == False:
      self.doesNotExistWarning()
    else:
      global item 
      item = self.programDelete.text()
      self.warning()

  def doesNotExistWarning(self):
    self.warning = dneWarning()
    self.warning.show()

  def warning(self):
    self.warning = deleteWarning()
    self.warning.show()

class editProgramWindow1(QMainWindow):
  def __init__(self):
    super(editProgramWindow1, self).__init__()
    loadUi("editProgramWindow1.ui", self)

    #Connect
    self.editingProgram.clicked.connect(self.check)
    self.editingProgram.clicked.connect(self.close)

  def check(self):
    if exists.programExists(self.programEdit.text()) == False:
      self.doesNotExistWarning()
    else:
      arr = []
      arr.append(self.programEdit.text())
      global programData
      programData = retrieveData.retrieveProgram(arr)
      self.editWindow2()

  def doesNotExistWarning(self):
    self.warning = dneWarning()
    self.warning.show()

  def editWindow2(self):
    self.window = editProgramWindow2()
    self.window.show()

class editProgramWindow2(QMainWindow):
  def __init__(self):
    super(editProgramWindow2, self).__init__()
    loadUi("editProgramWindow2.ui", self)

    #Connect
    self.submitProgram.clicked.connect(self.editProgram)
    self.submitProgram.clicked.connect(self.close)

    #Set current Data values
    self.programCodeNew.setText(programData[0])
    self.programNameNew.setText(programData[1])
    self.collegeCodeNew.setText(programData[2])
  
  def editProgram(self):
    if exists.programExists(self.programCodeNew.text()) == True and self.programCodeNew.text() != programData[0]:
      self.alreadyExist()
    else:
      global item
      item = []
      item.append(self.programCodeNew.text())
      item.append(self.programNameNew.text())
      item.append(self.collegeCodeNew.text())
      item.append(programData[0])
      self.warning()

  def warning(self):
    self.warning = editWarning()
    self.warning.show()

  def alreadyExist(self):
    self.warning = aeWarning()
    self.warning.show()

#Manage Windows for College
class addCollegeWindow(QMainWindow):
  def __init__(self):
    super(addCollegeWindow,self).__init__()
    loadUi("addCollegeWindow.ui", self)

    #Connect
    self.addCollegeSubmit.clicked.connect(self.submit)
    self.addCollegeSubmit.clicked.connect(self.close)

  def submit(self):
    if exists.collegeExists(self.collegeCodeAdd.text()) == True or exists.collegeNameExists(self.collegeNameAdd.text()) == True:
      self.alreadyExist()
    else:
      college = []
      college.append(self.collegeCodeAdd.text())
      college.append(self.collegeNameAdd.text())
      
      if '' in college:
        self.emptyField()
      else:
        add.addCollege(college)

  def emptyField(self):
    self.warning = emptyFieldWarning()
    self.warning.show()

  def wrongFormat(self):
    self.warning = wrongInputFormat()
    self.warning.show()

  def alreadyExist(self):
    self.warning = aeWarning()
    self.warning.show()

class deleteCollegeWindow(QMainWindow):
  def __init__(self):
    super(deleteCollegeWindow, self).__init__()
    loadUi("deleteCollegeWindow.ui", self)

    #Conncect
    self.deleteCollegeSubmit.clicked.connect(self.deleteCollege)
    self.deleteCollegeSubmit.clicked.connect(self.close)

  def deleteCollege(self):
    if exists.collegeExists(self.collegeDelete.text()) == False:
      self.doesNotExistWarning()
    else:
      global item 
      item = self.collegeDelete.text()
      self.warning()

  def doesNotExistWarning(self):
    self.warning = dneWarning()
    self.warning.show()

  def warning(self):
    self.warning = deleteWarning()
    self.warning.show()
    
class editCollegeWindow1(QMainWindow):
  def __init__(self):
    super(editCollegeWindow1, self).__init__()
    loadUi("editCollegeWindow1.ui", self)

    #Connect
    self.editingCollege.clicked.connect(self.check)
    self.editingCollege.clicked.connect(self.close)

  def check(self):
    if exists.collegeExists(self.collegeEdit.text()) == False:
      self.doesNotExistWarning()
    else: 
      arr = []
      arr.append(self.collegeEdit.text())
      global collegeData
      collegeData = retrieveData.retrieveCollege(arr)
      self.editWindow2()

  def doesNotExistWarning(self):
    self.warning = dneWarning()
    self.warning.show()

  def editWindow2(self):
    self.window = editCollegeWindow2()
    self.window.show()

class editCollegeWindow2(QMainWindow):
  def __init__(self):
    super(editCollegeWindow2, self).__init__()
    loadUi("editCollegeWindow2.ui", self)

    #Connect
    self.submitCollege.clicked.connect(self.editCollege)
    self.submitCollege.clicked.connect(self.close)

    #Set current data Values
    self.collegeCodeNew.setText(collegeData[0])
    self.collegeNameNew.setText(collegeData[1])

  def editCollege(self):
    if exists.collegeExists(self.collegeCodeNew.text()) == True and self.collegeCodeNew.text() != collegeData[0]:
      self.alreadyExist()
    else:
      global item
      item = []
      item.append(self.collegeCodeNew.text())
      item.append(self.collegeNameNew.text())
      item.append(collegeData[0])

      self.warning()

  def warning(self):
    self.warning = editWarning()
    self.warning.show()

  def alreadyExist(self):
    self.warning = aeWarning()
    self.warning.show()

#Warnings
class deleteWarning(QDialog):
  def __init__(self):
    super(deleteWarning, self).__init__()
    loadUi("deleteWarning.ui", self)

    #Connect
    self.yes.clicked.connect(confirmDelete)
    self.yes.clicked.connect(self.close)
    self.cancel.clicked.connect(self.close)

class editWarning(QDialog):
  def __init__(self):
    super(editWarning, self).__init__()
    loadUi("editWarning.ui", self)

    #Connect
    self.yes.clicked.connect(confirmEdit)
    self.yes.clicked.connect(self.close)
    self.cancel.clicked.connect(self.close)   

class dneWarning(QDialog):
  def __init__(self):
    super(dneWarning, self).__init__()
    loadUi("dneWarning.ui", self)

class aeWarning(QDialog):
  def __init__(self):
    super(aeWarning, self).__init__()
    loadUi("aeWarning.ui", self)

class wrongInputFormat(QDialog):
  def __init__(self):
    super(wrongInputFormat, self).__init__()
    loadUi("wIF.ui", self)

class emptyFieldWarning(QDialog):
  def __init__(self):
    super(emptyFieldWarning, self).__init__()
    loadUi("eFW.ui", self)

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
    self.refreshTable.triggered.connect(self.refresh)
    self.sortID.triggered.connect(self.sortById)
    self.sortFirstName.triggered.connect(self.sortByFirstName)
    self.sortLastName.triggered.connect(self.sortByLastName)
    self.sortYearLevel.triggered.connect(self.sortByYearLevel)
    self.sortGender.triggered.connect(self.sortByGender)
    self.sortProgram.triggered.connect(self.sortByProgram)

    #Connect Buttons
    self.searchButton.clicked.connect(self.search)
    self.nextButton.clicked.connect(self.nextPage)
    self.prevButton.clicked.connect(self.prevPage)
    self.fPage.clicked.connect(self.firstPage)
    self.lPage.clicked.connect(self.lastPage)
    self.jump.clicked.connect(self.jumpPage)

    #Fix Table Ratio
    self.studentTable.setColumnWidth(0,145)        
    self.studentTable.setColumnWidth(1, 260)        
    self.studentTable.setColumnWidth(2, 260)
    self.studentTable.setColumnWidth(3, 100)
    self.studentTable.setRowCount(50)
    
    #First run for table
    self.studentSortState = 0
    self.populateTable(self.studentSortState)

  def addWindow(self):
    self.window = addStudentWindow()
    self.window.show()  

  def deleteWindow(self):
    self.window = deleteStudentWindow()
    self.window.show()  
  
  def editWindow1(self):
    self.window = editStudentWindow1()
    self.window.show()  

  def refresh(self):
    self.studentSortState = 0
    self.populateTable(self.studentSortState)

  def programView(self):
    widget.setWindowTitle("Program Window")               
    widget.setCurrentIndex(widget.currentIndex()+1)
  
  def collegeView(self):
    widget.setWindowTitle("College Window")               
    widget.setCurrentIndex(widget.currentIndex()+2)
  
  def sortById(self):
    self.studentSortState = 0
    self.populateTable(self.studentSortState)

  def sortByFirstName(self):
    self.studentSortState = 1
    self.populateTable(self.studentSortState)

  def sortByLastName(self):
    self.studentSortState = 2
    self.populateTable(self.studentSortState)

  def sortByYearLevel(self):
    self.studentSortState = 3
    self.populateTable(self.studentSortState)

  def sortByGender(self):
    self.studentSortState = 4
    self.populateTable(self.studentSortState)

  def sortByProgram(self):
    self.studentSortState = 5
    self.populateTable(self.studentSortState)

  def search(self):
    self.studentSortState = 6
    self.populateTable(self.studentSortState)

  def populateTable(self, sortState):
    match sortState:
      case 0:
        students = retrieveData.retrieveStudentsIdSort(int(self.pageNum.text()),50)
        row = 0
        for student in students:
          self.studentTable.setItem(row, 0, QtWidgets.QTableWidgetItem(student[0]))
          self.studentTable.setItem(row, 1, QtWidgets.QTableWidgetItem(student[1]))
          self.studentTable.setItem(row, 2, QtWidgets.QTableWidgetItem(student[2]))
          self.studentTable.setItem(row, 3, QtWidgets.QTableWidgetItem(str(student[3])))
          self.studentTable.setItem(row, 4, QtWidgets.QTableWidgetItem(student[4]))
          self.studentTable.setItem(row, 5, QtWidgets.QTableWidgetItem(student[5]))
          row = row + 1

      case 1:
        students = retrieveData.retrieveStudentsFnameSort(int(self.pageNum.text()),50)
        row = 0
        for student in students:
          self.studentTable.setItem(row, 0, QtWidgets.QTableWidgetItem(student[0]))
          self.studentTable.setItem(row, 1, QtWidgets.QTableWidgetItem(student[1]))
          self.studentTable.setItem(row, 2, QtWidgets.QTableWidgetItem(student[2]))
          self.studentTable.setItem(row, 3, QtWidgets.QTableWidgetItem(str(student[3])))
          self.studentTable.setItem(row, 4, QtWidgets.QTableWidgetItem(student[4]))
          self.studentTable.setItem(row, 5, QtWidgets.QTableWidgetItem(student[5]))
          row = row + 1

      case 2:
        students = retrieveData.retrieveStudentsLnameSort(int(self.pageNum.text()),50)
        row = 0
        for student in students:
          self.studentTable.setItem(row, 0, QtWidgets.QTableWidgetItem(student[0]))
          self.studentTable.setItem(row, 1, QtWidgets.QTableWidgetItem(student[1]))
          self.studentTable.setItem(row, 2, QtWidgets.QTableWidgetItem(student[2]))
          self.studentTable.setItem(row, 3, QtWidgets.QTableWidgetItem(str(student[3])))
          self.studentTable.setItem(row, 4, QtWidgets.QTableWidgetItem(student[4]))
          self.studentTable.setItem(row, 5, QtWidgets.QTableWidgetItem(student[5]))
          row = row + 1

      case 3:
        students = retrieveData.retrieveStudentsYearSort(int(self.pageNum.text()),50)
        row = 0
        for student in students:
          self.studentTable.setItem(row, 0, QtWidgets.QTableWidgetItem(student[0]))
          self.studentTable.setItem(row, 1, QtWidgets.QTableWidgetItem(student[1]))
          self.studentTable.setItem(row, 2, QtWidgets.QTableWidgetItem(student[2]))
          self.studentTable.setItem(row, 3, QtWidgets.QTableWidgetItem(str(student[3])))
          self.studentTable.setItem(row, 4, QtWidgets.QTableWidgetItem(student[4]))
          self.studentTable.setItem(row, 5, QtWidgets.QTableWidgetItem(student[5]))
          row = row + 1

      case 4:
        students = retrieveData.retrieveStudentsGenderSort(int(self.pageNum.text()),50)
        row = 0
        for student in students:
          self.studentTable.setItem(row, 0, QtWidgets.QTableWidgetItem(student[0]))
          self.studentTable.setItem(row, 1, QtWidgets.QTableWidgetItem(student[1]))
          self.studentTable.setItem(row, 2, QtWidgets.QTableWidgetItem(student[2]))
          self.studentTable.setItem(row, 3, QtWidgets.QTableWidgetItem(str(student[3])))
          self.studentTable.setItem(row, 4, QtWidgets.QTableWidgetItem(student[4]))
          self.studentTable.setItem(row, 5, QtWidgets.QTableWidgetItem(student[5]))
          row = row + 1

      case 5:
        students = retrieveData.retrieveStudentsProgramSort(int(self.pageNum.text()),50)
        row = 0
        for student in students:
          self.studentTable.setItem(row, 0, QtWidgets.QTableWidgetItem(student[0]))
          self.studentTable.setItem(row, 1, QtWidgets.QTableWidgetItem(student[1]))
          self.studentTable.setItem(row, 2, QtWidgets.QTableWidgetItem(student[2]))
          self.studentTable.setItem(row, 3, QtWidgets.QTableWidgetItem(str(student[3])))
          self.studentTable.setItem(row, 4, QtWidgets.QTableWidgetItem(student[4]))
          self.studentTable.setItem(row, 5, QtWidgets.QTableWidgetItem(student[5]))
          row = row + 1
      
      case 6:
        if self.searchBar.text() != '':
          self.studentTable.clearContents()
          result = retrieveData.retrieveSearchStudent(self.searchBar.text(), int(self.pageNum.text()))
          row = 0
          for student in result:
            self.studentTable.setItem(row, 0, QtWidgets.QTableWidgetItem(student[0]))
            self.studentTable.setItem(row, 1, QtWidgets.QTableWidgetItem(student[1]))
            self.studentTable.setItem(row, 2, QtWidgets.QTableWidgetItem(student[2]))
            self.studentTable.setItem(row, 3, QtWidgets.QTableWidgetItem(str(student[3])))
            self.studentTable.setItem(row, 4, QtWidgets.QTableWidgetItem(student[4]))
            self.studentTable.setItem(row, 5, QtWidgets.QTableWidgetItem(student[5]))
            row = row + 1
        else:       #If empyt search bar 
          self.studentTable.clearContents()
          self.studentSortState = 0
          self.populateTable(self.studentSortState)

  def nextPage(self):
    page = int(self.pageNum.text()) + 1
    self.pageNum.setText(str(page))
    self.populateTable(self.studentSortState)
  
  def prevPage(self):
    if int(self.pageNum.text()) > 1:
      page = int(self.pageNum.text()) - 1
      self.pageNum.setText(str(page))
      self.populateTable(self.studentSortState)

  def firstPage(self):
    if int(self.pageNum.text()) > 1:
      self.pageNum.setText(str(1))
      self.populateTable(self.studentSortState)

  def lastPage(self):
    self.pageNum.setText(str(math.ceil(retrieveData.retrieveNumberOfStudents()/50)))
    self.populateTable(self.studentSortState)
  
  def jumpPage(self):
    if int(self.pageNum.text()) >= 1 and int(self.pageNum.text()) <= math.ceil(retrieveData.retrieveNumberOfStudents()/50):
      self.populateTable(self.studentSortState)


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
    self.refreshTable.triggered.connect(self.refresh)
    self.sortCode.triggered.connect(self.sortByCode)
    self.sortName.triggered.connect(self.sortByName)
    self.sortCollege.triggered.connect(self.sortByCollege)

    #Connect Buttons
    self.searchButton.clicked.connect(self.search)
    self.nextButton.clicked.connect(self.nextPage)
    self.prevButton.clicked.connect(self.prevPage)
    self.fPage.clicked.connect(self.firstPage)
    self.lPage.clicked.connect(self.lastPage)
    self.jump.clicked.connect(self.jumpPage)

    #Fix Table Ratio       
    self.programTable.setColumnWidth(0,145) 
    self.programTable.setColumnWidth(1, 730)
    self.programTable.setColumnWidth(2,145)
    self.programTable.setRowCount(25) 

    #First run
    self.programSortState = 0
    self.populateTable(self.programSortState)

  def addWindow(self):
    self.window = addProgramWindow()
    self.window.show()

  def deleteWindow(self):
    self.window = deleteProgramWindow()
    self.window.show()

  def editWindow1(self):
    self.window = editProgramWindow1()
    self.window.show()         

  def refresh(self):
    self.programSortState = 0
    self.populateTable(self.programSortState)

  def studentView(self):
    widget.setWindowTitle("Student Window")               
    widget.setCurrentIndex(widget.currentIndex()-1)
  
  def collegeView(self):
    widget.setWindowTitle("College Window") 
    widget.setCurrentIndex(widget.currentIndex()+1)

  def sortByCode(self):
    self.programSortState = 0
    self.populateTable(self.programSortState)

  def sortByName(self):
    self.programSortState = 1
    self.populateTable(self.programSortState)

  def sortByCollege(self):
    self.programSortState = 2
    self.populateTable(self.programSortState)

  def search(self):
    self.programSortState = 3
    self.populateTable(self.programSortState)

  def populateTable(self, sortState):
    match sortState:
      case 0:
        programs = retrieveData.retrieveProgramCodeSort(int(self.pageNum.text()), 25)
        row = 0
        for program in programs:
          self.programTable.setItem(row, 0, QtWidgets.QTableWidgetItem(program[0]))
          self.programTable.setItem(row, 1, QtWidgets.QTableWidgetItem(program[1]))
          self.programTable.setItem(row, 2, QtWidgets.QTableWidgetItem(program[2]))
          row = row + 1

      case 1:
        programs = retrieveData.retrieveProgramNameSort(int(self.pageNum.text()), 25)
        row = 0
        for program in programs:
          self.programTable.setItem(row, 0, QtWidgets.QTableWidgetItem(program[0]))
          self.programTable.setItem(row, 1, QtWidgets.QTableWidgetItem(program[1]))
          self.programTable.setItem(row, 2, QtWidgets.QTableWidgetItem(program[2]))
          row = row + 1

      case 2:
        programs = retrieveData.retrieveProgramCollegeSort(int(self.pageNum.text()), 25)
        row = 0
        for program in programs:
          self.programTable.setItem(row, 0, QtWidgets.QTableWidgetItem(program[0]))
          self.programTable.setItem(row, 1, QtWidgets.QTableWidgetItem(program[1]))
          self.programTable.setItem(row, 2, QtWidgets.QTableWidgetItem(program[2]))
          row = row + 1
      
      case 3:
        if self.searchBar.text() != '':
          self.programTable.clearContents()
          result = retrieveData.retrieveSearchProgram(self.searchBar.text(), int(self.pageNum.text()))
          row = 0
          for program in result:
            self.programTable.setItem(row, 0, QtWidgets.QTableWidgetItem(program[0]))
            self.programTable.setItem(row, 1, QtWidgets.QTableWidgetItem(program[1]))
            self.programTable.setItem(row, 2, QtWidgets.QTableWidgetItem(program[2]))
            row = row + 1
        else:
          self.programTable.clearContents()
          self.programSortState = 0
          self.populateTable(self.programSortState)

  def nextPage(self):
    page = int(self.pageNum.text()) + 1
    self.pageNum.setText(str(page))
    self.populateTable(self.programSortState)
  
  def prevPage(self):
    if int(self.pageNum.text()) > 1:
      page = int(self.pageNum.text()) - 1
      self.pageNum.setText(str(page))
      self.populateTable(self.programSortState)

  def firstPage(self):
    if int(self.pageNum.text()) > 1:
      self.pageNum.setText(str(1))
      self.populateTable(self.programSortState)

  def lastPage(self):
    self.pageNum.setText(str(math.ceil(retrieveData.retrieveNumberOfProgram()/25)))
    self.populateTable(self.programSortState)
  
  def jumpPage(self):
    if int(self.pageNum.text()) >= 1 and int(self.pageNum.text()) <= math.ceil(retrieveData.retrieveNumberOfProgram()/25):
      self.populateTable(self.programSortState)


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
    self.refreshTable.triggered.connect(self.refresh)
    self.sortCode.triggered.connect(self.sortByCode)
    self.sortName.triggered.connect(self.sortByName)

    #Connect Buttons
    self.searchButton.clicked.connect(self.search)
    self.nextButton.clicked.connect(self.nextPage)
    self.prevButton.clicked.connect(self.prevPage)
    self.fPage.clicked.connect(self.firstPage)
    self.lPage.clicked.connect(self.lastPage)
    self.jump.clicked.connect(self.jumpPage)

    #Fix Table Ratio       
    self.collegeTable.setColumnWidth(0,145) 
    self.collegeTable.setColumnWidth(1, 875)
    self.collegeTable.setRowCount(10) 

    #First run
    self.collegeSortState = 0
    self.populateTable(self.collegeSortState)

  
  def addWindow(self):
    self.window = addCollegeWindow()
    self.window.show()

  def deleteWindow(self):
    self.window = deleteCollegeWindow()
    self.window.show()
  
  def editWindow1(self):
    self.window = editCollegeWindow1()
    self.window.show()

  def refresh(self):
    self.collegeSortState = 0
    self.populateTable(self.collegeSortState)

  def studentView(self):
    widget.setWindowTitle("Student Window")               
    widget.setCurrentIndex(widget.currentIndex()-2)
  
  def programView(self):
    widget.setWindowTitle("Program Window") 
    widget.setCurrentIndex(widget.currentIndex()-1)
  
  def sortByCode(self):
    self.collegeSortState = 0
    self.populateTable(self.collegeSortState)

  def sortByName(self):
    self.collegeSortState = 1
    self.populateTable(self.collegeSortState)

  def search(self):
    self.collegeSortState = 2
    self.populateTable(self.collegeSortState)

  def populateTable(self,sortState):
    match sortState:
      case 0:
        self.collegeTable.clearContents()
        colleges = retrieveData.retrieveCollegeCodeSort(int(self.pageNum.text()), 10)
        row = 0
        for college in colleges:
          self.collegeTable.setItem(row, 0, QtWidgets.QTableWidgetItem(college[0]))
          self.collegeTable.setItem(row, 1, QtWidgets.QTableWidgetItem(college[1]))
          row = row + 1

      case 1:
        self.collegeTable.clearContents()
        colleges = retrieveData.retrieveCollegeNameSort(int(self.pageNum.text()), 10)
        row = 0
        for college in colleges:
          self.collegeTable.setItem(row, 0, QtWidgets.QTableWidgetItem(college[0]))
          self.collegeTable.setItem(row, 1, QtWidgets.QTableWidgetItem(college[1]))
          row = row + 1
      
      case 2:
        if self.searchBar.text() != '':
          self.collegeTable.clearContents()
          result = retrieveData.retrieveSearchCollege(self.searchBar.text(), int(self.pageNum.text()))
          row = 0
          for college in result:
            self.collegeTable.setItem(row, 0, QtWidgets.QTableWidgetItem(college[0]))
            self.collegeTable.setItem(row, 1, QtWidgets.QTableWidgetItem(college[1]))
            row = row + 1
        else:
          self.collegeTable.clearContents()
          self.collegeSortState = 0
          self.populateTable(self.collegeSortState)

  def nextPage(self):
    page = int(self.pageNum.text()) + 1
    self.pageNum.setText(str(page))
    self.populateTable(self.collegeSortState)
  
  def prevPage(self):
    if int(self.pageNum.text()) > 1:
      page = int(self.pageNum.text()) - 1
      self.pageNum.setText(str(page))
      self.populateTable(self.collegeSortState)

  def firstPage(self):
    if int(self.pageNum.text()) > 1:
      self.pageNum.setText(str(1))
      self.populateTable(self.collegeSortState)

  def lastPage(self):
    self.pageNum.setText(str(math.ceil(retrieveData.retrieveNumberOfCollege()/10)))
    self.populateTable(self.collegeSortState)
  
  def jumpPage(self):
    if int(self.pageNum.text()) >= 1 and int(self.pageNum.text()) <= math.ceil(retrieveData.retrieveNumberOfCollege()/10):
      self.populateTable(self.collegeSortState)

#Global functions
def confirmDelete():
  arr = []
  arr.append(item)
  if widget.currentIndex() == 0:
    delete.deleteStudent(arr)
  elif widget.currentIndex() == 1:
    delete.deleteProgram(arr)
  elif widget.currentIndex() == 2:
    delete.deleteCollege(arr)

def confirmEdit():
  if widget.currentIndex() == 0:
    edit.editStudent(item)
  elif widget.currentIndex() == 1:
    edit.editProgram(item)
  elif widget.currentIndex() == 2:
    edit.editCollege(item)


#####
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
  widget.setFixedHeight(640)               
  widget.setFixedWidth(1065)
  widget.setWindowTitle("Student Window")               
  widget.show()

  try:
    sys.exit(app.exec_())
  except:
    print("Exiting")
