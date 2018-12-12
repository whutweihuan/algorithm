from PyQt5.QtWidgets import QWidget, QApplication, QProgressBar, QPushButton, QMessageBox
from PyQt5.QtCore import Qt, QBasicTimer
import sys

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()    
    def initUI(self):

        self.resize(600,480)
        self.setWindowTitle('关注微信公众号：学点编程吧--跑马灯（进度条）')

        self.pb11 = QProgressBar(self)
        self.pb12 = QProgressBar(self)
        self.pb13 = QProgressBar(self)
        self.pb14 = QProgressBar(self)
        self.pb21 = QProgressBar(self)
        self.pb22 = QProgressBar(self)
        #self.pb12、self.pb13、self.pb14、self.pb21、self.pb22都这样创建的
        #代码省略...

        self.pb11.setOrientation(Qt.Horizontal)
        self.pb12.setOrientation(Qt.Vertical)
        self.pb13.setOrientation(Qt.Horizontal)
        self.pb14.setOrientation(Qt.Vertical)
        #布局的代码省略...

        self.pb21.setFormat("%v")
        self.pb22.setInvertedAppearance(True)

        self.b1 = QPushButton('外圈跑马灯',self)
        self.b2 = QPushButton('内圈跑进度',self)

        self.show()

        self.timer = QBasicTimer()
        self.step = 0

        self.b1.clicked.connect(self.running)
        self.b2.clicked.connect(self.doaction)
        
    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            QMessageBox.information(self,'提示','内圈收工了!')
            self.b2.setText('再来一次')
            self.step = 0
            return

        self.step = self.step + 1
        self.pb21.setValue(self.step)
        self.pb22.setValue(self.step)
    def doaction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.b2.setText('继续')
        else:
            self.timer.start(100, self)
            self.b2.setText('停止')
        
    def running(self):
        self.pb11.setMinimum(0)
        self.pb11.setMaximum(0)
        self.pb12.setInvertedAppearance(True)
        self.pb12.setMinimum(0)
        self.pb12.setMaximum(0)
        self.pb13.setInvertedAppearance(True)
        self.pb13.setMinimum(0)
        self.pb13.setMaximum(0)
        self.pb14.setMinimum(0)
        self.pb14.setMaximum(0)
    
if __name__ == '__main__':
    app = QApplication(sys.argv)

    exam = Example()

    sys.exit(app.exec_())