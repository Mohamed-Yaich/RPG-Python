from PySide6.QtWidgets import QWidget
from functions.game_functions.Hero import *

def addHeroInMap( mapCell, heroDirection):
    character = QWidget(mapCell[Hero.y][Hero.x])
    character.setGeometry(0, 0, 125, 124)
    character.setStyleSheet(
        " {} ".format(heroDirection))