from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore    import Qt, QTimer

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
    c.show()
    sys.exit(app.exec())
