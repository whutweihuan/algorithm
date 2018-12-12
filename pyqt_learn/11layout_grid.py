import sys
 
from PyQt5.QtWidgets import  QLabel, QLineEdit, QApplication, QPushButton, QGridLayout, QWidget
 
 
class ck(QWidget):
    def __init__(self,parent=None):
        super(ck,self).__init__(parent)
 
        self.setWindowTitle('QLabel demo')
 
        #init widget
 
        self.lal_name=QLabel("&Name",self)
        self.le_name=QLineEdit(self)
        self.lal_name.setBuddy(self.le_name)
 
        self.lal_pwd=QLabel("&Password",self)
        self.le_pwd=QLineEdit(self)
        self.lal_pwd.setBuddy(self.le_pwd)
 
        self.btn_ok=QPushButton("&Ok",self)
        self.btn_cancel=QPushButton("&Cancel",self)
 
        #init layout
        self.grid_main=QGridLayout(self)
        self.grid_main.addWidget(self.lal_name,0,0)
        self.grid_main.addWidget(self.le_name,0,1,1,2)
 
        self.grid_main.addWidget(self.lal_pwd,1,0)
        self.grid_main.addWidget(self.le_pwd,1,1,1,2)
 
        self.grid_main.addWidget(self.btn_ok,2,1)
        self.grid_main.addWidget(self.btn_cancel,2,2)
 
 
        #bind event
        self.btn_ok.clicked.connect(self.event_ok)
        self.btn_cancel.clicked.connect(self.event_cancel)
 
    def event_ok(self):
        self.le_name.setText("this is ok click")
    def event_cancel(self):
        self.close()
 
 
 
 
 
if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=ck()
    win.show()
    sys.exit(app.exec_())
