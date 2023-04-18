from PySide6.QtWidgets import QWidget, QLabel, QTextEdit, QLineEdit
from functions.game_functions.stages.Stage import *


def addTextBox(gameWindow):

    box = QWidget(gameWindow)
    box.setGeometry(390, 645, 690, 150)
    box.setStyleSheet(""" background : #ffffff; border-radius: 10px;""")
    positiony = 0
    message = QTextEdit(box) 
    message.setEnabled(False)
    
    for i in Stage.messageTab:
        message.append(i)
        message.setGeometry(10, positiony, 670, 70)
        message.setStyleSheet("""
                    border: 3px solid #ffffff;
                    border-radius: 10px;
                    
                    background : white;
                    font-size: 14px;
                    background-attachment: scroll;
                    font-weight : bold;
                """)
        
    positiony +=27
        
        
        
