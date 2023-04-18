from functions.game_functions.drawGameMap import *
from functions.game_functions.addHeroInMap import *

def LevelUp(gameWindow , countMonster , MonsterList , countKey , KeyList):
    global niveau_actuel

    # Vérifiez si tous les objectifs du niveau actuel sont accomplis
    if objective1Panel == 0 and objective2Panel == 0:
        # Passer au niveau suivant
        niveau_actuel += 1
        print("Le niveau est terminé")

        # Draw a new map
        drawGameMap(gameWindow)
        