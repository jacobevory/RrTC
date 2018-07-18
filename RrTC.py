import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (pyqtSlot, Qt)

wash = 0
wax = 0
rainx = 0

class rTC(QWidget):
	
	def __init__(self):
		super().__init__()
		
		self.initUI()
		
		
	def initUI(self):
		miniButton = QPushButton('Mini Wash', self)
		miniButton.setCheckable(True)
		miniButton.resize(250, 150)
		miniButton.move(0, 0)   
		miniButton.clicked.connect(lambda:self.washSelect(miniButton))
		
		wheelButton = QPushButton('Wheel Blaster Wash', self)
		wheelButton.setCheckable(True)
		wheelButton.resize(250, 150)
		wheelButton.move(0, 150)	   
		wheelButton.clicked.connect(lambda:self.washSelect(wheelButton))

		tripleButton = QPushButton('Triple Foam Wash', self)
		tripleButton.setCheckable(True)
		tripleButton.resize(250, 150)
		tripleButton.move(0, 300) 
		tripleButton.clicked.connect(lambda:self.washSelect(tripleButton))
		
		hotwaxButton = QPushButton('HotWax', self)
		hotwaxButton.setCheckable(True)
		hotwaxButton.resize(250, 150)
		hotwaxButton.move(250, 0)
		hotwaxButton.clicked.connect(lambda:self.washSelect(hotwaxButton))

		rainxButton = QPushButton('Rain-X', self)
		rainxButton.setCheckable(True)
		rainxButton.resize(250, 150)
		rainxButton.move(250, 150)
		rainxButton.clicked.connect(lambda:self.washSelect(rainxButton))
		
		resetButton = QPushButton('Clear Queue', self)
		resetButton.resize(230, 130)
		resetButton.move(260, 310)
		resetButton.clicked.connect(self.resetClick)
		
		sendButton = QPushButton('Send to Queue', self)
		sendButton.resize(250, 150)
		sendButton.move(500, 300)
		sendButton.clicked.connect(self.sendClick)
		
		washGroup = QtWidgets.QButtonGroup(self)
		washGroup.addButton(miniButton)
		washGroup.addButton(wheelButton)
		washGroup.addButton(tripleButton)
		
		self.setGeometry(300, 300, 750, 450)
		self.setWindowTitle('rTC remote')	
		self.show()
		
		
	@pyqtSlot()
	def washSelect(self, b):
		if b.text() == "Mini Wash":
			print (b.text() + " Selected")
			wash = 7;
		if b.text() == "Wheel Blaster Wash":
			print (b.text() + " Selected")
			wash = 1;
		if b.text() == "Triple Foam Wash":
			print (b.text() + " Selected")
			wash = 11;
		if b.text() == "HotWax":
			if b.isChecked():
				print (b.text() + " Enabled")
				wax = 3
			else:
				print (b.text() + " Disabled")
				wax = 0
		if b.text() == "Rain-X":
			if b.isChecked():
				print (b.text() + " Enabled")
				rainx = 5
			else:
				print (b.text() + " Disabled")
				rainx = 0

	@pyqtSlot()
	def resetClick(self):
		print('Queue Cleared')
	
	@pyqtSlot()
	def sendClick(self):
			print('Wash package sent to controller')
	
if __name__ == '__main__':
	
	app = QApplication(sys.argv)
	cont = rTC()
	sys.exit(app.exec_())