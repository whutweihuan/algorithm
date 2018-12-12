from PyQt5.QtWidgets import QWidget,QLabel,QLineEdit,QPushButton,QApplication,QGridLayout,QTextEdit,QVBoxLayout,QHBoxLayout
import sys

class Window(QWidget):
	"""docstring for window"""
	def __init__(self):
		super().__init__()
		self.initUi()
		
	def initUi(self):
		
		names = ["a","b","a+b"];
		# positions = [(i,j)for i in range(2) for j in range(3)]
		# print(*positions)
		grid = QGridLayout()
		grid.setSpacing(15)
		#从1开始
		for i,name in enumerate(names,1):
			lb = QLabel(name)
			grid.addWidget(lb,i,1)

		self.aEdit = QLineEdit()
		self.bEdit = QLineEdit()
		self.resEdit = QLineEdit()
		self.resEdit.setReadOnly(True)

		grid.setSpacing(5)
		for i in range(3):
			grid.setColumnStretch(0,1)
			grid.setColumnStretch(3,1)
		grid.addWidget(self.aEdit,1,2)
		grid.addWidget(self.bEdit,2,2)
		grid.addWidget(self.resEdit,3,2)

		vbox = QVBoxLayout()
		# QVBoxLayout.addLayout(grid)

		bt = QPushButton('计算')
		bt.clicked.connect(self.figure)
		grid.addWidget(bt,4,2)

		gridParent = QGridLayout()
		gridParent.addLayout(grid,1,0)
		lab = QLabel('hello boys!')

		grid2 = QGridLayout()

		####
		#setColumnStretch(column,stretch)
		#column:第几列
		#stretch：伸缩因子
		##
		grid2.setColumnStretch(0,1)
		grid2.setColumnStretch(2,1)
		grid2.addWidget(lab,0,1)
		gridParent.addLayout(grid2,2,0)

		# gridParent 

		self.setLayout(gridParent)
		# self.setGeometry(600,300,400,280)
		self.setGeometry(300, 300, 350, 150)
		self.setWindowTitle('a+b')
		self.setFixedSize(self.width(),self.height())
		self.show()

	def figure(self):
		try:
			sum = float(self.aEdit.text())+float(self.bEdit.text())
			self.resEdit.setText(str(sum))
		except Exception as e:
			self.resEdit.setText('error')
if __name__ =='__main__':
	app = QApplication(sys.argv)
	win = Window()
	sys.exit(app.exec_())

