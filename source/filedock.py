from PyQt6.QtCore    import Qt, QSize
from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QWidget, QPushButton, QGridLayout, QFileDialog, QSpacerItem,QSizePolicy)
from PyQt6 import QtGui
import os
from PyQt6.QtGui import QMouseEvent

#from numpy import source

import filedockstylesheet as style
import folderbutton as fb

class FileDock(QDialog):

    def __init__(self, screenheight, screenwidth, *args, **kwargs):
        super(FileDock, self).__init__(*args, **kwargs)
        self.setObjectName('FileDock_Dialog')
        self.setWindowFlags(self.windowFlags() | Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
        self.setStyleSheet(style.Stylesheet)
        self.side = 'left'
        self.screenheight = screenheight
        self.screenwidth = screenwidth

        posy = int(screenheight / 2 - 450)
        if self.side == 'right':
            posx = screenwidth - 110
        else:
            posx = 0

        self.setGeometry(posx, posy, 100, 900)
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
        path = os.path.join(os.getcwd(), 'source', 'assets', 'addIcon.png')
        b.setIcon(QtGui.QIcon(path))
        self.layout.addWidget(b, 0, 0, alignment=Qt.AlignmentFlag.AlignTop)

        b = QPushButton('', self, clicked=self.switchSide, objectName='SwitchButton')
        b.setIconSize(QSize(25,20))
        b.setFixedSize(25,20)
        path = os.path.join(os.getcwd(), 'source', 'assets', 'biArrow.png')
        b.setIcon(QtGui.QIcon(path))
        self.layout.addWidget(b, 9, 0, alignment=Qt.AlignmentFlag.AlignBottom)

        b = QPushButton('', self, clicked=self.close, objectName='closeButton')
        b.setIconSize(QSize(50,50))
        path = os.path.join(os.getcwd(), 'source', 'assets', 'closeIcon.png')
        b.setIcon(QtGui.QIcon(path))
        self.layout.addWidget(b, 9, 0, alignment=Qt.AlignmentFlag.AlignBottom)

    def folderButtonPush(self):
        sending_button = self.sender()
        sending_button.clickCount = sending_button.clickCount + 1
        self.sortFileButtonsList()
        self.updateFolderButtonLayout()
        os.system('xdg-open "%s"' % sending_button.path)

    def addButtonPush(self):
        path = str(QFileDialog.getExistingDirectory(None, "Select Directory", os.path.expanduser('~') ,QFileDialog.Option.ShowDirsOnly))

        if path == "":
            return

        if self.folderNumber != self.maxFolderNumber:
            b = fb.FolderButton(self.folderNumber, self.folderNumber + 1, path, self.folderButtonPush, self)
            self.layout.addWidget(b, self.folderNumber + 1, 0, alignment=Qt.AlignmentFlag.AlignCenter)
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
            self.layout.addWidget(b, layoutPosition, 0, alignment=Qt.AlignmentFlag.AlignCenter)
            self.folderButtons.append(b)
            self.sortFileButtonsList()
            self.updateFolderButtonLayout()

        os.system('xdg-open "%s"' % path)
        self.switchDock()

    def mouseMoveEvent(self, e: QMouseEvent):
        pos = e.position()
        x = pos.x()
        y = pos.y()

        if self.side == 'right':
            if x < 15:
                self.switchDock()
        else:
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
            self.layout.addWidget(x, i + 1, 0, alignment=Qt.AlignmentFlag.AlignCenter)
        
    def sortFileButtonsList(self):
        self.folderButtons.sort(key= self.calculateFolderButtonValue, reverse=True)

    def calculateFolderButtonValue(self, button):
        return 0.7 * button.folderNumber + 0.3 * button.clickCount

    def switchSide(self):
        self.filedockclose.switchSide()
        self.switchDock()

        if self.side == 'left':
            self.side = 'right'
            posx = self.screenwidth - 110

        else:
            self.side = 'left'
            posx = 0 

        posy = int(self.screenheight / 2 - 450)
        self.move(posx, posy)















