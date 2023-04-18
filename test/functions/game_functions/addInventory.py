import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLabel
from functions.game_functions.createcelleInventory import *
from functions.game_functions.addItemsInInventory import *


def addInventory(gameWindow) :

    yPosition = 6

    rowInventory = []
    MapcellInventory = []

    title = QLabel("I" , gameWindow)
    title.setGeometry(1166, 28 , 350 , 40 )
    title.setStyleSheet("font-size : 35px;" "color : white;" "background : none;")

    limiteInventaire = QWidget(gameWindow)
    limiteInventaire.setGeometry(1100 ,70 , 350 , 840)
    limiteInventaire.setStyleSheet("border : none;" "background : none;")


    for y in range(16) :
        Y = QWidget(limiteInventaire)
        Y.setGeometry(50 , yPosition , 325 , 40)
        Y.setStyleSheet("border : none;")
        yPosition = yPosition + 44
        
        rowInventory.append(Y)


    
    for i in rowInventory:
        # a chaque itération j'appel la fonction createCellInYPosition qui
        # retourne la liste des QWidget créer pour la ligne i que je stock dans une variable cells
        cellsInv = createCellInYPositionInventory(i)
        # je stock la liste des QWidget pour la ligne i dans la liste mapCell
        MapcellInventory.append(cellsInv)
        # voila a quoi ressemblera mapCell : mapCell [ ligne1[QWidget1, QWidget2 ], ligne2[QWidget1, QWidget2 ], ... ]
        # mapCell contient donc toute les coordonnée X et Y de la map
    
    addItemsInInventory(MapcellInventory)

    return MapcellInventory





    
