from PySide6.QtWidgets import QWidget, QLabel

def addAttackIndication(gameWindow, color):

    attackAction = QWidget(gameWindow)
    attackAction.setGeometry(1110, 35, 100, 100)

    attackLabel = QLabel("Attaquer !", attackAction)
    attackLabel.setGeometry(0,0,100,50)
    attackLabel.setStyleSheet("font-weight: bold;" "color: {};".format(color))
    return attackLabel
    