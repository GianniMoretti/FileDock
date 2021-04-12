from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore    import Qt, QTimer

import filedockclose as fdc      
import filedock as fd   

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    screen = app.primaryScreen()
    height = screen.size().height()
    o = fd.FileDock(height)
    c = fdc.FileDockClose(height)
    o.setFileDockClose(c)
    c.setFileDock(o)
    c.exec_()
    sys.exit(app.exec_())
