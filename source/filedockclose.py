from PyQt5.QtCore    import Qt, QSize
from PyQt5.QtWidgets import (QDialog, QWidget)
from PyQt5 import QtGui
import os

import filedockstylesheet as style
import folderbutton as fb

class FileDockClose(QDialog):

    def __init__(self, screenHeight, screenWidth, *args, **kwargs):
        super(FileDockClose, self).__init__(*args, **kwargs)
        self.setObjectName('FileDockClose_Dialog')
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setStyleSheet(style.Stylesheet)
        self.side = 'left'
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight

        posy = screenHeight / 2 - 440
        if self.side == 'right':
            posx = screenWidth - 20
        else:
            posx = 0
        self.setGeometry(posx, posy, 20, 880)
        self.setMouseTracking(True)
        self.widget = QWidget(self)

        if self.side == 'right':
            self.widget.setGeometry(5, 0, 15, 880)
            self.widget.setObjectName('FileDockRightClose_Widgets')
        else:
            self.widget.setGeometry(0, 0, 15, 880)
            self.widget.setObjectName('FileDockClose_Widgets')

        self.widget.setMouseTracking(True)

    def mouseMoveEvent(self, e):
        x = e.x()
        y = e.y()

        if self.side == 'right':
            if x > 0:
                self.switchDock()
        else:
            if x < 20:
                self.switchDock()      

    def setFileDock(self, filedock):
        self.filedock = filedock

    def switchDock(self):
        self.filedock.show()
        self.hide()

    def switchSide(self):
        if self.side == 'right':
            self.side = 'left'
            self.widget.setObjectName('FileDockClose_Widgets')
        else:
            self.side = 'right'
            self.widget.setObjectName('FileDockRightClose_Widgets')

        self.setStyleSheet(style.Stylesheet)
        
        posy = self.screenHeight / 2 - 440
        if self.side == 'right':
            posx = self.screenWidth - 20
        else:
            posx = 0
        self.move(posx, posy)

