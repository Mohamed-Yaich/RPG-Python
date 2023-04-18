from PySide6.QtWidgets import QWidget


def centralWindow(self):

    centralArea = QWidget()
    self.setCentralWidget(centralArea)
    return centralArea
