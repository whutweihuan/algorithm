#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 

In this example, we position two push
buttons in the bottom-right corner 
of the window. 

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        hbox = QHBoxLayout()
        hbox.addStretch(1) # stretch函数在两个按钮前面增加了一些弹性空间

        # 把这些元素放在应用的右下角
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        # 把这个水平布局放到了一个垂直布局盒里面
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        
        # 弹性元素会把所有的元素一起都放置在应用的右下角
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())