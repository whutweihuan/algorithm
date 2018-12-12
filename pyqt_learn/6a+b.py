#!/usr/bin/python3
#coding=utf-8

import sys
from PyQt5.QtWidgets import QWidget,QLabel,QLineEdit,QPushButton,QVBoxLayout,QHBoxLayout,QApplication
from PyQt5.QtGui import QIcon

class window(QWidget):
	"""docstring for window"""
	def __init__(self):
		super().__init__()
		self.initGui()
		self.result = 0;
		
	def initGui(self):
		self.setGeometry(400,200,400,260)

		self.setWindowTitle('a+b')
		self.setWindowIcon(QIcon('bird.ico'))
		vbox = QVBoxLayout()

		lb1 = QLabel("a: ")
		lb2 = QLabel("b: ")

		self.edit1 = QLineEdit()
		self.edit2 = QLineEdit()


		lb_shuru = QLabel("请输入数据")
		vbox.addWidget(lb_shuru)

		# a+b
		hbox = QHBoxLayout()
		hbox.addStretch(1)
		hbox.addWidget(lb1)
		hbox.addWidget(self.edit1)
		hbox.addStretch(1)
		vbox.addLayout(hbox)

		hbox = QHBoxLayout()
		hbox.addStretch(1)
		hbox.addWidget(lb2)
		hbox.addWidget(self.edit2)
		hbox.addStretch(1)
		vbox.addLayout(hbox)

		lb_result = QLabel("a+b")

		# vbox.addWidget(lb_result)

		self.edit_result = QLineEdit()
		self.edit_result.setReadOnly(True)
		self.edit_result.setMaxLength(5)
		hbox_editRes = QHBoxLayout()
		hbox_editRes.addStretch(1)
		hbox_editRes.addWidget(lb_result)
		hbox_editRes.addWidget(self.edit_result)
		hbox_editRes.addStretch(1)
		vbox.addLayout(hbox_editRes)
		# vbox.addWidget(self.edit_result)

		bt_result = QPushButton('计算')
		hbox_bt = QHBoxLayout()
		hbox_bt.addStretch(1)
		hbox_bt.addWidget(bt_result)
		hbox_bt.addStretch(1)
		vbox.addLayout(hbox_bt)
		bt_result.clicked.connect(self.figure)
		vbox.addWidget(bt_result)

		vbox.setSpacing(20)

		vbox.addStretch(1)

		self.setLayout(vbox)

		#禁止拉伸窗口大小
		self.setFixedSize(self.width(), self.height()); 

		self.show()

	def figure(self):
		# print(self.edit1.text())
		try:
			a = float(self.edit1.text() )
			b=  float(self.edit2.text())
			self.edit_result.setText(str(a+b))
		except Exception as e:
			self.edit_result.setText("error")

if __name__ =='__main__':
	app = QApplication(sys.argv)
	win = window()
	sys.exit(app.exec_())
