
from functions.game_functions.Hero import *


class Stage:

    saveDropItems = []
    inventaire = []
    messageTab = []
    isOpen = False
    isDead = False
 
    Shield_use = False
    countMonster = 0
    countKey = 0

    worldArray = ["grassland", "lavaland", "iceland",  "cloudland", "demonicland"]
    indexWorld = 0
    currentWorld = worldArray[indexWorld]
    currentStage = 1

    world = {
        "grassland":{

            "stages": {

                "stage 1" : {

                    "name": "Grassland : Stage 1",
                    "description": "",
                    "top-background": "background: url(test/images/map/top-grassland.png);",
                    "background": "border: none;" "margin: auto;" "background: url(test/images/map/Grassland.png) no-repeat center center;",
                    "monsters": {
                        "name": "Orc",
                        "life": 25,
                        "progressPV": 100,
                        "strength": 50,
                        "defense": 10,
                        "level": 1,
                        "info": [],
                        "coordinate" : [],
                        "drop": ["aucun item", "petite potion de hp", "petit bouclier"],
                        "isDroped": False,
                        "isAlive": True,
                        "front": "background: url(test/sprites/monsters/monster-stage1_front-left.png);" "background-position: top",
                        "back": "background: url(test/sprites/monsters/monster-stage1_right-back.png);" "background-position: bottom",
                        "left":"background: url(test/sprites/monsters/monster-stage1_front-left.png);" "background-position: bottom",
                        "right": "background: url(test/sprites/monsters/monster-stage1_right-back.png);" "background-position: top",
                        "face": "background: url(test/sprites/monsters/monster-face_stage1.png);",
                        "dead": "background: url(test/sprites/monsters/Dead_monster-stage1.png);",                      
                    },
                    "chest": {
                        "name": "Coffre du donjon",
                        "description": "",
                        "image": "background: url(test/sprites/items/chest1.png);"  "background-position: top",
                        "openImage": "background: url(test/sprites/items/chest2.png);"  "background-position: bottom",
                        "coordinate" : [],
                        "drop": ["clée du donjon"],
                    },
                    "target": {
                        "name": "Portail",
                        "description": "",
                        "coordinate" : [],
                        "close_door-image": "background: url(test/sprites/items/close_green-door.png);",
                        "open_door-image": "background: url(test/sprites/items/open_green-door.png);"
                    },
                },

                "stage 2" : {

                    "name": "Grassland : Stage 2",
                    "description": "",
                    "top-background": "background: url(test/images/map/top-grassland.png);",
                    "background": "border: none;" "margin: auto;" "background: url(test/images/map/Grassland.png) no-repeat center center;",
                    "monsters": {
                        "name": "Orc",
                        "life": 30,
                        "progressPV": 100,
                        "strength": 55,
                        "defense": 15,
                        "level": 2,
                        "info": [],
                        "coordinate" : [],
                        "drop": ["aucun item", "petite potion de hp", "petit bouclier"],
                        "isDroped": False,
                        "isAlive": True,
                        "front":"background: url(test/sprites/monsters/monster-stage1_front-left.png);"  "background-position: top",
                        "back": "background: url(test/sprites/monsters/monster-stage1_right-back.png);"  "background-position: bottom",
                        "left":"background: url(test/sprites/monsters/monster-stage1_front-left.png);"  "background-position: bottom",
                        "right": "background: url(test/sprites/monsters/monster-stage1_right-back.png);"  "background-position: top",
                        "face": "background: url(test/sprites/monsters/monster-face_stage1.png);",
                        "dead": "background: url(test/sprites/monsters/Dead_monster-stage1.png);",
                    },
                    "chest": {
                        "name": "Coffre du donjon",
                        "description": "",
                        "image": "background: url(test/sprites/items/chest1.png);"  "background-position: top",
                        "openImage": "background: url(test/sprites/items/chest2.png);"  "background-position: bottom",
                        "coordinate" : [],
                        "drop": ["clée du donjon"],
                    },
                    "target": {
                        "name": "Portail",
                        "description": "",
                        "coordinate" : [],
                        "close_door-image": "background: url(test/sprites/items/close_green-door.png);",
                        "open_door-image": "background: url(test/sprites/items/open_green-door.png);"
                    },
                },

                "stage 3" : {

                    "name": "Grassland : Stage 3",
                    "description": "",
                    "top-background": "background: url(test/images/map/top-grassland-stage3_4.png);",
                    "background": "border: none;" "margin: auto;" "background: url(test/images/map/grassland-stage3_4.png) no-repeat center center;",
                    "monsters": {
                        "name": "Orc",
                        "life": 45,
                        "progressPV": 100,
                        "strength": 60,
                        "defense": 30,
                        "level": 3,
                        "info": [],
                        "coordinate" : [],
                        "drop": ["aucun item", "petite potion de hp", "petit bouclier"],
                        "isDroped": False,
                        "isAlive": True,
                        "front":"background: url(test/sprites/monsters/monster-stage1_front-left.png);"  "background-position: top",
                        "back": "background: url(test/sprites/monsters/monster-stage1_right-back.png);"  "background-position: bottom",
                        "left":"background: url(test/sprites/monsters/monster-stage1_front-left.png);"  "background-position: bottom",
                        "right": "background: url(test/sprites/monsters/monster-stage1_right-back.png);"  "background-position: top",
                        "face": "background: url(test/sprites/monsters/monster-face_stage1.png);",
                        "dead": "background: url(test/sprites/monsters/Dead_monster-stage1.png);",
                    },
                    "chest": {
                        "name": "Coffre du donjon",
                        "description": "",
                        "image": "background: url(test/sprites/items/chest1.png);"  "background-position: top",
                        "openImage": "background: url(test/sprites/items/chest2.png);"  "background-position: bottom",
                        "coordinate" : [],
                        "drop": ["clée du donjon"],
                    },
                    "target": {
                        "name": "Portail",
                        "description": "",
                        "coordinate" : [],
                        "close_door-image": "background: url(test/sprites/items/close_green-door.png);",
                        "open_door-image": "background: url(test/sprites/items/open_green-door.png);"
                    },
                },

                "stage 4" : {

                    "name": "Grassland : Stage 4",
                    "top-background": "background: url(test/images/map/top-grassland-stage3_4.png);",
                    "background": "border: none;" "margin: auto;" "background: url(test/images/map/grassland-stage3_4.png) no-repeat center center;",
                    "monsters": {
                        "name": "Orc",
                        "life": 65,
                        "progressPV": 100,
                        "strength": 80,
                        "defense": 50,
                        "level": 4,
                        "info": [],
                        "coordinate" : [],
                        "drop": ["aucun item", "petite potion de hp", "petit bouclier"],
                        "isDroped": False,
                        "isAlive": True,
                        "front":"background: url(test/sprites/monsters/monster-stage1_front-left.png);"  "background-position: top",
                        "back": "background: url(test/sprites/monsters/monster-stage1_right-back.png);"  "background-position: bottom",
                        "left":"background: url(test/sprites/monsters/monster-stage1_front-left.png);"  "background-position: bottom",
                        "right": "background: url(test/sprites/monsters/monster-stage1_right-back.png);"  "background-position: top",
                        "face": "background: url(test/sprites/monsters/monster-face_stage1.png);",
                        "dead": "background: url(test/sprites/monsters/Dead_monster-stage1.png);",
                    },
                    "chest": {
                        "name": "Coffre du donjon",
                        "description": "",
                        "image": "background: url(test/sprites/items/chest1.png);"  "background-position: top",
                        "openImage": "background: url(test/sprites/items/chest2.png);"  "background-position: bottom",
                        "coordinate" : [],
                        "drop": ["clée du donjon"],
                    },
                    "target": {
                        "name": "Portail",
                        "description": "",
                        "coordinate" : [],
                        "close_door-image": "background: url(test/sprites/items/close_green-door.png);",
                        "open_door-image": "background: url(test/sprites/items/open_green-door.png);"
                    },
                },

                "stage 5" : {

                    "name": "Grassland : Stage final",
                    "description": "",
                    "top-background": "background: url(test/images/map/top-grassland-stage_5.png);",
                    "background": "border: none;" "margin: auto;" "background: url(test/images/map/grassland-stage_5.png) no-repeat center center;",
                    "boss": {
                        "name": "Emulan", 
                        "life": 100,
                        "progressPV": 100,
                        "strength": 105,
                        "defense": 80,
                        "level": 5,     
                        "info": [],
                        "coordinate" : [],
                        "drop": ["pierre eternel"],
                        "isDroped": False,
                        "isAlive": True,
                        "front":"background: url(test/sprites/monsters/boss-stage_1.png);",
                        "face": "background: url(test/sprites/monsters/boss-image/face_Emulan.png);",
                        "pierre" : "background: url(test/sprites/monsters/Dead_monster-stage1.png) 0 0 0 0 no-repeat streach streach;", 
                    },
                    "chest": {
                        "name": "Coffre du donjon",
                        "description": "",
                        "image": "background: url(test/sprites/items/chest1.png);"  "background-position: top",
                        "openImage": "background: url(test/sprites/items/chest2.png);"  "background-position: bottom",
                        "coordinate" : [],
                        "drop": ["clée du donjon"],
                    },
                    "target": {
                        "name": "Portail",
                        "description": "",
                        "coordinate" : [],
                        "close_door-image": "background: url(test/sprites/items/close_red-door.png);",
                        "open_door-image": "background: url(test/sprites/items/open_red-door.png);"
                    },
                },

            },

        },

        "lavaland": {

            "stages": {

                "stage 1" : {

                    "name": "Lavaland stage 1",
                    "top-background": "background: url(test/images/map/top-lavaland_stage-1-4.png);",
                    "background": "border: none;" "margin: auto;" "background: url(test/images/map/lavaland_stage1-2.png) no-repeat center center;",
                    "monsters": {
                        "name": "Chimère",
                        "life": 110,
                        "progressPV": 100,
                        "strength": 115,
                        "defense": 90,
                        "level": 6,                        
                        "info": [],
                        "coordinate" : [],
                        "drop": ["aucun item", "petite potion de hp", "petit bouclier"],
                        "isDroped": False,
                        "isAlive": True,
                        "front":"background: url(test/sprites/monsters/monster-stage3_front-left.png);"  "background-position: top",
                        "back": "background: url(test/sprites/monsters/monster-stage3_right-back.png);"  "background-position: bottom",
                        "left":"background: url(test/sprites/monsters/monster-stage3_front-left.png);"  "background-position: bottom",
                        "right": "background: url(test/sprites/monsters/monster-stage3_right-back.png);"  "background-position: top",
                        "face": "background: url(test/sprites/monsters/monster-face_stage3.png);",
                        "dead": "background: url(test/sprites/monsters/chimere-dead.png);",
                    },
                    "chest": {
                        "name": "Coffre du donjon",
                        "description": "",
                        "image": "background: url(test/sprites/items/chest1.png);"  "background-position: top",
                        "openImage": "background: url(test/sprites/items/chest2.png);"  "background-position: bottom",
                        "coordinate" : [],
                        "drop": ["clée du donjon"],
                    },
                    "target": {
                        "name": "Portail",
                        "description": "",
                        "coordinate" : [],
                        "close_door-image": "background: url(test/sprites/items/close_red-door.png);",
                        "open_door-image": "background: url(test/sprites/items/open_red-door.png);"
                    },
                },

                "stage 2" : {

                    "name": "Lavaland stage 2",
                    "description": "",
                    "top-background": "background: url(test/images/map/top-lavaland_stage-1-4.png);",
                    "background": "border: none;" "margin: auto;" "background: url(test/images/map/lavaland_stage1-2.png) no-repeat center center;",
                    "monsters": {
                        "name": "Chimère",
                        "life": 120,
                        "progressPV": 100,
                        "strength": 125,
                        "defense": 100,
                        "level": 7,  
                        "info": [],
                        "coordinate" : [],
                        "drop": ["aucun item", "petite potion de hp", "petit bouclier"],
                        "isDroped": False,
                        "isAlive": True,
                        "front":"background: url(test/sprites/monsters/monster-stage3_front-left.png);"  "background-position: top",
                        "back": "background: url(test/sprites/monsters/monster-stage3_right-back.png);"  "background-position: bottom",
                        "left":"background: url(test/sprites/monsters/monster-stage3_front-left.png);"  "background-position: bottom",
                        "right": "background: url(test/sprites/monsters/monster-stage3_right-back.png);"  "background-position: top",
                        "face": "background: url(test/sprites/monsters/monster-face_stage3.png);",
                        "dead": "background: url(test/sprites/monsters/chimere-dead.png);",
                    },
                    "chest": {
                        "name": "Coffre du donjon",
                        "description": "",
                        "image": "background: url(test/sprites/items/chest1.png);"  "background-position: top",
                        "openImage": "background: url(test/sprites/items/chest2.png);"  "background-position: bottom",
                        "coordinate" : [],
                        "drop": ["clée du donjon"],
                    },
                    "target": {
                        "name": "Portail",
                        "description": "",
                        "coordinate" : [],
                        "close_door-image": "background: url(test/sprites/items/close_red-door.png);",
                        "open_door-image": "background: url(test/sprites/items/open_red-door.png);"
                    },
                },

                "stage 3" : {

                    "name": "Lavaland stage 3",
                    "description": "",
                    "top-background": "background: url(test/images/map/top-lavaland_stage-1-4.png);",
                    "background": "border: none;" "margin: auto;" "background: url(test/images/map/lavaland_stage2-3.png) no-repeat center center;",
                    "monsters": {
                        "name": "Chimère",
                        "life": 125,
                        "progressPV": 100,
                        "strength": 130,
                        "defense": 105,
                        "level": 8,  
                        "info": [],
                        "coordinate" : [],
                        "drop": ["aucun item", "petite potion de hp", "petit bouclier"],
                        "isDroped": False,
                        "isAlive": True,
                        "front":"background: url(test/sprites/monsters/monster-stage3_front-left.png);"  "background-position: top",
                        "back": "background: url(test/sprites/monsters/monster-stage3_right-back.png);"  "background-position: bottom",
                        "left":"background: url(test/sprites/monsters/monster-stage3_front-left.png);"  "background-position: bottom",
                        "right": "background: url(test/sprites/monsters/monster-stage3_right-back.png);"  "background-position: top",
                        "face": "background: url(test/sprites/monsters/monster-face_stage3.png);",
                        "dead": "background: url(test/sprites/monsters/chimere-dead.png);",
                    },
                    "chest": {
                        "name": "Coffre du donjon",
                        "description": "",
                        "image": "background: url(test/sprites/items/chest1.png);"  "background-position: top",
                        "openImage": "background: url(test/sprites/items/chest2.png);"  "background-position: bottom",
                        "coordinate" : [],
                        "drop": ["clée du donjon"],
                    },
                    "target": {
                        "name": "Portail",
                        "description": "",
                        "coordinate" : [],
                        "close_door-image": "background: url(test/sprites/items/close_red-door.png);",
                        "open_door-image": "background: url(test/sprites/items/open_red-door.png);"
                    },
                },

                "stage 4" : {

                    "name": "Lavaland stage 4",
                    "description": "",
                    "top-background": "background: url(test/images/map/top-lavaland_stage-1-4.png);",
                    "background": "border: none;" "margin: auto;" "background: url(test/images/map/lavaland_stage2-3.png) no-repeat center center;",
                    "monsters": {
                        "name": "Chimère",
                        "life": 130,
                        "progressPV": 100,
                        "strength": 135,
                        "defense": 110,
                        "level": 9,  
                        "info": [],
                        "coordinate" : [],
                        "drop": ["aucun item", "petite potion de hp", "petit bouclier"],
                        "isDroped": False,
                        "isAlive": True,
                        "front":"background: url(test/sprites/monsters/monster-stage3_front-left.png);"  "background-position: top",
                        "back": "background: url(test/sprites/monsters/monster-stage3_right-back.png);"  "background-position: bottom",
                        "left":"background: url(test/sprites/monsters/monster-stage3_front-left.png);"  "background-position: bottom",
                        "right": "background: url(test/sprites/monsters/monster-stage3_right-back.png);"  "background-position: top",
                        "face": "background: url(test/sprites/monsters/monster-face_stage3.png);",
                        "dead": "background: url(test/sprites/monsters/chimere-dead.png);",
                    },
                    "chest": {
                        "name": "Coffre du donjon",
                        "description": "",
                        "image": "background: url(test/sprites/items/chest1.png);"  "background-position: top",
                        "openImage": "background: url(test/sprites/items/chest2.png);"  "background-position: bottom",
                        "coordinate" : [],
                        "drop": ["clée du donjon"],
                    },
                    "target": {
                        "name": "Portail",
                        "description": "",
                        "coordinate" : [],
                        "close_door-image": "background: url(test/sprites/items/close_red-door.png);",
                        "open_door-image": "background: url(test/sprites/items/open_red-door.png);"
                    },
                },

                "stage 5" : {

                    "name": "Lavaland final stage",
                    "description": "",
                    "top-background": "background: url(test/images/map/top-lavaland_stage5.png);",
                    "background": "border: none;" "margin: auto;" "background: url(test/images/map/lavaland_stage5.png) no-repeat center center;",
                    "boss": {
                        "name": "Sogrim",
                        "life": 140,
                        "progressPV": 100,
                        "strength": 145,
                        "defense": 120,
                        "level": 10,            
                        "info": [],
                        "coordinate" : [],
                        "drop": ["pierre eternel"],
                        "isDroped": False,
                        "isAlive": True,
                        "front":"background: url(test/sprites/monsters/boss-stage_2.png);",
                        "face": "background: url(test/sprites/monsters/boss-image/face_Sogrim.png);",
                        "pierre" : "background: url(test/sprites/monsters/Dead_monster-stage1.png);", 
                    },
                    "chest": {
                        "name": "Coffre du donjon",
                        "description": "",
                        "image": "background: url(test/sprites/items/chest1.png);"  "background-position: top",
                        "openImage": "background: url(test/sprites/items/chest2.png);"  "background-position: bottom",
                        "coordinate" : [],
                        "drop": ["clée du donjon"],
                    },
                    "target": {
                        "name": "Portail",
                        "description": "",
                        "coordinate" : [],
                        "close_door-image": "background: url(test/sprites/items/close_blue-door.png);",
                        "open_door-image": "background: url(test/sprites/items/open_blue-door.png);"
                    },
                },
            },
        },
        
        "iceland": {

            "stages": {

                "stage 1" : {

                    "name": "Iceland stage 1",
                    "description": "",
                    "top-background": "background: url(test/images/map/top-iceland_stage1-2.png);",
                    "background": "border: 1px solid black;"  "margin: auto;"  "background: url(test/images/map/iceland_stage1-4.png) no-repeat center center;",
                    "monsters": {
                        "name": "Slime",
                        "life": 140,
                        "progressPV": 100,
                        "strength": 145,
                        "defense": 120,
                        "level": 11,  
                        "info": [],
                        "coordinate" : [],
                        "drop": ["aucun item", "petite potion de hp", "petit bouclier"],
                        "isDroped": False,
                        "isAlive": True,
                        "front": "background: url(test/sprites/monsters/monster-stage2_front-left.png);" "background-position: top",
                        "back": "background: url(test/sprites/monsters/monster-stage2_right-back.png);" "background-position: bottom",
                        "left": "background: url(test/sprites/monsters/monster-stage2_front-left.png);" "background-position: bottom",
                        "right": "background: url(test/sprites/monsters/monster-stage2_right-back.png);" "background-position: top",
                        "face": "background: url(test/sprites/monsters/monster-face_stage2.png);",
                        "dead": "background: url(test/sprites/monsters/slime-dead.png);",
                    },
                    "chest": {
                        "name": "Coffre du donjon",
                        "description": "",
                        "image": "background: url(test/sprites/items/chest1.png);"  "background-position: top",
                        "openImage": "background: url(test/sprites/items/chest2.png);"  "background-position: bottom",
                        "coordinate" : [],
                        "drop": ["clée du donjon"],
                    },
                    "target": {
                        "name": "Portail",
                        "description": "",
                        "coordinate" : [],
                        "close_door-image": "background: url(test/sprites/items/close_blue-door.png);",
                        "open_door-image": "background: url(test/sprites/items/open_blue-door.png);"
                    },
                },

                "stage 2" : {

                    "name": "Iceland stage 2",
                    "description": "",
                    "top-background": "background: url(test/images/map/top-iceland_stage1-2.png);",
                    "background": "border: 1px solid black;"  "margin: auto;"  "background: url(test/images/map/iceland_stage1-4.png) no-repeat center center;",
                    "monsters": {
                        "name": "Slime",
                        "life": 145,
                        "progressPV": 100,
                        "strength": 150,
                        "defense": 125,
                        "level": 12,  
                        "info": [],
                        "coordinate" : [],
                        "drop": ["aucun item", "petite potion de hp", "petit bouclier"],
                        "isDroped": False,
                        "isAlive": True,
                        "front": "background: url(test/sprites/monsters/monster-stage2_front-left.png);" "background-position: top",
                        "back": "background: url(test/sprites/monsters/monster-stage2_right-back.png);" "background-position: bottom",
                        "left": "background: url(test/sprites/monsters/monster-stage2_front-left.png);" "background-position: bottom",
                        "right": "background: url(test/sprites/monsters/monster-stage2_right-back.png);" "background-position: top",
                        "face": "background: url(test/sprites/monsters/monster-face_stage2.png);",
                        "dead": "background: url(test/sprites/monsters/slime-dead.png);",
                    },
                    "chest": {
                        "name": "Coffre du donjon",
                        "description": "",
                        "image": "background: url(test/sprites/items/chest1.png);"  "background-position: top",
                        "openImage": "background: url(test/sprites/items/chest2.png);"  "background-position: bottom",
                        "coordinate" : [],
                        "drop": ["clée du donjon"],
                    },
                    "target": {
                        "name": "Portail",
                        "description": "",
                        "coordinate" : [],
                        "close_door-image": "background: url(test/sprites/items/close_blue-door.png);",
                        "open_door-image": "background: url(test/sprites/items/open_blue-door.png);"
                    },
                },

                "stage 3" : {

                    "name": "Iceland stage 3",
                    "description": "",
                    "top-background": "background: url(test/images/map/top-iceland_stage-3-4.png);",
                    "background": "border: 1px solid black;"  "margin: auto;"  "background: url(test/images/map/iceland_stage1-4.png) no-repeat center center;",
                    "monsters": {
                        "name": "Slime",
                        "life": 150,
                        "progressPV": 100,
                        "strength": 155,
                        "defense": 130,
                        "level": 13,  
                        "info": [],
                        "coordinate" : [],
                        "drop": ["aucun item", "petite potion de hp", "petit bouclier"],
                        "isDroped": False,
                        "isAlive": True,
                        "front": "background: url(test/sprites/monsters/monster-stage2_front-left.png);" "background-position: top",
                        "back": "background: url(test/sprites/monsters/monster-stage2_right-back.png);" "background-position: bottom",
                        "left": "background: url(test/sprites/monsters/monster-stage2_front-left.png);" "background-position: bottom",
                        "right": "background: url(test/sprites/monsters/monster-stage2_right-back.png);" "background-position: top",
                        "face": "background: url(test/sprites/monsters/monster-face_stage2.png);",
                        "dead": "background: url(test/sprites/monsters/slime-dead.png);",
                    },
                    "chest": {
                        "name": "Coffre du donjon",
                        "description": "",
                        "image": "background: url(test/sprites/items/chest1.png);"  "background-position: top",
                        "openImage": "background: url(test/sprites/items/chest2.png);"  "background-position: bottom",
                        "coordinate" : [],
                        "drop": ["clée du donjon"],
                    },
                    "target": {
                        "name": "Portail",
                        "description": "",
                        "coordinate" : [],
                        "close_door-image": "background: url(test/sprites/items/close_blue-door.png);",
                        "open_door-image": "background: url(test/sprites/items/open_blue-door.png);"
                    },
                },

                "stage 4" : {

                    "name": "Iceland stage 4",
                    "description": "",
                    "top-background": "background: url(test/images/map/top-iceland_stage-3-4.png);",
                    "background": "border: 1px solid black;"  "margin: auto;"  "background: url(test/images/map/iceland_stage1-4.png) no-repeat center center;",
                    "monsters": {
                        "name": "Slime",
                        "life": 155,
                        "progressPV": 100,
                        "strength": 160,
                        "defense": 135,
                        "level": 14,  
                        "info": [],
                        "coordinate" : [],
                        "drop": ["aucun item", "petite potion de hp", "petit bouclier"],
                        "isDroped": False,
                        "isAlive": True,
                        "front": "background: url(test/sprites/monsters/monster-stage2_front-left.png);" "background-position: top",
                        "back": "background: url(test/sprites/monsters/monster-stage2_right-back.png);" "background-position: bottom",
                        "left": "background: url(test/sprites/monsters/monster-stage2_front-left.png);" "background-position: bottom",
                        "right": "background: url(test/sprites/monsters/monster-stage2_right-back.png);" "background-position: top",
                        "face": "background: url(test/sprites/monsters/monster-face_stage2.png);",
                        "dead": "background: url(test/sprites/monsters/slime-dead.png);",
                    },
                    "chest": {
                        "name": "Coffre du donjon",
                        "description": "",
                        "image": "background: url(test/sprites/items/chest1.png);"  "background-position: top",
                        "openImage": "background: url(test/sprites/items/chest2.png);"  "background-position: bottom",
                        "coordinate" : [],
                        "drop": ["clée du donjon"],
                    },
                    "target": {
                        "name": "Portail",
                        "description": "",
                        "coordinate" : [],
                        "close_door-image": "background: url(test/sprites/items/close_blue-door.png);",
                        "open_door-image": "background: url(test/sprites/items/open_blue-door.png);"
                    },
                },

                "stage 5" : {

                    "name": "Iceland stage 5",
                    "description": "",
                    "top-background": "background: url(test/images/map/top-iceland_stage-5.png);",
                    "background": "border: 1px solid black;"  "margin: auto;"  "background: url(test/images/map/iceland_stage-5.png) no-repeat center center;",
                    "boss": {
                        "name": "Finstern",
                        "life": 175,
                        "progressPV": 100,
                        "strength": 170,
                        "defense": 155,
                        "level": 15,            
                        "info": [],
                        "coordinate" : [],
                        "drop": ["pierre eternel"],
                        "isDroped": False,
                        "isAlive": True,
                        "front":"background: url(test/sprites/monsters/finstern.png) no-repeat;",
                        "face": "background: url(test/sprites/monsters/boss-image/face_Finstern.png);",
                        "pierre" : "background: url(test/sprites/monsters/Dead_monster-stage1.png);",  
                    },
                    "chest": {
                        "name": "Coffre du donjon",
                        "description": "",
                        "image": "background: url(test/sprites/items/chest1.png);"  "background-position: top",
                        "openImage": "background: url(test/sprites/items/chest2.png);"  "background-position: bottom",
                        "coordinate" : [],
                        "drop": ["clée du donjon"],
                    },
                    "chest": {
                        "name": "Coffre du donjon",
                        "description": "",
                        "image": "background: url(test/sprites/items/chest1.png);"  "background-position: top",
                        "openImage": "background: url(test/sprites/items/chest2.png);"  "background-position: bottom",
                        "coordinate" : [],
                        "drop": ["clée du donjon"],
                    },
                    "target": {
                        "name": "Portail",
                        "description": "",
                        "coordinate" : [],
                        "close_door-image": "background: url(test/sprites/items/close_yel-door.png);",
                        "open_door-image": "background: url(test/sprites/items/open_yel-door.png);"
                    },
                },
            },
        },
        
        "cloudland": {

            "stages": {

                "stage 1" : {

                    "name": "Cloudland stage 1",
                    "description": "",
                    "top-background": "background: url(test/images/map/top-cloud_stage1-4.png);",
                    "background": "border: 1px solid black;"  "margin: auto;"  "background: url(test/images/map/Clouds_stage1-5.png) no-repeat center center;",
                    "monsters": {
                        "name": "Chien-Dragon",
                        "life": 180,
                        "progressPV": 100,
                        "strength": 175,
                        "defense": 160,
                        "level": 16,                           
                        "info": [],
                        "coordinate" : [],
                        "drop": ["aucun item", "petite potion de hp", "petit bouclier"],
                        "isDroped": False,
                        "isAlive": True,
                        "front":"background: url(test/sprites/monsters/monster-stage4_front-left.png);"  "background-position: top",
                        "back": "background: url(test/sprites/monsters/monster-stage4_right-back.png);"  "background-position: bottom",
                        "left":"background: url(test/sprites/monsters/monster-stage4_front-left.png);"  "background-position: bottom",
                        "right": "background: url(test/sprites/monsters/monster-stage4_right-back.png);"  "background-position: top",
                        "face": "background: url(test/sprites/monsters/monster-face_stage4.png);",
                        "dead": "background: url(test/sprites/monsters/chien-dragon_dead.png);",
                    },
                    "chest": {
                        "name": "Coffre du donjon",
                        "description": "",
                        "image": "background: url(test/sprites/items/chest1.png);"  "background-position: top",
                        "openImage": "background: url(test/sprites/items/chest2.png);"  "background-position: bottom",
                        "coordinate" : [],
                        "drop": ["clée du donjon"],
                    },
                    "target": {
                        "name": "Portail",
                        "description": "",
                        "coordinate" : [],
                        "close_door-image": "background: url(test/sprites/items/close_yel-door.png);",
                        "open_door-image": "background: url(test/sprites/items/open_yel-door.png);"
                    },
                },

                "stage 2" : {

                    "name": "Cloudland stage 2",
                    "description": "",
                    "top-background": "background: url(test/images/map/top-cloud_stage1-4.png);",
                    "background": "border: 1px solid black;"  "margin: auto;"  "background: url(test/images/map/Clouds_stage1-5.png) no-repeat center center;",
                    "monsters": {
                        "name": "Chien-Dragon",
                        "life": 185,
                        "progressPV": 100,
                        "strength": 180,
                        "defense": 165,
                        "level": 17,                           
                        "info": [],
                        "coordinate" : [],
                        "drop": ["aucun item", "petite potion de hp", "petit bouclier"],
                        "isDroped": False,
                        "isAlive": True,
                        "front":"background: url(test/sprites/monsters/monster-stage4_front-left.png);"  "background-position: top",
                        "back": "background: url(test/sprites/monsters/monster-stage4_right-back.png);"  "background-position: bottom",
                        "left":"background: url(test/sprites/monsters/monster-stage4_front-left.png);"  "background-position: bottom",
                        "right": "background: url(test/sprites/monsters/monster-stage4_right-back.png);"  "background-position: top",
                        "face": "background: url(test/sprites/monsters/monster-face_stage4.png);",
                        "dead": "background: url(test/sprites/monsters/chien-dragon_dead.png);",
                    },
                    "chest": {
                        "name": "Coffre du donjon",
                        "description": "",
                        "image": "background: url(test/sprites/items/chest1.png);"  "background-position: top",
                        "openImage": "background: url(test/sprites/items/chest2.png);"  "background-position: bottom",
                        "coordinate" : [],
                        "drop": ["clée du donjon"],
                    },
                    "target": {
                        "name": "Portail",
                        "description": "",
                        "coordinate" : [],
                        "close_door-image": "background: url(test/sprites/items/close_yel-door.png);",
                        "open_door-image": "background: url(test/sprites/items/open_yel-door.png);"
                    },
                },

                "stage 3" : {

                    "name": "Cloudland stage 3",
                    "description": "",
                    "top-background": "background: url(test/images/map/top-cloud_stage1-4.png);",
                    "background": "border: 1px solid black;"  "margin: auto;"  "background: url(test/images/map/Clouds_stage1-5.png) no-repeat center center;",
                    "monsters": {
                        "name": "Chien-Dragon",
                        "life": 190,
                        "progressPV": 100,
                        "strength": 185,
                        "defense": 170,
                        "level": 18,                           
                        "info": [],
                        "coordinate" : [],
                        "drop": ["aucun item", "petite potion de hp", "petit bouclier"],
                        "isDroped": False,
                        "isAlive": True,
                        "front":"background: url(test/sprites/monsters/monster-stage4_front-left.png);"  "background-position: top",
                        "back": "background: url(test/sprites/monsters/monster-stage4_right-back.png);"  "background-position: bottom",
                        "left":"background: url(test/sprites/monsters/monster-stage4_front-left.png);"  "background-position: bottom",
                        "right": "background: url(test/sprites/monsters/monster-stage4_right-back.png);"  "background-position: top",
                        "face": "background: url(test/sprites/monsters/monster-face_stage4.png);",
                        "dead": "background: url(test/sprites/monsters/chien-dragon_dead.png);",
                    },
                    "chest": {
                        "name": "Coffre du donjon",
                        "description": "",
                        "image": "background: url(test/sprites/items/chest1.png);"  "background-position: top",
                        "openImage": "background: url(test/sprites/items/chest2.png);"  "background-position: bottom",
                        "coordinate" : [],
                        "drop": ["clée du donjon"],
                    },
                    "target": {
                        "name": "Portail",
                        "description": "",
                        "coordinate" : [],
                        "close_door-image": "background: url(test/sprites/items/close_yel-door.png);",
                        "open_door-image": "background: url(test/sprites/items/open_yel-door.png);"
                    },
                },

                "stage 4" : {

                    "name": "Cloudland stage 4",
                    "description": "",
                    "top-background": "background: url(test/images/map/top-cloud_stage1-4.png);",
                    "background": "border: 1px solid black;"  "margin: auto;"  "background: url(test/images/map/Clouds_stage1-5.png) no-repeat center center;",
                    "monsters": {
                        "name": "Chien-Dragon",
                        "life": 195,
                        "progressPV": 100,
                        "strength": 190,
                        "defense": 175,
                        "level": 19,                           
                        "info": [],
                        "coordinate" : [],
                        "drop": ["aucun item", "petite potion de hp", "petit bouclier"],
                        "isDroped": False,
                        "isAlive": True,
                        "front":"background: url(test/sprites/monsters/monster-stage4_front-left.png);"  "background-position: top",
                        "back": "background: url(test/sprites/monsters/monster-stage4_right-back.png);"  "background-position: bottom",
                        "left":"background: url(test/sprites/monsters/monster-stage4_front-left.png);"  "background-position: bottom",
                        "right": "background: url(test/sprites/monsters/monster-stage4_right-back.png);"  "background-position: top",
                        "face": "background: url(test/sprites/monsters/monster-face_stage4.png);",
                        "dead": "background: url(test/sprites/monsters/chien-dragon_dead.png);",
                    },
                    "chest": {
                        "name": "Coffre du donjon",
                        "description": "",
                        "image": "background: url(test/sprites/items/chest1.png);"  "background-position: top",
                        "openImage": "background: url(test/sprites/items/chest2.png);"  "background-position: bottom",
                        "coordinate" : [],
                        "drop": ["clée du donjon"],
                    },
                    "target": {
                        "name": "Portail",
                        "description": "",
                        "coordinate" : [],
                        "close_door-image": "background: url(test/sprites/items/close_yel-door.png);",
                        "open_door-image": "background: url(test/sprites/items/open_yel-door.png);"
                    },
                },

                "stage 5" : {

                    "name": "Cloudland final stage",
                    "description": "",
                    "top-background": "background: url(test/images/map/top-clouds_stage5.png);",
                    "background": "border: 1px solid black;"  "margin: auto;"  "background: url(test/images/map/Clouds_stage1-5.png) no-repeat center center;",
                    "boss": {
                        "name": "Vitusa",
                        "life": 205,
                        "progressPV": 100,
                        "strength": 200,
                        "defense": 185,
                        "level": 20,               
                        "info": [],
                        "coordinate" : [],
                        "drop": ["pierre eternel"],
                        "isDroped": False,
                        "isAlive": True,
                        "front":"background: url(test/sprites/monsters/vitusa.png) no-repeat;",
                        "face": "background: url(test/sprites/monsters/boss-image/face_Vitusa.png);",
                        "pierre" : "background: url(test/sprites/monsters/Dead_monster-stage1.png);", 
                    },
                    "chest": {
                        "name": "Coffre du donjon",
                        "description": "",
                        "image": "background: url(test/sprites/items/chest1.png);"  "background-position: top",
                        "openImage": "background: url(test/sprites/items/chest2.png);"  "background-position: bottom",
                        "coordinate" : [],
                        "drop": ["clée du donjon"],
                    },
                    "target": {
                        "name": "Portail",
                        "description": "",
                        "coordinate" : [],
                        "close_door-image": "background: url(test/sprites/items/close_yel-door.png);",
                        "open_door-image": "background: url(test/sprites/items/open_yel-door.png);"
                    },
                },
            },
        },
        
        "demonicland": {

            "stages": {

                "stage 1" : {

                    "name": "demonicland stage 1",
                    "description": "",
                    "top-background": "background: url(test/images/map/top-demonic_stage1-2.png);",
                    "background": "border: 1px solid black;"  "margin: auto;"  "background: url(test/images/map/Demonic_stage1-2.png) no-repeat center center;",
                    "monsters": {
                        "name": "Diablotin",
                        "life": 210,
                        "progressPV": 100,
                        "strength": 205,
                        "defense": 190,
                        "level": 21,                            
                        "info": [],
                        "coordinate" : [],
                        "drop": ["aucun item", "petite potion de hp", "petit bouclier"],
                        "isDroped": False,
                        "isAlive": True,
                        "front":"background: url(test/sprites/monsters/monster-stage5_front-left.png);"  "background-position: top",
                        "back": "background: url(test/sprites/monsters/monster-stage5_right-back.png);"  "background-position: bottom",
                        "left":"background: url(test/sprites/monsters/monster-stage5_front-left.png);"  "background-position: bottom",
                        "right": "background: url(test/sprites/monsters/monster-stage5_right-back.png);"  "background-position: top",
                        "face": "background: url(test/sprites/monsters/monster-face_stage5.png);",
                        "dead": "background: url(test/sprites/monsters/diablotin_dead.png);",
                    },
                    "chest": {
                        "name": "Coffre du donjon",
                        "description": "",
                        "image": "background: url(test/sprites/items/chest1.png);"  "background-position: top",
                        "openImage": "background: url(test/sprites/items/chest2.png);"  "background-position: bottom",
                        "coordinate" : [],
                        "drop": ["clée du donjon"],
                    },
                    "target": {
                        "name": "Portail",
                        "description": "",
                        "coordinate" : [],
                        "close_door-image": "background: url(test/sprites/items/close_yel-door.png);",
                        "open_door-image": "background: url(test/sprites/items/open_yel-door.png);"
                    },
                },

                "stage 2" : {

                    "name": "Demonicland stage 2",
                    "description": "",
                    "top-background": "background: url(test/images/map/top-demonic_stage1-2.png);",
                    "background": "border: 1px solid black;"  "margin: auto;"  "background: url(test/images/map/Demonic_stage1-2.png) no-repeat center center;",
                    "monsters": {
                        "name": "Diablotin",
                        "life": 215,
                        "progressPV": 100,
                        "strength": 210,
                        "defense": 195,
                        "level": 22,                            
                        "info": [],
                        "coordinate" : [],
                        "drop": ["aucun item", "petite potion de hp", "petit bouclier"],
                        "isDroped": False,
                        "isAlive": True,
                        "front":"background: url(test/sprites/monsters/monster-stage5_front-left.png);"  "background-position: top",
                        "back": "background: url(test/sprites/monsters/monster-stage5_right-back.png);"  "background-position: bottom",
                        "left":"background: url(test/sprites/monsters/monster-stage5_front-left.png);"  "background-position: bottom",
                        "right": "background: url(test/sprites/monsters/monster-stage5_right-back.png);"  "background-position: top",
                        "face": "background: url(test/sprites/monsters/monster-face_stage5.png);",
                        "dead": "background: url(test/sprites/monsters/diablotin_dead.png);",
                    },
                    "chest": {
                        "name": "Coffre du donjon",
                        "description": "",
                        "image": "background: url(test/sprites/items/chest1.png);"  "background-position: top",
                        "openImage": "background: url(test/sprites/items/chest2.png);"  "background-position: bottom",
                        "coordinate" : [],
                        "drop": ["clée du donjon"],
                    },
                    "target": {
                        "name": "Portail",
                        "description": "",
                        "coordinate" : [],
                        "close_door-image": "background: url(test/sprites/items/close_yel-door.png);",
                        "open_door-image": "background: url(test/sprites/items/open_yel-door.png);"
                    },
                },

                "stage 3" : {

                    "name": "Demonicland stage 3",
                    "description": "",
                    "top-background": "background: url(test/images/map/top-demonic_stage3-4.png);",
                    "background": "border: 1px solid black;"  "margin: auto;"  "background: url(test/images/map/demonic_stage3-4.png) no-repeat center center;",
                    "monsters": {
                        "name": "Diablotin",
                        "life": 220,
                        "progressPV": 100,
                        "strength": 215,
                        "defense": 200,
                        "level": 23,                            
                        "info": [],
                        "coordinate" : [],
                        "drop": ["aucun item", "petite potion de hp", "petit bouclier"],
                        "isDroped": False,
                        "isAlive": True,
                        "front":"background: url(test/sprites/monsters/monster-stage5_front-left.png);"  "background-position: top",
                        "back": "background: url(test/sprites/monsters/monster-stage5_right-back.png);"  "background-position: bottom",
                        "left":"background: url(test/sprites/monsters/monster-stage5_front-left.png);"  "background-position: bottom",
                        "right": "background: url(test/sprites/monsters/monster-stage5_right-back.png);"  "background-position: top",
                        "face": "background: url(test/sprites/monsters/monster-face_stage5.png);",
                        "dead": "background: url(test/sprites/monsters/diablotin_dead.png);",
                    },
                    "chest": {
                        "name": "Coffre du donjon",
                        "description": "",
                        "image": "background: url(test/sprites/items/chest1.png);"  "background-position: top",
                        "openImage": "background: url(test/sprites/items/chest2.png);"  "background-position: bottom",
                        "coordinate" : [],
                        "drop": ["clée du donjon"],
                    },
                    "target": {
                        "name": "Portail",
                        "description": "",
                        "coordinate" : [],
                        "close_door-image": "background: url(test/sprites/items/close_yel-door.png);",
                        "open_door-image": "background: url(test/sprites/items/open_yel-door.png);"
                    },
                },

                "stage 4" : {

                    "name": "Demonicland stage 4",
                    "description": "",
                    "top-background": "background: url(test/images/map/top-demonic_stage3-4.png);",
                    "background": "border: 1px solid black;"  "margin: auto;"  "background: url(test/images/map/demonic_stage3-4.png) no-repeat center center;",
                    "monsters": {
                        "name": "Diablotin",
                        "life": 225,
                        "progressPV": 100,
                        "strength": 220,
                        "defense": 205,
                        "level": 24,                            
                        "info": [],
                        "coordinate" : [],
                        "drop": ["aucun item", "petite potion de hp", "petit bouclier"],
                        "isDroped": False,
                        "isAlive": True,
                        "front":"background: url(test/sprites/monsters/monster-stage5_front-left.png);"  "background-position: top",
                        "back": "background: url(test/sprites/monsters/monster-stage5_right-back.png);"  "background-position: bottom",
                        "left":"background: url(test/sprites/monsters/monster-stage5_front-left.png);"  "background-position: bottom",
                        "right": "background: url(test/sprites/monsters/monster-stage5_right-back.png);"  "background-position: top",
                        "face": "background: url(test/sprites/monsters/monster-face_stage5.png);",
                        "dead": "background: url(test/sprites/monsters/diablotin_dead.png);",
                    },
                    "chest": {
                        "name": "Coffre du donjon",
                        "description": "",
                        "image": "background: url(test/sprites/items/chest1.png);"  "background-position: top",
                        "openImage": "background: url(test/sprites/items/chest2.png);"  "background-position: bottom",
                        "coordinate" : [],
                        "drop": ["clée du donjon"],
                    },
                    "target": {
                        "name": "Portail",
                        "description": "",
                        "coordinate" : [],
                        "close_door-image": "background: url(test/sprites/items/close_yel-door.png);",
                        "open_door-image": "background: url(test/sprites/items/open_yel-door.png);"
                    },
                },

                "stage 5" : {

                    "name": "Demonicland final stage",
                    "description": "",
                    "top-background": "background: url(test/images/map/top-demonic_stage5.png);",
                    "background": "border: 1px solid black;"  "margin: auto;"  "background: url(test/images/map/demonic_stage3-4.png) no-repeat center center;",
                    "boss": {
                        "name": "Ouroboros",
                        "life": 230,
                        "progressPV": 100,
                        "strength": 225,
                        "defense": 215,
                        "level": 25,                  
                        "info": [],
                        "coordinate" : [],
                        "drop": ["pierre eternel"],
                        "isDroped": False,
                        "isAlive": True,
                        "front":"background: url(test/sprites/monsters/Ouroboros.png) no-repeat;",
                        "face": "background: url(test/sprites/monsters/boss-image/face_Ouroboros.png);",
                        "pierre" : "background: url(test/sprites/monsters/Dead_monster-stage1.png);", 
                    },
                    "chest": {
                        "name": "Coffre du donjon",
                        "description": "",
                        "image": "background: url(test/sprites/items/chest1.png);"  "background-position: top",
                        "openImage": "background: url(test/sprites/items/chest2.png);"  "background-position: bottom",
                        "coordinate" : [],
                        "drop": ["clée du donjon"],
                    },
                    "target": {
                        "name": "Portail",
                        "description": "",
                        "coordinate" : [],
                        "close_door-image": "background: url(test/sprites/items/close_yel-door.png);",
                        "open_door-image": "background: url(test/sprites/items/open_yel-door.png);"
                    },
                },
            },
        }
    }

    dropInfo = {
        "petite potion de hp": {
            "description": "",
            "image": "border-image: url(test/sprites/items/hp_potion.png) 0 0 0 0 no-repeat streach streach;",
            "effect": 50,
        },
        "petit bouclier": {
            "description": "",
            "image": "border-image: url(test/sprites/items/petit_bouclier.png) 0 0 0 0 no-repeat streach streach;",
            "effect" : 20,
        },
        "clée du donjon": {
            "description": "",
            "image": "border-image: url(test/sprites/items/dunjon_key.png) 0 0 0 0 no-repeat streach streach;"
        }

    }
