
import random
from functions.interface_functions.centralWindow import *
from functions.game_functions.stages.Stage import *
from functions.game_functions.addSprite import *
from functions.game_functions.Hero import *



def addMonsterInMap(mapCell, world, stage):

    if Stage.currentStage < 5 :
   
        for m in Stage.world[world]["stages"][stage]["monsters"]["coordinate"] :

            Stage.world[world]["stages"][stage]["monsters"]["info"].append({
                "y": m[0],
                "x": m[1],
                "name": Stage.world[world]["stages"][stage]["monsters"]["name"],
                "life": Stage.world[world]["stages"][stage]["monsters"]["life"],
                "strength": Stage.world[world]["stages"][stage]["monsters"]["strength"],
                "defense": Stage.world[world]["stages"][stage]["monsters"]["defense"],
                "level": Stage.world[world]["stages"][stage]["monsters"]["level"],
                "progressPV": Stage.world[world]["stages"][stage]["monsters"]["progressPV"],
                "isDroped" : Stage.world[world]["stages"][stage]["monsters"]["isDroped"],
                "isAlive": Stage.world[world]["stages"][stage]["monsters"]["isAlive"]
            })   
            
            if m[0] == Hero.y and m[1] == Hero.x+1:
                addSprite(mapCell, m[0], m[1], Stage.world[world]["stages"][stage]["monsters"]["left"])

            elif m[0] == Hero.y and m[1] == Hero.x-1:
                addSprite(mapCell, m[0], m[1], Stage.world[world]["stages"][stage]["monsters"]["right"])

            elif m[0] == Hero.y+1 and m[1] == Hero.x:
                addSprite(mapCell, m[0], m[1], Stage.world[world]["stages"][stage]["monsters"]["back"])

            elif m[0] == Hero.y-1 and m[1] == Hero.x:
    
                addSprite(mapCell, m[0], m[1], Stage.world[world]["stages"][stage]["monsters"]["front"])
            else:
                addSprite(mapCell, m[0], m[1], Stage.world[world]["stages"][stage]["monsters"]["front"]) 
            

        for i in Stage.world[world]["stages"][stage]["monsters"]["info"]:

            if i["life"] <= 0:
                addSprite(mapCell, i["y"], i["x"], Stage.world[world]["stages"][stage]["monsters"]["dead"])             
        

        for k in Stage.world[world]["stages"][stage]["chest"]["coordinate"]:

            if Stage.countMonster == len(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["coordinate"]):
                addSprite(mapCell, k[0], k[1], Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)]["chest"]["openImage"])
            else:    
                addSprite(mapCell, k[0], k[1], Stage.world[world]["stages"][stage]["chest"]["image"])

        for t in Stage.world[world]["stages"][stage]["target"]["coordinate"]:

            if Stage.isOpen == True:
                addSprite(mapCell, t[0], t[1], Stage.world[world]["stages"][stage]["target"]["open_door-image"])
            else: 
                addSprite(mapCell, t[0], t[1], Stage.world[world]["stages"][stage]["target"]["close_door-image"])



    else:

        for m in Stage.world[world]["stages"][stage]["boss"]["coordinate"] :

            Stage.world[world]["stages"][stage]["boss"]["info"].append({
                "name": Stage.world[world]["stages"][stage]["boss"]["name"],
                "life": Stage.world[world]["stages"][stage]["boss"]["life"],
                "strength": Stage.world[world]["stages"][stage]["boss"]["strength"],
                "defense": Stage.world[world]["stages"][stage]["boss"]["defense"],
                "level": Stage.world[world]["stages"][stage]["boss"]["level"],
                "progressPV": Stage.world[world]["stages"][stage]["boss"]["progressPV"],
                "isDroped" : Stage.world[world]["stages"][stage]["boss"]["isDroped"],
                "isAlive": Stage.world[world]["stages"][stage]["boss"]["isAlive"]
            })
            addSprite(mapCell, m[0], m[1], Stage.world[world]["stages"][stage]["boss"]["front"])

        for i in Stage.world[world]["stages"][stage]["boss"]["info"]:

            if i["life"] <= 0:
                addSprite(mapCell, 0, 0, "") 

        
        for t in Stage.world[world]["stages"][stage]["target"]["coordinate"]:

            if Stage.isDead == True:
                addSprite(mapCell, t[0], t[1], Stage.world[world]["stages"][stage]["target"]["open_door-image"])
            else: 
                addSprite(mapCell, t[0], t[1], Stage.world[world]["stages"][stage]["target"]["close_door-image"])

