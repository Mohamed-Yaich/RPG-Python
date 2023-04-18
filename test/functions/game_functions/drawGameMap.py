from PySide6.QtWidgets import QWidget
from functions.game_functions.Hero import *
from functions.game_functions.createCell import *
from functions.game_functions.addMonsterInMap import *
from functions.game_functions.stages.Stage import *


def drawGameMap(world, stage, gameWindow, heroDirection):

    

    if Stage.currentStage == 5:
     
        # tableau bidimentionnel qui contien toute les coordonner de la map (QWidget)
        mapCell = []
        row =[]
        cell = []
        xPosition = 0

        

        borderMap = QWidget(gameWindow)
        borderMap.setGeometry(350, 100, 763, 565)
        borderMap.setStyleSheet(Stage.world[world]["stages"][stage]["background"])

        mapTop = QWidget(gameWindow)
        mapTop.setGeometry(387, 37, 689, 400)
        mapTop.setStyleSheet(Stage.world[world]["stages"][stage]["top-background"]) 

        Y0 = QWidget(borderMap)
        Y0.setGeometry(0, 245, 763, 269)
        Y0.setStyleSheet("border: none;" "background: none")

        Y1 = QWidget(borderMap)
        Y1.setGeometry(0, 440, 763, 123)
        Y1.setStyleSheet("border: none;" "background: none")
        
        X0 = QWidget(Y0)
        X0.setGeometry(260, 70, 195, 200)

        mapCell.append([X0])

        for x in range(14):

            X = QWidget(Y1)
            X.setGeometry(xPosition, 0, 125, 123)
            X.setStyleSheet("border: none;" "background: none")
            xPosition = xPosition + 49
            x = x + 1
            cell.append(X)
            mapCell.append(cell)

        character = QWidget(mapCell[Hero.y][Hero.x])
        character.setGeometry(0, 0, 125, 124)
        character.setStyleSheet(" {} ".format(heroDirection))

        addMonsterInMap(mapCell, Stage.currentWorld, "stage {}".format(Stage.currentStage))

        return borderMap, mapCell

    else: 
        # permet de placer les lignes les une en dessous des autres
        yPosition = 245
        # compteur de boucle
        y = 0
        # un tableau qui contient le lignes de la map
        row = []
        # tableau bidimentionnel qui contien toute les coordonner de la map (QWidget)
        mapCell = []

        

        borderMap = QWidget(gameWindow)
        borderMap.setGeometry(350, 100, 763, 565)
        borderMap.setStyleSheet(Stage.world[world]["stages"][stage]["background"])

        mapTop = QWidget(gameWindow)
        mapTop.setGeometry(387, 37, 689, 400)
        mapTop.setStyleSheet(Stage.world[world]["stages"][stage]["top-background"])

        # dans borderMap je crée 10 ligne
        while y < 5:

            Y = QWidget(borderMap)
            Y.setGeometry(0, yPosition, 763, 123)
            Y.setStyleSheet("border: none;" "background: none")
            yPosition = yPosition + 49
            y = y + 1

            # chaque ligne créer est un QWidget que j'ajoute dans la liste row
            row.append(Y)

        for i in row:
            # a chaque itération j'appel la fonction createCellInYPosition qui
            # retourne la liste des QWidget créer pour la ligne i que je stock dans une variable cells
            cells = createCellInYPosition(i)
            # je stock la liste des QWidget pour la ligne i dans la liste mapCell
            mapCell.append(cells)
            # voila a quoi ressemblera mapCell : mapCell [ ligne1[QWidget1, QWidget2 ], ligne2[QWidget1, QWidget2 ], ... ]
            # mapCell contient donc toute les coordonnée X et Y de la map

        character = QWidget(mapCell[Hero.y][Hero.x])
        character.setGeometry(0, 0, 125, 124)
        character.setStyleSheet(" {} ".format(heroDirection))

        addMonsterInMap(mapCell, Stage.currentWorld, "stage {}".format(Stage.currentStage))

        return borderMap, mapCell
