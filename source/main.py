from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore    import Qt, QTimer

import filedockclose as fdc      
import filedock as fd

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    screen = app.primaryScreen()
    height = screen.size().height()
    width = screen.size().width()
    o = fd.FileDock(height, width)
    c = fdc.FileDockClose(height, width)
    o.setFileDockClose(c)
    c.setFileDock(o)
    c.exec_()
    sys.exit(app.exec_())
