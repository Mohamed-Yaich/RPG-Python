from PySide6.QtWidgets import QWidget
from functions.game_functions.drawGameMap import *
from functions.game_functions.addInventory import *
from functions.game_functions.addTextBox import *




def gameScreen(world, stage, centralArea):

    gameWindow = QWidget(centralArea)
    gameWindow.setGeometry(0, 0, 1275, 900)
    gameWindow.setStyleSheet("background: url(Fond.jpg) no-repeat center;")

    drawGameMap(world, stage, gameWindow, Hero.front)
    addTextBox(gameWindow)
    addInventory(gameWindow)
    return gameWindow
