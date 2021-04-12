from PyQt5.QtCore    import Qt, QSize
from PyQt5.QtWidgets import QToolButton
from PyQt5 import QtGui

import filedockstylesheet as style

class FolderButton(QToolButton):

    def __init__(self, folderNumber, layoutPosition, path, clicked, parent=None):
        super(FolderButton, self).__init__(parent)

        self.folderNumber = folderNumber
        self.layoutPosition = layoutPosition
        self.path = path
        self.folderName = path.split("/")[-1]
        self.clickCount = 1

        self.setObjectName('FolderButton')
        self.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.setIconSize(QSize(50,50))
        self.setIcon(QtGui.QIcon('assets/folderIcon.png'))
        self.setText(self.folderName)
        self.released.connect(clicked)