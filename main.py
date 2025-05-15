import sys
from PyQt5 import QtWidgets
from layout.login_window import Ui_Form as login_window
from layout.main_window import Ui_Form as main_window
import model

class ProgramBiodata(login_window):
	def __init__(self, dialog):
		login_window.__init__(self)
		self.setupUi(dialog)

		model.createDatabase()

		self.QpushButton_login.clicked.connect(self.login)

	def login(self):
		username = self.QlineEdit_username.text()
		password = self.QlineEdit_password.text()
		if(username == "cahyo" and password == "1234"):
			self.mainWindow = QtWidgets.QDialog()
			self.mainUI = main_window()
			self.mainUI.setupUi(self.mainWindow)
			loginWindow.hide()
			self.mainWindow.show()
			self.viewData()

		self.mainUI.QpushButton_tambahkan.clicked.connect(self.tambahData)
		self.mainUI.QpushButton_hapus.clicked.connect(self.hapusData)

	def viewData(self):
		data = model.viewDataFromDB()

		for biodata in data:
			rowPosition = self.mainUI.QtableWidget_biodata.rowCount()
			self.mainUI.QtableWidget_biodata.insertRow(rowPosition)
			self.mainUI.QtableWidget_biodata.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(biodata[1]))
			self.mainUI.QtableWidget_biodata.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(str(biodata[0])))
			self.mainUI.QtableWidget_biodata.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(biodata[2]))
			self.mainUI.QtableWidget_biodata.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(biodata[3]))


	def tambahData(self):
		nama = self.mainUI.QLineEdit_nama.text()
		nim = self.mainUI.QLineEdit_nim.text()
		prodi = self.mainUI.QLineEdit_prodi.text()
		hobi = self.mainUI.QLineEdit_hobi.text()

		model.insertDatatoDB(nim,nama,prodi,hobi)
		rowPosition = self.mainUI.QtableWidget_biodata.rowCount()

		self.mainUI.QtableWidget_biodata.insertRow(rowPosition)
		self.mainUI.QtableWidget_biodata.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(nama))
		self.mainUI.QtableWidget_biodata.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(nim))
		self.mainUI.QtableWidget_biodata.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(prodi))
		self.mainUI.QtableWidget_biodata.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(hobi))

	def hapusData(self):
		"""fungsi menghapus biodata"""
		selectedRow = self.mainUI.QtableWidget_biodata.currentRow()
		nama = self.mainUI.QtableWidget_biodata.item(selectedRow,0).text()
		self.mainUI.QtableWidget_biodata.removeRow(selectedRow)
		self.mainUI.Qlabel_warning.setText("Data {} berhasil dihapus".format(nama))
		self.mainUI.Qlabel_warning.show()
	

if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	loginWindow = QtWidgets.QDialog()

	loginUI = ProgramBiodata(loginWindow)

	loginWindow.show()
	sys.exit(app.exec_())