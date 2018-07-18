import sys, random, socket
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (pyqtSlot, Qt)

TCP_IP = '192.168.1.80'
TCP_PORT = 20250
BUFFER_SIZE = 1024

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
	
		global wash
		global wax
		global rainx
		
		if b.text() == "Mini Wash":
			print (b.text() + " Selected")
			wash = 7
		if b.text() == "Wheel Blaster Wash":
			print (b.text() + " Selected")
			wash = 1
		if b.text() == "Triple Foam Wash":
			print (b.text() + " Selected")
			wash = 11
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
		global wash
		global wax
		global rainx
		last_id = random.randint(10000, 99999)
		send_string = ("<washSoft><addTail><id>" + str(last_id) + "</id><washPkgNum>" + str(wash) + "</washPkgNum>")
		if wax:
			send_string = send_string + "<optNum>" + str(wax) + "</optNum>"
		if rainx:
			send_string = send_string + "<optNum>" + str(rainx) + "</optNum>"
		send_string = send_string + "</addTail></washSoft>"
		print (send_string)
		"""
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((TCP_IP, TCP_PORT))
		s.send(send_string.encode('utf-8'))
		print("Last wash ID: " + last_id)
		data = s.recv(BUFFER_SIZE)
		s.close()
		print('Wash package sent to controller')
		print ("received data:", data)
		"""
if __name__ == '__main__':
	
	app = QApplication(sys.argv)
	cont = rTC()
	sys.exit(app.exec_())