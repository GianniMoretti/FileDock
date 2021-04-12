from PyQt5.QtCore    import Qt, QSize
from PyQt5.QtWidgets import (QDialog, QVBoxLayout, QWidget, QPushButton, QGridLayout, QFileDialog)
from PyQt5 import QtGui
import os

import filedockstylesheet as style
import folderbutton as fb

class FileDock(QDialog):

    def __init__(self, height, *args, **kwargs):
        super(FileDock, self).__init__(*args, **kwargs)
        self.setObjectName('FileDock_Dialog')
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setStyleSheet(style.Stylesheet)
        posy = height / 2 - 450
        self.setGeometry(0, posy, 100, 900)
        self.folderNumber = 0
        self.maxFolderNumber = 8
        self.folderButtons = []

        self.initUi()

    def initUi(self):
        self.widget = QWidget(self)
        self.widget.setObjectName('FileDock_Widgets')
        self.widget.setMouseTracking(True)
        layout = QVBoxLayout(self)
        layout.addWidget(self.widget)
        layout = QGridLayout(self.widget)
        self.layout = layout
        self.mousePassed = False

        self.setMouseTracking(True)

        b = QPushButton('', self, clicked=self.addButtonPush, objectName='NewFolderButton')
        b.setIconSize(QSize(50,50))
        b.setIcon(QtGui.QIcon('assets/addIcon.png'))
        self.layout.addWidget(b, 0, 0, alignment=Qt.AlignTop)

        b = QPushButton('', self, clicked=self.close, objectName='closeButton')
        b.setIconSize(QSize(50,50))
        b.setIcon(QtGui.QIcon('assets/closeIcon.png'))
        self.layout.addWidget(b, 9, 0, alignment=Qt.AlignBottom)

    def folderButtonPush(self):
        sending_button = self.sender()
        sending_button.clickCount = sending_button.clickCount + 1
        self.sortFileButtonsList()
        self.updateFolderButtonLayout()
        os.system('xdg-open "%s"' % sending_button.path)

    def addButtonPush(self):
        path = str(QFileDialog.getExistingDirectory(None, "Select Directory", os.path.expanduser('~') ,QFileDialog.ShowDirsOnly))

        if path == "":
            return

        if self.folderNumber != self.maxFolderNumber:
            b = fb.FolderButton(self.folderNumber, self.folderNumber + 1, path, self.folderButtonPush, self)
            self.layout.addWidget(b, self.folderNumber + 1, 0, alignment=Qt.AlignCenter)
            self.folderButtons.append(b)
            self.folderNumber = self.folderNumber + 1
            self.sortFileButtonsList()
            self.updateFolderButtonLayout()
        else:
            b = self.folderButtons.pop(0)
            layoutPosition = b.layoutPosition
            b.setParent(None)
            
            self.updateFileButtonNumber()
            b = fb.FolderButton(self.maxFolderNumber , layoutPosition, path, self.folderButtonPush, self)
            self.layout.addWidget(b, layoutPosition, 0, alignment=Qt.AlignCenter)
            self.folderButtons.append(b)
            self.sortFileButtonsList()
            self.updateFolderButtonLayout()

        os.system('xdg-open "%s"' % path)
        self.switchDock()


    def mouseMoveEvent(self, e):
        x = e.x()
        y = e.y()

        if x > 90:
            self.switchDock()

    def switchDock(self):
        self.filedockclose.show()
        self.hide()

    def setFileDockClose(self, filedockclose):
        self.filedockclose = filedockclose

    def close(self):
        self.filedockclose.accept()
        self.accept()

    def updateFileButtonNumber(self):
        for x in self.folderButtons:
            x.folderNumber = x.folderNumber - 1

    def updateFolderButtonLayout(self):
        for x in self.folderButtons:
            self.layout.removeWidget(x)

        for i in range(0, self.folderNumber):
            x = self.folderButtons[i]
            x.layoutPosition = i + 1
            self.layout.addWidget(x, i + 1, 0, alignment=Qt.AlignCenter)
        

    def sortFileButtonsList(self):
        self.folderButtons.sort(key= self.calculateFolderButtonValue, reverse=True)

    def calculateFolderButtonValue(self, button):
        return 0.7 * button.folderNumber + 0.3 * button.clickCount












