import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget,QLCDNumber, QSlider, QVBoxLayout,QHBoxLayout, QApplication,QLabel,QLineEdit)
from PyQt5.QtGui import QIcon

class winQwidget(QWidget):
	"""docstring for ClassName"""
	def __init__(self):
		super().__init__()
		
		self.initUI()

	def initUI(self):
		self.setGeometry(400,200,400,400)
		self.setWindowTitle("Hello my god.")
		self.setWindowIcon(QIcon('bird.ico'))

		lb1 = QLabel(self)
		lb1.setText("hello PyQt5")
		lb2 = QLabel(self)
		lb2.setText("hello PyQt5")

		hbox = QHBoxLayout()
		hbox.addStretch(1)
		hbox.addWidget(lb1)
		hbox.addWidget(lb2)
 
		vbox = QVBoxLayout()
		vbox.addStretch(1)
		vbox.addLayout(hbox)
		 
		self.setLayout(vbox)   


		lb1 = QLabel(self)
		lb1.setText("hello PyQt5")
		lb1.move(45,12)

		# self.input = QLineEdit('密码', self)
		self.show()

app = QApplication(sys.argv)
win = winQwidget()
sys.exit(app.exec_())
