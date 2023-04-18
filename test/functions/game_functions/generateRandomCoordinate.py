
import random
from functions.game_functions.drawGameMap import *
from functions.interface_functions.centralWindow import *
from functions.game_functions.stages.Stage import *


def generateRandomCoordinate(world, stage):

    if Stage.currentStage != 5 :

        # count = random.randint(3, 3)
        x= 0
        Y = 0
        
        # Génération de coordonnées pour les monstres
        for m in range(3):

            randX = random.randint(1, 6)

            if Y < 5 :

                if  x == randX :
                    print("impossible de placer le monstre !")
                else:
                    x = randX

                    Stage.world[world]["stages"][stage]["monsters"]["coordinate"].append([Y, randX])
                    
                    Y = Y + 2   
            

        # Génération de coordonnées pour la clée
        randX = random.randint(9, 10)
        randY = random.randint(0, 4)

        Stage.world[world]["stages"][stage]["chest"]["coordinate"].append([randY, randX])

        # Génération de coordonnées pour la case d'arriver
        randX = random.randint(11, 13)
        randY = random.randint(0, 4)

        Stage.world[world]["stages"][stage]["target"]["coordinate"].append([randY, randX])

    else:
        Stage.world[world]["stages"][stage]["boss"]["coordinate"].append([0, 0])
        Stage.world[world]["stages"][stage]["target"]["coordinate"].append([1, 13])

