import time
from functions.game_functions.Hero import *
from functions.game_functions.stages.Stage import *
from functions.game_functions.createMonsterPanel import *
from functions.game_functions.addTextBox import *
from functions.game_functions.drawGameMap import *
from functions.game_functions.createHeroPanel import *
from functions.game_functions.addPanelGoals import *
from functions.game_functions.addInventory import *


def attackSysteme(parent, name, life, strength, defense, level, progressPV, heroDirection):

        attack = int(Hero.strength/(defense/2)*Hero.level)
        life = life - attack
        progressPV =  progressPV - ((attack*100)/life)

        createMonsterPanel(
            parent, 
            name,
            life,
            strength, 
            defense, 
            level, 
            progressPV,
            Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["face"],       
        )

        addTextBox(parent,"vous attaquer le monstre et lui infliger au monstre {} de dégats".format(attack))

        drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), parent, heroDirection)

        time.sleep(2)

        attackBack = int(strength/(Hero.defense/2)*level)
        Hero.life = Hero.life - attackBack
        Hero.progressHeroPv = Hero.progressHeroPv - ((attackBack*100)/Hero.life)

        createHeroPanel(parent)

        addTextBox(parent,"Le monstre vous attaque en retour et vous recevez {} de dégats".format(attackBack))

        if life <= 0:

            Stage.countMonster = Stage.countMonster + 1

            addPanelGoals(
                parent, 
                Stage.countMonster, 
                Stage.currentWorld, 
                "stage {}".format(Stage.currentStage), 
                Stage.countKey
            )

            addTextBox(parent,"bravos le monstre a été vaincu, vous avez gagner XX d'exp")

            
            RAND = random.randint(0,len(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["drop"])-1)
            
            if RAND == 0:
                addTextBox(parent,"aucun objet reçus !")
            else:
                addTextBox(parent,"{},reçus et ranger dans l'inventaire".format(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["drop"][RAND]))
                Stage.saveDropItems.append(Stage.dropInfo["{}".format(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["drop"][RAND])]["image"])
                addInventory(parent)

            drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), parent, heroDirection)