from PyQt5.QtCore    import Qt, QSize
from PyQt5.QtWidgets import (QDialog, QWidget)
from PyQt5 import QtGui
import os

import filedockstylesheet as style
import folderbutton as fb

class FileDockClose(QDialog):

    def __init__(self, height, *args, **kwargs):
        super(FileDockClose, self).__init__(*args, **kwargs)
        self.setObjectName('FileDockClose_Dialog')
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setStyleSheet(style.Stylesheet)
        posy = height / 2 - 440
        self.setGeometry(0, posy, 20, 880)
        self.setMouseTracking(True)

        self.widget = QWidget(self)
        self.widget.setObjectName('FileDockClose_Widgets')
        self.widget.setGeometry(0, 0, 15, 880)
        self.widget.setMouseTracking(True)

    def mouseMoveEvent(self, e):
        x = e.x()
        y = e.y()

        if x < 20:
            self.switchDock()

    def setFileDock(self, filedock):
        self.filedock = filedock

    def switchDock(self):
        self.filedock.show()
        self.hide()