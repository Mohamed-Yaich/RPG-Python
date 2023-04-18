import signal
import os
import sys
import time
import random 
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import Signal, QUrl
from PySide6.QtGui import QIcon, QFont, QFontDatabase
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QWidget, QLabel
from functions.interface_functions.centralWindow import *
from functions.game_functions.stages.Stage import *
from functions.game_functions.addMonsterInMap import *
from functions.game_functions.gameScreen import *
from functions.game_functions.createMonsterPanel import *
from functions.game_functions.addSprite import *
from functions.interface_functions.gameMainTitleScreen import *
from functions.game_functions.addAttackIndication import *
from functions.game_functions.closeFunction import *
from functions.game_functions.stages.nextStage import *
from functions.game_functions.stages.nextStage import *
from functions.game_functions.addPanelGoals import *
from functions.game_functions.generateRandomCoordinate import *
from functions.game_functions.createHeroPanel import *
from functions.interface_functions.addShortcutInventoryLabel import *




class WelcomeDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Game Info")
        self.setMinimumSize(1200, 780)
        self.setWindowIcon(QIcon("icons/rpg.png"))
        self.setStyleSheet("background-color: #000000;")
        title = QLabel("Histoire du Jeu", self)
        title.move(310, 25)
        title.setFont(QFont("Yeon Sung", 40))
        title.setStyleSheet("color: white;")
        title2 = QLabel("Controles", self)
        title2.move(355, 440)
        title2.setFont(QFont("Yeon Sung", 40))
        title2.setStyleSheet("color: white;")
        synopsys = QLabel("Bienvenue dans Empire of Chaos, l'objectif principal du jeu est de recueillir \nles 4 clés dispersés dans les 4 endroits remplis de traces magiques, que \nvous devrez explorer ils sont gouvernés par des êtres puissants et ainsi \nvaincre Ouroboros, une créature terrifiante qui a jadis détruit votre rayaume \ntout entier avec le but de récupérer le plus de pouvoir magique possible et\n devenir immortel, vous devez donc partir de rien pour arriver à sauver le \n                           monde avant que ce ne soit trop tard.\n\n Vous vous êtes donc mis sur la quête de votre ennemi juré, après un long\n voyage et une longue enquête pour pouvoir déterminer où se situait son\n repère vous apprétez à entrer dans les zones où a été vu Ouroboros le\n plus souvent et décidez d'aller vérifier malgré la présence de nombreux\n                                               monstres.", self)
        synopsys.move(220, 120)
        id = QFontDatabase.addApplicationFont("YeonSung-Regular.ttf")
        synopsys.setFont(QFont("Yeon Sung", 12))
        synopsys.setStyleSheet("color: white;")
        
        controls = QLabel("                               Entrée = Attaquer/Intéragir      Flèches du Clavier = Se Déplacer\n\n A = Slot 1 de l'Inventaire      Z = Slot 2 de l'Inventaire      E = Slot 3 de l'Inventaire      R = Slot 4 de l'Inventaire\n\nT = Slot 5 de l'Inventaire      Y = Slot 6 de l'Inventaire      U = Slot 7 de l'Inventaire      I = Slot 8 de l'Inventaire\n\nO = Slot 9 de l'Inventaire      P = Slot 10 de l'Inventaire    Q = Slot 11 de l'Inventaire    S = Slot 12 de l'Inventaire\n\nD = Slot 13 de l'Inventaire    F = Slot 14 de l'Inventaire      G = Slot 15 de l'Inventaire    H = Slot 16 de l'Inventaire", self)
        controls.move(120, 530)
        controls.setFont(QFont("Yeon Sung", 12))
        controls.setStyleSheet("color: white;")

        close_button = QPushButton("Fermer", self)
        close_button.move(80, 750)
        close_button.setFont(QFont("Yeon Sung"))
        close_button.setStyleSheet(f"""
                QPushButton {{
                            color: white;
                            font-size: 18px;
                            background: none;
                            border: none;}}
                
            """)
        close_button.clicked.connect(self.close)

    def close_game(self):
        self.close()
        self.close_game_signal.emit()


class GameWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_menu = self

        self.setWindowTitle("Empire Of Chaos")
        self.setMinimumSize(1275, 1000)
        self.setWindowIcon(QIcon("icons/rpg.png"))

        close_game_signal = Signal()

        centralArea = centralWindow(self)

        def launchGame():
            self.welcome_dialog = WelcomeDialog()
            self.welcome_dialog.show()
            panelMainTitle.deleteLater()
            generateRandomCoordinate(Stage.currentWorld, "stage {}".format(Stage.currentStage))
            centralArea = centralWindow(self)
            gameWindow = gameScreen(Stage.currentWorld, "stage {}".format(Stage.currentStage),  centralArea)
            addShortcutInventoryLabel(gameWindow)
            createHeroPanel(gameWindow, Hero.life)
            addPanelGoals(
                gameWindow, 
                Stage.countMonster, 
                Stage.currentWorld, 
                "stage {}".format(Stage.currentStage), 
                Stage.countKey
            )

        def play_music():
            self.player = QMediaPlayer()
            audioOutput = QAudioOutput()
            self.player.setAudioOutput(audioOutput)
            file_path = "music/DMT.mp3"
            self.player.setSource(QUrl.fromLocalFile(file_path))
            audioOutput.setVolume(80)
            self.player.setLoops(-1)
            self.player.play()
            if self.player.state() == QMediaPlayer.PlayingState:
                print("Music is playing")
            else:
                print("Music is not playing")

        def show_credits():
            credits_window = QDialog()
            credits_window.setWindowTitle("Credits")
            credits_window.setMinimumSize(1200, 650) 
            credits_window.setWindowIcon(QIcon("icons/rpg.png"))
            credits_title = QLabel("Développeurs & Tâches", credits_window)
            credits_title.move(200, 60)
            credits_title.setFont(QFont("Yeon Sung", 40))
            credits_label = QLabel("• LEAD DEV : William Vandal (groupe 1) ---> Map, Système de Combats, d'EXP, de Vie, de mouvements, Sprites, Débug \n\n• DEV : Lucas Yalman (groupe 2) ---> Menu Principal (Boutons et leurs fonctions, Background, Design, Modal Message \ndu Jeu), Musique de fond\n\n• DEV : Mohamed Yaich (groupe 1) ---> Inventaire et lien entre l'inventaire et le jeu + touches de raccourcis, Panel \nObjectifs et Redesign de la map\n\n• DEV : Ken's (groupe 1) ---> Messages qui s'affichent en jeu décrivant l'action que le joueur fait ou subit au lieu \nd'être print sur la console \n\n\n\n• Le projet a été entièrement réalisé avec l'aide de PyQt6 malgré la faible documentation de disponible, \nénormément de disfonctionnement qu'on a du ainsi contourner en essayant plusieurs façons de faire, \nun projet assez complet dans son ensemble malgré le peu de temps et de difficulté qu'on a eu, en espérant que \ncela vous plaise.", credits_window)
            credits_label.move(100, 190)
            id = QFontDatabase.addApplicationFont("YeonSung-Regular.ttf")
            credits_label.setFont(QFont("Yeon Sung", 12))
            credits_window.setStyleSheet("color : white;" "background : black;")
            credits_window.show()
            close_game_signal.connect(show_credits)


        panelMainTitle = QWidget(self)
        panelMainTitle.setGeometry(0, 0, 1275, 900)
        panelMainTitle.setStyleSheet("background: url(home.jpg) no-repeat center;")

        StartGame = QPushButton("Start", panelMainTitle)
        StartGame.setGeometry(500, 340, 300, 40)
        StartGame.clicked.connect(launchGame)
        id = QFontDatabase.addApplicationFont("YeonSung-Regular.ttf")
        StartGame.setFont(QFont("Yeon Sung", 25))
        StartGame.setStyleSheet(f"""
                QPushButton {{
                            background : none;
                            border: none;}}
                
                QPushButton:pressed {{
                                    background : white; 
                                    color: #000000; 
                                    font-weight: bold; 
                                    font-size : 18px; 
                                    border: none;
                                    border-radius: 10px;}}
                                    """)

        credits = QPushButton("Credits", panelMainTitle)
        credits.setGeometry(500, 400, 300, 40)
        credits.clicked.connect(show_credits) 
        id = QFontDatabase.addApplicationFont("YeonSung-Regular.ttf")
        credits.setFont(QFont("Yeon Sung", 25))
        credits.setStyleSheet("color : white;" "background : black;")
        credits.setStyleSheet(f"""
                QPushButton {{
                            background : none;
                            border: none;}}
                
                QPushButton:pressed {{
                                    background : white; 
                                    color: #000000; 
                                    font-weight: bold; 
                                    font-size : 18px; 
                                    border: none;
                                    border-radius: 10px;}}
                                    """)
                                    

        Exit = QPushButton("Exit", panelMainTitle)
        Exit.setGeometry(500, 460, 300, 40)
        id = QFontDatabase.addApplicationFont("YeonSung-Regular.ttf")
        Exit.setFont(QFont("Yeon Sung", 25))
        Exit.setStyleSheet(f"""
                QPushButton {{
                            background : none;
                            border: none;}}
                
                QPushButton:pressed {{
                                    background : white; 
                                    color: #000000; 
                                    font-weight: bold; 
                                    font-size : 18px; 
                                    border: none;
                                    border-radius: 10px;}}
                                    """)
        Exit.clicked.connect(self.exitGame)

        music = QPushButton("Play Music", panelMainTitle)
        music.setGeometry(930, 10, 300, 40)
        music.clicked.connect(play_music) 
        id = QFontDatabase.addApplicationFont("YeonSung-Regular.ttf")
        music.setFont(QFont("Yeon Sung", 15))
        music.setStyleSheet("color : white;" "background : black;")
        music.setStyleSheet(f"""
                QPushButton {{
                            background : none;
                            border: none;}}
                QPushButton:pressed {{
                                    background : white; 
                                    color: #000000; 
                                    font-weight: bold; 
                                    font-size : 18px; 
                                    border: none;
                                    border-radius: 10px;}}
                                    """)

    def exitGame(self):
        choice = QMessageBox.question(self, "Exit", "Êtes-vous sûrs de vouloir quitter ?",
                                      QMessageBox.Yes | QMessageBox.No)

        if choice == QMessageBox.Yes:
            sys.exit()
        else:
            pass


    # keyPressEvent est une fonction native a Qt elle permet de gérer les évènement
    def keyPressEvent(self, event):

        centralArea = centralWindow(self)

        gameScreenWindow = gameScreen(Stage.currentWorld, "stage {}".format(Stage.currentStage), centralArea )
        addPanelGoals(
            gameScreenWindow, 
            Stage.countMonster, 
            Stage.currentWorld, 
            "stage {}".format(Stage.currentStage), 
            Stage.countKey
        )

        createHeroPanel(gameScreenWindow, Hero.life)
        addShortcutInventoryLabel(gameScreenWindow)

        # j'appelle borderMap pour qu'elle soit connue de ma fonction keyPressEvent
        mapCell = drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.front)[1]
#===========================================================================================================================================================================================================
# GESTION DES MOUVEMENTS DU HERO AVEC LES FLECHES DU CLAVIER
#==========================================================================================================================================================================================================       
        
        # FLECHE DE DROITE
        if event.key() == 16777236:
            Hero.direction = "droite"
            if Stage.currentStage != 5 :
                if Hero.x <= 12:
                    if "[{}, {}]".format(Hero.y, Hero.x+1) in str(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["coordinate"]):
                        for i in Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["info"]:
                            if i["y"] == Hero.y and i["x"] == Hero.x+1:
                            # Voire les stats du monstre
                                createMonsterPanel(
                                    gameScreenWindow, 
                                    i["name"],
                                    i["life"],
                                    i["strength"], 
                                    i["defense"], 
                                    i["level"], 
                                    i["progressPV"],
                                    Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["face"],
                                
                                )
            
                                drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.right)
                                return

                    elif "[{}, {}]".format(Hero.y, Hero.x+1) in str(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)]["chest"]["coordinate"]):
                        Stage.messageTab.append("un coffre !")
                        addTextBox(gameScreenWindow)
                        drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.right)

                    elif  "[{}, {}]".format(Hero.y, Hero.x+1) in str(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)]["target"]["coordinate"]) and Stage.isOpen == False:
                        drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.right) 

                    elif  "[{}, {}]".format(Hero.y, Hero.x) in str(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)]["target"]["coordinate"]):
                        Stage.messageTab.append("vous avez terminer le stage {} de {}".format(Stage.currentStage, Stage.currentWorld))
                        addTextBox(gameScreenWindow)

                        Stage.currentStage = Stage.currentStage + 1
                        Hero.y = 1
                        Hero.x = 0
                        Stage.isOpen = False
                        Stage.countKey = 0
                        Stage.countMonster = 0

                        generateRandomCoordinate(Stage.currentWorld, "stage {}".format(Stage.currentStage))
                        gameScreen(Stage.currentWorld, "stage {}".format(Stage.currentStage),  centralArea)
                        Stage.messageTab.append("Hello Player")
                        addTextBox(gameScreenWindow)
                        createHeroPanel(gameScreenWindow, Hero.life)
                        addPanelGoals(
                            gameScreenWindow, 
                            Stage.countMonster, 
                            Stage.currentWorld, 
                            "stage {}".format(Stage.currentStage), 
                            Stage.countKey
                        )   

                    else:
                        Hero.x = Hero.x + 1 
                        drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.right)
            else: 

                if Hero.x <= 6 :
                    Hero.x = Hero.x + 1 
                    drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.right)  
               
                elif Hero.x == 6 and Hero.y == 1:

                    for i in Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)]["boss"]["info"]:
                        createMonsterPanel(
                            gameScreenWindow, 
                            i["name"],
                            i["life"],
                            i["strength"], 
                            i["defense"], 
                            i["level"], 
                            i["progressPV"],
                            Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "boss"]["face"],
                        )
                        drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.right)
                        
                if Stage.isDead == True:
                    if Hero.x <= 12 :
                        Hero.x = Hero.x + 1 
                        drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.right)

                    elif  "[{}, {}]".format(Hero.y, Hero.x) in str(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)]["target"]["coordinate"]):
                        print("vous avez terminer le stage {} de {}".format(Stage.currentStage, Stage.currentWorld))
                        
                        Stage.indexWorld = Stage.indexWorld + 1
                        Stage.currentWorld = Stage.worldArray[Stage.indexWorld]
                        Stage.currentStage = 1
                        Hero.y = 1
                        Hero.x = 0
                        Stage.isOpen = False
                        Stage.countKey = 0
                        Stage.countMonster = 0

                        generateRandomCoordinate(Stage.currentWorld, "stage {}".format(Stage.currentStage))
                        gameScreen(Stage.currentWorld, "stage {}".format(Stage.currentStage),  centralArea)
                        createHeroPanel(gameScreenWindow, Hero.life)
                        addPanelGoals(
                            gameScreenWindow, 
                            Stage.countMonster, 
                            Stage.currentWorld, 
                            "stage {}".format(Stage.currentStage), 
                            Stage.countKey
                        ) 


        # FLECHE DU HAUT
        elif event.key() == 16777235:
            Hero.direction = "haut"
            if Stage.currentStage < 5 :
                if Hero.y > 0:
                    if "[{}, {}]".format(Hero.y-1, Hero.x) in str(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["coordinate"]):
                        for i in Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["info"]:
                            if i["y"] == Hero.y-1 and i["x"] == Hero.x:
                                createMonsterPanel(
                                    gameScreenWindow, 
                                    i["name"],
                                    i["life"],
                                    i["strength"], 
                                    i["defense"], 
                                    i["level"], 
                                    i["progressPV"],
                                    Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["face"],
                                
                                )
                
                                drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.back)
                                return

                    elif "[{}, {}]".format(Hero.y-1, Hero.x) in str(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)]["chest"]["coordinate"]):
                        Stage.messageTab.append("un coffre !")
                        addTextBox(gameScreenWindow)
                        drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.back)

                    elif  "[{}, {}]".format(Hero.y-1, Hero.x) in str(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)]["target"]["coordinate"]) and Stage.isOpen == False:
                        drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.back)

                    elif  "[{}, {}]".format(Hero.y, Hero.x) in str(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)]["target"]["coordinate"]):
                        Stage.messageTab.append("vous avez terminer le stage {} de {}".format(Stage.currentStage, Stage.currentWorld))
                        addTextBox(gameScreenWindow)

                        if Stage.currentStage == 5:
                            Stage.indexWorld = Stage.indexWorld +1
                            Stage.currentStage = 1
                            Hero.y = 1
                            Hero.x = 0
                            Stage.isOpen = False
                            Stage.countKey = 0
                            Stage.countMonster = 0

                        generateRandomCoordinate(Stage.currentWorld, "stage {}".format(Stage.currentStage))
                        gameScreen(Stage.currentWorld, "stage {}".format(Stage.currentStage),  centralArea)
                        createHeroPanel(gameScreenWindow, Hero.life)
                        addPanelGoals(
                            gameScreenWindow, 
                            Stage.countMonster, 
                            Stage.currentWorld, 
                            "stage {}".format(Stage.currentStage), 
                            Stage.countKey
                        )

                    else:
                        Hero.y = Hero.y - 1
                        drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.back)
            else:
                if Hero.y > 1:
                    Hero.y = Hero.y - 1
                    drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.back)  

                else:
                    for i in Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)]["boss"]["info"]:
                        if Hero.x == 6 and Hero.y == 1:
                            createMonsterPanel(
                                gameScreenWindow, 
                                i["name"],
                                i["life"],
                                i["strength"], 
                                i["defense"], 
                                i["level"], 
                                i["progressPV"],
                                Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "boss"]["face"],
                            )
                            drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.back) 
                            return   
                    

        # FLECHE DU BAS
        elif event.key() == 16777237:
            Hero.direction = "bas"
            if Stage.currentStage < 5 :
                if Hero.y <= 3:
                    if "[{}, {}]".format(Hero.y+1, Hero.x) in str(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["coordinate"]):
                        for i in Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["info"]:
                                if i["y"] == Hero.y+1 and i["x"] == Hero.x:
                                    createMonsterPanel(
                                        gameScreenWindow, 
                                        i["name"],
                                        i["life"],
                                        i["strength"], 
                                        i["defense"], 
                                        i["level"], 
                                        i["progressPV"],
                                        Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["face"],
                                        
                                    )
                                    drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.front)   
                                    return

                    elif "[{}, {}]".format(Hero.y+1, Hero.x) in str(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)]["chest"]["coordinate"]):
                        Stage.messageTab.append("un coffre !")
                        addTextBox(gameScreenWindow)

                        drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.front)

                    elif  "[{}, {}]".format(Hero.y+1, Hero.x) in str(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)]["target"]["coordinate"]) and Stage.isOpen == False:
                        drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.front)  

                    elif  "[{}, {}]".format(Hero.y, Hero.x) in str(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)]["target"]["coordinate"]):
                        Stage.messageTab.append("vous avez terminer le stage {} de {}".format(Stage.currentStage, Stage.currentWorld)) 

                        addTextBox(gameScreenWindow)
                        if Stage.currentStage == 5:
                            Stage.indexWorld = Stage.indexWorld +1
                            Stage.currentStage = 1
                            Hero.y = 1
                            Hero.x = 0
                            Stage.isOpen = False
                            Stage.countKey = 0
                            Stage.countMonster = 0

                            generateRandomCoordinate(Stage.currentWorld, "stage {}".format(Stage.currentStage))
                            gameScreen(Stage.currentWorld, "stage {}".format(Stage.currentStage),  centralArea, "Hello player")
                            createHeroPanel(gameScreenWindow, Hero.life)
                            addPanelGoals(
                                gameScreenWindow, 
                                Stage.countMonster, 
                                Stage.currentWorld, 
                                "stage {}".format(Stage.currentStage), 
                                Stage.countKey
                            )
                        else:
                            Stage.currentStage = Stage.currentStage + 1
                            Hero.y = 1
                            Hero.x = 0
                            Stage.isOpen = False
                            Stage.countKey = 0
                            Stage.countMonster = 0

                            generateRandomCoordinate(Stage.currentWorld, "stage {}".format(Stage.currentStage))
                            gameScreen(Stage.currentWorld, "stage {}".format(Stage.currentStage),  centralArea)
                            createHeroPanel(gameScreenWindow, Hero.life)
                            addPanelGoals(
                                gameScreenWindow, 
                                Stage.countMonster, 
                                Stage.currentWorld, 
                                "stage {}".format(Stage.currentStage), 
                                Stage.countKey
                            ) 

                    else:
                        Hero.y = Hero.y + 1
                        drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.front)
            else :
                if Hero.y <= 1:
                    Hero.y = Hero.y + 1
                    for i in Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)]["boss"]["info"]:
                        if Hero.x == 6 and Hero.y == 1:
                            createMonsterPanel(
                                gameScreenWindow,
                                i["name"],
                                i["life"],
                                i["strength"], 
                                i["defense"], 
                                i["level"], 
                                i["progressPV"],
                                Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "boss"]["face"],
                            )
                            drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.front)
                            return
                else:
                    drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.front)    

        # FLACHE DE GAUCHE
        elif event.key() == 16777234:
            Hero.direction = "gauche"
            if Stage.currentStage < 5 :
                if Hero.x > 0:
                    if "[{}, {}]".format(Hero.y, Hero.x-1) in str(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["coordinate"]):
                        for i in Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["info"]:
                            if i["y"] == Hero.y and i["x"] == Hero.x-1:
                                createMonsterPanel(
                                    gameScreenWindow, 
                                    i["name"],
                                    i["life"],
                                    i["strength"], 
                                    i["defense"], 
                                    i["level"], 
                                    i["progressPV"],
                                    Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["face"],
                                
                                )
                
                                drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.left) 
                                return

                    elif "[{}, {}]".format(Hero.y, Hero.x-1) in str(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)]["chest"]["coordinate"]):
                        Stage.messageTab.append("un coffre !")
                        addTextBox(gameScreenWindow)

                        drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.left)

                    elif  "[{}, {}]".format(Hero.y, Hero.x-1) in str(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)]["target"]["coordinate"]) and Stage.isOpen == False:
                        drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.left)      

                    elif  "[{}, {}]".format(Hero.y, Hero.x) in str(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)]["target"]["coordinate"]):
                        Stage.messageTab.append("vous avez terminer le stage {} de {}".format(Stage.currentStage, Stage.currentWorld))
                        addTextBox(gameScreenWindow)

                        if Stage.currentStage == 5:
                            Stage.indexWorld = Stage.indexWorld +1
                            Stage.currentStage = 1
                            Hero.y = 1
                            Hero.x = 0
                            Stage.isOpen = False
                            Stage.countKey = 0
                            Stage.countMonster = 0

                            generateRandomCoordinate(Stage.currentWorld, "stage {}".format(Stage.currentStage))
                            gameScreen(Stage.currentWorld, "stage {}".format(Stage.currentStage),  centralArea, "Hello player")
                            createHeroPanel(gameScreenWindow, Hero.life)
                            addPanelGoals(
                                gameScreenWindow, 
                                Stage.countMonster, 
                                Stage.currentWorld, 
                                "stage {}".format(Stage.currentStage), 
                                Stage.countKey
                            )
                        else:
                            Stage.currentStage = Stage.currentStage + 1
                            Hero.y = 1
                            Hero.x = 0
                            Stage.isOpen = False
                            Stage.countKey = 0
                            Stage.countMonster = 0

                            generateRandomCoordinate(Stage.currentWorld, "stage {}".format(Stage.currentStage))
                            gameScreen(Stage.currentWorld, "stage {}".format(Stage.currentStage),  centralArea)
                            createHeroPanel(gameScreenWindow, Hero.life)
                            addPanelGoals(
                                gameScreenWindow, 
                                Stage.countMonster, 
                                Stage.currentWorld, 
                                "stage {}".format(Stage.currentStage), 
                                Stage.countKey
                            ) 

                    else:
                        Hero.x = Hero.x - 1
                        drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.left)
            else:
                if Hero.x > 0:
                    Hero.x = Hero.x - 1
                    drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.left)
                    for i in Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)]["boss"]["info"]:
                        if Hero.x == 6 and Hero.y == 1:
                            createMonsterPanel(
                                gameScreenWindow, 
                                i["name"],
                                i["life"],
                                i["strength"], 
                                i["defense"], 
                                i["level"], 
                                i["progressPV"],
                                Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "boss"]["face"],
                            )
                            drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.left)
                            return
                else:
                    drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.left)   
#===========================================================================================================================================================================================================
# GESTION DES INTERACTIONS DU HERO AVEC LA TOUCHE ENTRER
#=========================================================================================================================================================================================================

        # TOUCHE ENTRER
        elif event.key() == 16777220 :

#========================================================================================================================================================================================================
# GESTION DU SYSTEME DE COMBATS            
#========================================================================================================================================================================================================

            # EVENT SUR LA TOUCHE ENTRER
            if Stage.currentStage < 5:
                for i in Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["info"]:
            
                    # DROITE
                    if i["y"] == Hero.y and i["x"] == Hero.x+1:

                        if i["isAlive"] == True :

                            attack = int(Hero.strength/(i["defense"]/2)*Hero.level)
                            i["life"] = i["life"] - attack
                            i["progressPV"] =  i["progressPV"] - ((attack*100)/i["life"])
                                
                            createMonsterPanel(
                            gameScreenWindow, 
                                i["name"],
                                i["life"],
                                i["strength"], 
                                i["defense"], 
                                i["level"], 
                                i["progressPV"],
                                Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["face"],       
                            )

                            Stage.messageTab.append("vous attaquer le monstre et lui infliger au monstre {} de dégats".format(attack))
                            addTextBox(gameScreenWindow)

                            drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.right)

                            time.sleep(2)

                            attackBack = int(i['strength']/(Hero.defense/2)*i["level"])
                            Hero.life = Hero.life - attackBack
                            Hero.progressHeroPv = Hero.progressHeroPv - ((attackBack*100)/Hero.life)

                            createHeroPanel(gameScreenWindow, Hero.life)

                            Stage.messageTab.append("Le monstre vous attaque en retour et vous recevez {} de dégats".format(attackBack))
                            addTextBox(gameScreenWindow)
                                
                            if Hero.life <= 0:

                                Stage.messageTab.append("Vous succombez à vos blessures")
                                addTextBox(gameScreenWindow)
                            
                                Stage.indexWorld = 0
                                Stage.currentWorld = Stage.worldArray[Stage.indexWorld]
                                Stage.currentStage = 1 
                                Hero.y = 1
                                Hero.x = 0
                                Hero.level = 1
                                Hero.life = 100
                                Hero.maxlife = 100
                                Hero.progressHeroPv = 100
                                Hero.strength = 50
                                Hero.defense = 30
                                Hero.exp = 0
                                Hero.progressEXP = 0
                                Stage.isOpen = False
                                Stage.countKey = 0
                                Stage.countMonster = 0

                                generateRandomCoordinate(Stage.currentWorld, "stage {}".format(Stage.currentStage))
                                gameScreen(Stage.currentWorld, "stage {}".format(Stage.currentStage),  centralArea)
                                createHeroPanel(gameScreenWindow, Hero.life)
                                addPanelGoals(
                                    gameScreenWindow, 
                                    Stage.countMonster, 
                                    Stage.currentWorld, 
                                    "stage {}".format(Stage.currentStage), 
                                    Stage.countKey
                                )    

                            elif i["life"] <= 0 and i["isDroped"] == False:

                                i["life"] = 0
                                i["progressPV"] = 0
                                i["isAlive"] = False

                                Stage.countMonster = Stage.countMonster + 1

                                addPanelGoals(
                                    gameScreenWindow, 
                                    Stage.countMonster, 
                                    Stage.currentWorld, 
                                    "stage {}".format(Stage.currentStage), 
                                    Stage.countKey
                                )

                                exp = int((100/Hero.level)*Stage.currentStage)
                                Hero.progressEXP = Hero.progressEXP + exp
                                Stage.messageTab.append("bravos le monstre a été vaincu, vous avez gagner {} d'exp".format(exp))
                                addTextBox(gameScreenWindow)

                                if Hero.progressEXP == 100:
                                    Stage.messageTab.append("Félicitation vous montez au niveau {}".format(Hero.level + 1))
                                    addTextBox(gameScreenWindow)
                                    Hero.level = Hero.level +1
                                    Hero.life = Hero.life+15
                                    Hero.maxlife = Hero.maxlife+15
                                    Hero.strength = Hero.strength+15
                                    Hero.defense = Hero.defense+15
                                    Hero.progressEXP = 0
                                    Hero.life = Hero.maxlife
                                    Hero.progressHeroPv = 100

                                elif Hero.progressEXP > 100:
                                    Stage.messageTab.append("Félicitation vous montez au niveau {}".format(Hero.level + 1))
                                    addTextBox(gameScreenWindow)
                                    Hero.level = Hero.level +1
                                    Hero.life = Hero.life+15
                                    Hero.maxlife = Hero.maxlife+15
                                    Hero.strength = Hero.strength+15
                                    Hero.defense = Hero.defense+15
                                    reste = 100 - exp
                                    Hero.progressEXP = reste
                                    Hero.life = Hero.maxlife
                                    Hero.progressHeroPv = 100

                                createHeroPanel(gameScreenWindow, Hero.life)


                                
                                RAND = random.randint(0,len(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["drop"])-1)
                                
                                if RAND == 0:
                                    Stage.messageTab.append("aucun objet reçus !")
                                    addTextBox(gameScreenWindow)
                                else:
                                    
                                    Stage.inventaire.append(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["drop"][RAND])
                                    addInventory(gameScreenWindow)
                                    Stage.messageTab.append("{},reçus et ranger dans l'inventaire".format(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["drop"][RAND]))
                                    addTextBox(gameScreenWindow)
                                    Stage.saveDropItems.append(Stage.dropInfo["{}".format(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["drop"][RAND])]["image"])


                                i["isDroped"] = True
                                return
                                            
                        else:
                            Stage.messageTab.append("le monstre est mort")
                            addTextBox(gameScreenWindow)

                            drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.right)
                            i["isDroped"] = True
                            return                                                
                        return   
                        

                    # HAUT
                    elif i["y"] == Hero.y-1 and i["x"] == Hero.x:

                        if i["isAlive"] == True :

                            attack = int(Hero.strength/(i["defense"]/2)*Hero.level)
                            i["life"] = i["life"] - attack
                            i["progressPV"] =  i["progressPV"] - ((attack*100)/i["life"])    

                            createMonsterPanel(
                                gameScreenWindow, 
                                i["name"],
                                i["life"],
                                i["strength"], 
                                i["defense"], 
                                i["level"], 
                                i["progressPV"],
                                Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["face"],       
                            )

                            Stage.messageTab.append("vous attaquer le monstre et lui infliger au monstre {} de dégats".format(attack))
                            addTextBox(gameScreenWindow)

                            drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.back)

                            time.sleep(2)

                            attackBack = int(i['strength']/(Hero.defense/2)*i["level"])
                            Hero.life = Hero.life - attackBack
                            Hero.progressHeroPv = Hero.progressHeroPv - ((attackBack*100)/Hero.life)

                            createHeroPanel(gameScreenWindow, Hero.life)

                            Stage.messageTab.append("Le monstre vous attaque en retour et vous recevez {} de dégats".format(attackBack))
                            addTextBox(gameScreenWindow)

                            if Hero.life <= 0:

                                Stage.messageTab.append("Vous succombez à vos blessures")
                                addTextBox(gameScreenWindow)
                            
                                Stage.indexWorld = 0
                                Stage.currentWorld = Stage.worldArray[Stage.indexWorld]
                                Stage.currentStage = 1 
                                Hero.y = 1
                                Hero.x = 0
                                Hero.level = 1
                                Hero.life = 100
                                Hero.maxlife = 100
                                Hero.progressHeroPv = 100
                                Hero.strength = 50
                                Hero.defense = 30
                                Hero.exp = 0
                                Hero.progressEXP = 0
                                Stage.isOpen = False
                                Stage.countKey = 0
                                Stage.countMonster = 0

                                generateRandomCoordinate(Stage.currentWorld, "stage {}".format(Stage.currentStage))
                                gameScreen(Stage.currentWorld, "stage {}".format(Stage.currentStage),  centralArea)
                                createHeroPanel(gameScreenWindow, Hero.life)
                                addPanelGoals(
                                    gameScreenWindow, 
                                    Stage.countMonster, 
                                    Stage.currentWorld, 
                                    "stage {}".format(Stage.currentStage), 
                                    Stage.countKey
                                )

                            elif i["life"] <= 0 and i["isDroped"] == False:

                                i["life"] = 0
                                i["progressPV"] = 0
                                i["isAlive"] = False

                                Stage.countMonster = Stage.countMonster + 1

                                addPanelGoals(
                                    gameScreenWindow, 
                                    Stage.countMonster, 
                                    Stage.currentWorld, 
                                    "stage {}".format(Stage.currentStage), 
                                    Stage.countKey
                                )

                                exp = int((100/Hero.level)*Stage.currentStage)
                                Hero.progressEXP = Hero.progressEXP + exp
                                Stage.messageTab.append("bravos le monstre a été vaincu, vous avez gagner {} d'exp".format(exp))
                                addTextBox(gameScreenWindow)

                                if Hero.progressEXP == 100:
                                    Stage.messageTab.append("Félicitation vous montez au niveau {}".format(Hero.level + 1))
                                    addTextBox(gameScreenWindow)
                                    Hero.level = Hero.level +1
                                    Hero.life = Hero.life+15
                                    Hero.maxlife = Hero.maxlife+15
                                    Hero.strength = Hero.strength+15
                                    Hero.defense = Hero.defense+15
                                    Hero.progressEXP = 0
                                    Hero.life = Hero.maxlife
                                    Hero.progressHeroPv = 100

                                elif Hero.progressEXP > 100:
                                    Stage.messageTab.append("Félicitation vous montez au niveau {}".format(Hero.level + 1))
                                    addTextBox(gameScreenWindow)
                                    Hero.level = Hero.level +1
                                    Hero.life = Hero.life+15
                                    Hero.maxlife = Hero.maxlife+15
                                    Hero.strength = Hero.strength+15
                                    Hero.defense = Hero.defense+15
                                    reste = 100 - exp
                                    Hero.progressEXP = reste
                                    Hero.life = Hero.maxlife
                                    Hero.progressHeroPv = 100

                                createHeroPanel(gameScreenWindow, Hero.life)

                                RAND = random.randint(1,len(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["drop"])-1)
                                
                                if RAND == 0:
                                    Stage.messageTab.append("aucun objet reçus !")
                                    addTextBox(gameScreenWindow)
                                else:
                                    Stage.inventaire.append(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["drop"][RAND])
                                    addInventory(gameScreenWindow)
                                    Stage.messageTab.append("{}reçus et ranger dans l'inventaire".format(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["drop"][RAND]))
                                    addTextBox(gameScreenWindow)  
                                    Stage.saveDropItems.append(Stage.dropInfo["{}".format(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["drop"][RAND])]["image"])
                                drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.back) 
                                i["isDroped"] = True
                                return        
                        else:
                            Stage.messageTab.append("le monstre est mort")
                            addTextBox(gameScreenWindow)    
                            drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.back)               
                            return
                        return  
                    
            
                    # BAS
                    elif i["y"] == Hero.y+1 and i["x"] == Hero.x:

                        if i["isAlive"] == True :

                            attack = int(Hero.strength/(i["defense"]/2)*Hero.level)
                            i["life"] = i["life"] - attack
                            i["progressPV"] =  i["progressPV"] - ((attack*100)/i["life"])    

                            createMonsterPanel(
                                gameScreenWindow, 
                                i["name"],
                                i["life"],
                                i["strength"], 
                                i["defense"], 
                                i["level"], 
                                i["progressPV"],
                                Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["face"],
                            )
                            

                            Stage.messageTab.append("vous attaquer le monstre et lui infliger au monstre {} de dégats".format(attack))
                            addTextBox(gameScreenWindow)

                            drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.front)

                            time.sleep(2)

                            attackBack = int(i['strength']/(Hero.defense/2)*i["level"])
                            Hero.life = Hero.life - attackBack
                            Hero.progressHeroPv = Hero.progressHeroPv - ((attackBack*100)/Hero.life)

                            createHeroPanel(gameScreenWindow, Hero.life)

                            Stage.messageTab.append("Le monstre vous attaque en retour et vous recevez {} de dégats".format(attackBack))
                            addTextBox(gameScreenWindow)

                            if Hero.life <= 0:

                                Stage.messageTab.append("Vous succombez à vos blessures")
                                addTextBox(gameScreenWindow)
                            
                                Stage.indexWorld = 0
                                Stage.currentWorld = Stage.worldArray[Stage.indexWorld]
                                Stage.currentStage = 1 
                                Hero.y = 1
                                Hero.x = 0
                                Hero.level = 1
                                Hero.life = 100
                                Hero.maxlife = 100
                                Hero.progressHeroPv = 100
                                Hero.strength = 50
                                Hero.defense = 30
                                Hero.exp = 0
                                Hero.progressEXP = 0
                                Stage.isOpen = False
                                Stage.countKey = 0
                                Stage.countMonster = 0

                                generateRandomCoordinate(Stage.currentWorld, "stage {}".format(Stage.currentStage))
                                gameScreen(Stage.currentWorld, "stage {}".format(Stage.currentStage),  centralArea)
                                createHeroPanel(gameScreenWindow, Hero.life)
                                addPanelGoals(
                                    gameScreenWindow, 
                                    Stage.countMonster, 
                                    Stage.currentWorld, 
                                    "stage {}".format(Stage.currentStage), 
                                    Stage.countKey
                                )

                            elif i["life"] <= 0 and i["isDroped"] == False:

                                i["life"] = 0
                                i["progressPV"] = 0
                                i["isAlive"] = False

                                Stage.countMonster = Stage.countMonster + 1

                                addPanelGoals(
                                    gameScreenWindow, 
                                    Stage.countMonster, 
                                    Stage.currentWorld, 
                                    "stage {}".format(Stage.currentStage), 
                                    Stage.countKey
                                )

                                exp = int((100/Hero.level)*Stage.currentStage)
                                Hero.progressEXP = Hero.progressEXP + exp
                                Stage.messageTab.append("bravos le monstre a été vaincu, vous avez gagner {} d'exp".format(exp))
                                addTextBox(gameScreenWindow)

                                if Hero.progressEXP == 100:
                                    Stage.messageTab.append("Félicitation vous montez au niveau {}".format(Hero.level + 1))
                                    addTextBox(gameScreenWindow)
                                    Hero.level = Hero.level +1
                                    Hero.life = Hero.life+15
                                    Hero.maxlife = Hero.maxlife+15
                                    Hero.strength = Hero.strength+15
                                    Hero.defense = Hero.defense+15
                                    Hero.progressEXP = 0
                                    Hero.life = Hero.maxlife
                                    Hero.progressHeroPv = 100

                                elif Hero.progressEXP > 100:
                                    Stage.messageTab.append("Félicitation vous montez au niveau {}".format(Hero.level + 1))
                                    addTextBox(gameScreenWindow)
                                    Hero.level = Hero.level +1
                                    Hero.life = Hero.life+15
                                    Hero.maxlife = Hero.maxlife+15
                                    Hero.strength = Hero.strength+15
                                    Hero.defense = Hero.defense+15
                                    reste = 100 - exp
                                    Hero.progressEXP = reste
                                    Hero.life = Hero.maxlife
                                    Hero.progressHeroPv = 100

                                createHeroPanel(gameScreenWindow, Hero.life)

                                RAND = random.randint(0,len(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["drop"])-1)
                                
                                
                                if RAND == 0:
                                    Stage.messageTab.append("aucun objet reçus !")
                                    addTextBox(gameScreenWindow)
                                else:
                                    Stage.inventaire.append(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["drop"][RAND])
                                    addInventory(gameScreenWindow)
                                    Stage.messageTab.append("{}reçus et ranger dans l'inventaire".format(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["drop"][RAND]))
                                    addTextBox(gameScreenWindow)  
                                    Stage.saveDropItems.append(Stage.dropInfo["{}".format(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["drop"][RAND])]["image"])
                               
                                i["isDroped"] = True
                                return

                        else:
                            Stage.messageTab.append("Le monstre est mort")
                            addTextBox(gameScreenWindow)
                            drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.front)               
                            return
                        return
                    # GAUCHE
                    elif i["y"] == Hero.y and i["x"] == Hero.x-1:
                
                        if i["isAlive"] == True :

                            attack = int(Hero.strength/(i["defense"]/2)*Hero.level)
                            i["life"] = i["life"] - attack
                            i["progressPV"] =  i["progressPV"] - ((attack*100)/i["life"])    

                            createMonsterPanel(
                                gameScreenWindow, 
                                i["name"],
                                i["life"],
                                i["strength"], 
                                i["defense"], 
                                i["level"], 
                                i["progressPV"],
                                Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["face"],
                            )

                            Stage.messageTab.append("vous attaquer le monstre et lui infliger au monstre {} de dégats".format(attack))
                            addTextBox(gameScreenWindow)

                            drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.left)

                            time.sleep(2)

                            attackBack = int(i['strength']/(Hero.defense/2)*i["level"])
                            Hero.life = Hero.life - attackBack
                            Hero.progressHeroPv = Hero.progressHeroPv - ((attackBack*100)/Hero.life)

                            createHeroPanel(gameScreenWindow, Hero.life)

                            Stage.messageTab.append("Le monstre vous attaque en retour et vous recevez {} de dégats".format(attackBack))
                            addTextBox(gameScreenWindow)

                            if Hero.life <= 0:

                                Stage.messageTab.append("Vous succombez à vos blessures")
                                addTextBox(gameScreenWindow)
                            
                                Stage.indexWorld = 0
                                Stage.currentWorld = Stage.worldArray[Stage.indexWorld]
                                Stage.currentStage = 1 
                                Hero.y = 1
                                Hero.x = 0
                                Hero.level = 1
                                Hero.life = 100
                                Hero.maxlife = 100
                                Hero.progressHeroPv = 100
                                Hero.strength = 50
                                Hero.defense = 30
                                Hero.exp = 0
                                Hero.progressEXP = 0
                                Stage.isOpen = False
                                Stage.countKey = 0
                                Stage.countMonster = 0

                                generateRandomCoordinate(Stage.currentWorld, "stage {}".format(Stage.currentStage))
                                gameScreen(Stage.currentWorld, "stage {}".format(Stage.currentStage),  centralArea)
                                createHeroPanel(gameScreenWindow, Hero.life)
                                addPanelGoals(
                                    gameScreenWindow, 
                                    Stage.countMonster, 
                                    Stage.currentWorld, 
                                    "stage {}".format(Stage.currentStage), 
                                    Stage.countKey
                                )

                            elif i["life"] <= 0 and i["isDroped"] == False:

                                i["life"] = 0
                                i["progressPV"] = 0
                                i["isAlive"] = False

                                Stage.countMonster = Stage.countMonster + 1

                                addPanelGoals(
                                    gameScreenWindow, 
                                    Stage.countMonster, 
                                    Stage.currentWorld, 
                                    "stage {}".format(Stage.currentStage), 
                                    Stage.countKey
                                )
                                
                                exp = int((100/Hero.level)*Stage.currentStage)
                                Hero.progressEXP = Hero.progressEXP + exp
                                Stage.messageTab.append("bravos le monstre a été vaincu, vous avez gagner {} d'exp".format(exp))
                                addTextBox(gameScreenWindow)
                                
                                if Hero.progressEXP == 100:
                                    Stage.messageTab.append("Félicitation vous montez au niveau {}".format(Hero.level + 1))
                                    addTextBox(gameScreenWindow)
                                    Hero.level = Hero.level +1
                                    Hero.life = Hero.life+15
                                    Hero.maxlife = Hero.maxlife+15
                                    Hero.strength = Hero.strength+15
                                    Hero.defense = Hero.defense+15
                                    Hero.progressEXP = 0
                                    Hero.life = Hero.maxlife
                                    Hero.progressHeroPv = 100

                                elif Hero.progressEXP > 100:
                                    Stage.messageTab.append("Félicitation vous montez au niveau {}".format(Hero.level + 1))
                                    addTextBox(gameScreenWindow)
                                    Hero.level = Hero.level +1
                                    Hero.life = Hero.life+15
                                    Hero.maxlife = Hero.maxlife+15
                                    Hero.strength = Hero.strength+15
                                    Hero.defense = Hero.defense+15
                                    reste = 100 - exp
                                    Hero.progressEXP = reste
                                    Hero.life = Hero.maxlife
                                    Hero.progressHeroPv = 100

                                createHeroPanel(gameScreenWindow, Hero.life)

                                RAND = random.randint(0,len(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["drop"])-1)
                                
                                if RAND == 0:
                                    Stage.messageTab.append("aucun objet reçus !")
                                    addTextBox(gameScreenWindow)
                                else:
                                    Stage.inventaire.append(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["drop"][RAND])
                                    addInventory(gameScreenWindow)
                                    Stage.messageTab.append("{}reçus et ranger dans l'inventaire".format(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["drop"][RAND]))
                                    addTextBox(gameScreenWindow)   
                                    Stage.saveDropItems.append(Stage.dropInfo["{}".format(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["drop"][RAND])]["image"])

                                i["isDroped"] == True
                                return

                        else:
                            Stage.messageTab.append("Le monstre est mort")
                            addTextBox(gameScreenWindow)        
                            drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.left)               
                            return
                        return    

#==================================================================================================================================================================
# GESTION DU SYSTEME DE COMBAT CONTRE LE BOSS
# ================================================================================================================================================================                   
            else:
                
                if Hero.x == 6 and Hero.direction == "haut":

                    for i in Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)]["boss"]["info"]:
                        

                        if i["isAlive"] == True :

                            attack = int(Hero.strength/(i["defense"]/2)*Hero.level)
                            i["life"] = i["life"] - attack
                            i["progressPV"] =  i["progressPV"] - ((attack*100)/i["life"])
                            print(attack)

                            createMonsterPanel(
                            gameScreenWindow, 
                                i["name"],
                                i["life"],
                                i["strength"], 
                                i["defense"], 
                                i["level"], 
                                i["progressPV"],
                                Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "boss"]["face"],       
                            )

                            Stage.messageTab.append("vous attaquer le monstre et lui infliger au monstre {} de dégats".format(attack))
                            addTextBox(gameScreenWindow)

                            drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.back)

                            time.sleep(2)

                            attackBack = int(i['strength']/(Hero.defense/2)*i["level"])
                            Hero.life = Hero.life - attackBack
                            Hero.progressHeroPv = Hero.progressHeroPv - ((attackBack*100)/Hero.life)

                            createHeroPanel(gameScreenWindow, Hero.life)

                            Stage.messageTab.append("Le monstre vous attaque en retour et vous recevez {} de dégats".format(attackBack))
                            addTextBox(gameScreenWindow)

                            if Hero.life <= 0:

                                Stage.messageTab.append("Vous succombez à vos blessures")
                                addTextBox(gameScreenWindow)
                            
                                Stage.indexWorld = 0
                                Stage.currentWorld = Stage.worldArray[Stage.indexWorld]
                                Stage.currentStage = 1 
                                Hero.y = 1
                                Hero.x = 0
                                Hero.level = 1
                                Hero.life = 100
                                Hero.maxlife = 100
                                Hero.progressHeroPv = 100
                                Hero.strength = 50
                                Hero.defense = 30
                                Hero.exp = 0
                                Hero.progressEXP = 0
                                Stage.isOpen = False
                                Stage.countKey = 0
                                Stage.countMonster = 0

                                generateRandomCoordinate(Stage.currentWorld, "stage {}".format(Stage.currentStage))
                                gameScreen(Stage.currentWorld, "stage {}".format(Stage.currentStage),  centralArea)
                                createHeroPanel(gameScreenWindow, Hero.life)
                                addPanelGoals(
                                    gameScreenWindow, 
                                    Stage.countMonster, 
                                    Stage.currentWorld, 
                                    "stage {}".format(Stage.currentStage), 
                                    Stage.countKey
                                )

                            elif i["life"] <= 0 and i["isDroped"] == False:
                                
                                i["life"] = 0
                                i["progressPV"] = 0
                                i["isAlive"] = False
                                Stage.isDead = True

                                Stage.countMonster = Stage.countMonster + 1

                                addPanelGoals(
                                    gameScreenWindow, 
                                    Stage.countMonster, 
                                    Stage.currentWorld, 
                                    "stage {}".format(Stage.currentStage), 
                                    Stage.countKey
                                )

                                exp = int((100/Hero.level)*Stage.currentStage)
                                Hero.progressEXP = Hero.progressEXP + exp

                                if Hero.progressEXP == 100:
                                    Hero.level = Hero.level +1
                                    Hero.life = Hero.life+5
                                    Hero.maxlife = Hero.maxlife+5
                                    Hero.strength = Hero.strength+5
                                    Hero.defense = Hero.defense+5
                                    Hero.progressEXP = 0

                                elif Hero.progressEXP > 100:
                                    Hero.level = Hero.level +1
                                    Hero.life = Hero.life+5
                                    Hero.maxlife = Hero.maxlife+5
                                    Hero.strength = Hero.strength+5
                                    Hero.defense = Hero.defense+5
                                    reste = Hero.progressEXP - exp
                                    Hero.progressEXP = reste


                                createHeroPanel(gameScreenWindow, Hero.life)

                                Stage.messageTab.append("bravos le monstre a été vaincu, vous avez gagner {} d'exp".format(exp))
                                Stage.isOpen = True
                                addTextBox(gameScreenWindow)

                                
                                RAND = 0
                                
                                Stage.messageTab.append("{},reçus et ranger dans l'inventaire".format(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "boss"]["drop"][RAND]))
                                addTextBox(gameScreenWindow)
                                # Stage.saveDropItems.append(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "boss"])
                                # addInventory(gameScreenWindow)

                                i["isDroped"] = True
                                return
                        
                        else:
                            Stage.messageTab.append("le monstre est mort")
                            addTextBox(gameScreenWindow)
                            drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.back)
                            return
                        return
#=========================================================================================================================================================================================================
# GESTION DES INTERACTIONS AVEC LE COFFRE SUR LA MAP
#==========================================================================================================================================================================================================
            
            # EVENT SUR LA TOUCHE ENTRER
            for k in Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)]["chest"]["coordinate"]:

                # DROITE
                if k[0] == Hero.y and k[1] == Hero.x+1:

                    drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.right)

                    if Stage.countMonster == len(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["coordinate"]):

                        if Stage.dropInfo["clée du donjon"]["image"] in str(Stage.saveDropItems):
                            Stage.messageTab.append("vous avez déja la clée")
                            addTextBox(gameScreenWindow)
                        else:    
                            Stage.messageTab.append("{},reçus et ranger dans l'inventaire".format(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)]["chest"]["drop"][0]))
                            addTextBox(gameScreenWindow)
                            Stage.saveDropItems.append(Stage.dropInfo["{}".format(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)]["chest"]["drop"][0])]["image"])
                            addInventory(gameScreenWindow)

                            Stage.countKey = Stage.countKey +1

                            addPanelGoals(
                                gameScreenWindow, 
                                Stage.countMonster, 
                                Stage.currentWorld, 
                                "stage {}".format(Stage.currentStage), 
                                Stage.countKey
                            ) 


                    else:
                        Stage.messageTab.append("il reste des monstre a tuer")
                        addTextBox(gameScreenWindow)

                # HAUT    
                elif k[0] == Hero.y-1 and k[1] == Hero.x:

                    drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.back)

                    if Stage.countMonster == len(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["coordinate"]):

                        if Stage.dropInfo["clée du donjon"]["image"] in str(Stage.saveDropItems):
                            Stage.messageTab.append("vous avez déja la clée")
                            addTextBox(gameScreenWindow)
                        else:    
                            Stage.messageTab.append("{},reçus et ranger dans l'inventaire".format(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)]["chest"]["drop"][0]))
                            addTextBox(gameScreenWindow)
                            Stage.saveDropItems.append(Stage.dropInfo["{}".format(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)]["chest"]["drop"][0])]["image"])
                            addInventory(gameScreenWindow)

                            Stage.countKey = Stage.countKey +1

                            addPanelGoals(
                                gameScreenWindow, 
                                Stage.countMonster, 
                                Stage.currentWorld, 
                                "stage {}".format(Stage.currentStage), 
                                Stage.countKey
                            ) 
                    else:
                        Stage.messageTab.append("il reste des monstre a tuer")
                        addTextBox(gameScreenWindow) 

                # BAS 
                elif k[0] == Hero.y+1 and k[1] == Hero.x:

                    drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.front)
                    if Stage.countMonster == len(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["coordinate"]):

                        if Stage.dropInfo["clée du donjon"]["image"] in str(Stage.saveDropItems):
                            Stage.messageTab.append("vous avez déja la clée")
                        else:    
                            Stage.messageTab.append("{},reçus et ranger dans l'inventaire".format(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)]["chest"]["drop"][0]))
                            addTextBox(gameScreenWindow) 
                            Stage.saveDropItems.append(Stage.dropInfo["{}".format(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)]["chest"]["drop"][0])]["image"])
                            addInventory(gameScreenWindow)

                            Stage.countKey = Stage.countKey +1

                            addPanelGoals(
                                gameScreenWindow, 
                                Stage.countMonster, 
                                Stage.currentWorld, 
                                "stage {}".format(Stage.currentStage), 
                                Stage.countKey
                            ) 
                    else:
                        Stage.messageTab.append("il reste des monstre a tuer")
                        addTextBox(gameScreenWindow) 

                # GAUCHE    
                elif k[0] == Hero.y and k[1] == Hero.x-1:

                    drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.left)

                    if Stage.countMonster == len(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["coordinate"]):

                        if Stage.dropInfo["clée du donjon"]["image"] in str(Stage.saveDropItems):
                            Stage.messageTab.append("vous avez déja la clée")
                            addTextBox(gameScreenWindow)
                        else:    
                            Stage.messageTab.append("{},reçus et ranger dans l'inventaire".format(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)]["chest"]["drop"][0]))
                            addTextBox(gameScreenWindow)
                            Stage.saveDropItems.append(Stage.dropInfo["{}".format(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)]["chest"]["drop"][0])]["image"])
                            addInventory(gameScreenWindow)

                            Stage.countKey = Stage.countKey +1

                            addPanelGoals(
                                gameScreenWindow, 
                                Stage.countMonster, 
                                Stage.currentWorld, 
                                "stage {}".format(Stage.currentStage), 
                                Stage.countKey
                            ) 
                    else:
                        Stage.messageTab.append("il reste des monstre a tuer")
                        addTextBox(gameScreenWindow) 

#========================================================================================================================================================================================================= 
# GESTION DES INTERACTIONS AVEC LA CASE D ARRIVEE SUR LA MAP           
#=========================================================================================================================================================================================================

            # EVENT SUR LA TOUCHE ENTRER
            
            #  DROITE            
            if "[{}, {}]".format(Hero.y, Hero.x+1) in str(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)]["target"]["coordinate"]):

                if (Stage.countMonster == len(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["coordinate"]) 
                    and Stage.countKey == len(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "chest"]["coordinate"])
                    ):
                    Stage.isOpen = True
                    Stage.messageTab.append("vous avez utiliser la clée pour sortir du portail")
                    addTextBox(gameScreenWindow)
                    Stage.saveDropItems.remove(Stage.dropInfo["clée du donjon"]["image"])
                    addInventory(gameScreenWindow)
                    drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.right)
                else:
                    Stage.messageTab.append("Vous n'avez pas remplie toute les conditions")
                    addTextBox(gameScreenWindow)    
                    

            # HAUT
            if "[{}, {}]".format(Hero.y-1, Hero.x) in str(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)]["target"]["coordinate"]):

                if (Stage.countMonster == len(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["coordinate"]) 
                    and Stage.countKey == len(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "chest"]["coordinate"])
                    ):
                    Stage.isOpen = True
                    Stage.messageTab.append("vous avez utiliser la clée pour sortir du portail")
                    Stage.saveDropItems.remove(Stage.dropInfo["clée du donjon"]["image"])
                    addInventory(gameScreenWindow)
                    drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.back)
                else:
                    Stage.messageTab.append("Vous n'avez pas remplie toute les conditions")
                    addTextBox(gameScreenWindow)     

            # BAS
            if "[{}, {}]".format(Hero.y+1, Hero.x) in str(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)]["target"]["coordinate"]):

                if (Stage.countMonster == len(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["coordinate"]) 
                    and Stage.countKey == len(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "chest"]["coordinate"])
                    ):
                    Stage.isOpen = True
                    Stage.messageTab.append("vous avez utiliser la clée pour sortir du portail")
                    addTextBox(gameScreenWindow)
                    Stage.saveDropItems.remove(Stage.dropInfo["clée du donjon"]["image"])
                    addInventory(gameScreenWindow)
                    drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.front)
                else:
                    Stage.messageTab.append("Vous n'avez pas remplie toute les conditions")
                    addTextBox(gameScreenWindow)     
                

            # GAUCHE 
            if "[{}, {}]".format(Hero.y, Hero.x-1) in str(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)]["target"]["coordinate"]):

                if (Stage.countMonster == len(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "monsters"]["coordinate"]) 
                    and Stage.countKey == len(Stage.world[Stage.currentWorld]["stages"]["stage {}".format(Stage.currentStage)][ "chest"]["coordinate"])
                    ):
                    Stage.isOpen = True
                    Stage.messageTab.append("vous avez utiliser la clée pour sortir du portail")
                    addTextBox(gameScreenWindow)
                    Stage.saveDropItems.remove(Stage.dropInfo["clée du donjon"]["image"])
                    addInventory(gameScreenWindow)
                    drawGameMap(Stage.currentWorld, "stage {}".format(Stage.currentStage), gameScreenWindow, Hero.front)
                else:
                    Stage.messageTab.append("Vous n'avez pas remplie toute les conditions")
                    addTextBox(gameScreenWindow)     
                     
#=================================================================================================================================================================
# GESTION DE L'INVENTAIRE
# ================================================================================================================================================================
        
        #A
        elif event.key() == 65:
            
            if Stage.inventaire[0] == "petite potion de hp":
                effect = Stage.dropInfo[Stage.inventaire[0]]["effect"]
                if Hero.life < Hero.maxlife:
                    hpNeedToRestore = Hero.maxlife - Hero.life
                    if hpNeedToRestore >= 50:
                        Hero.life = Hero.life + effect
                        Hero.progressHeroPv = Hero.progressHeroPv + ((effect*100)/ Hero.maxlife)
                        createHeroPanel(gameScreenWindow, Hero.life)
                        Stage.inventaire.remove(Stage.inventaire[0])
                        Stage.saveDropItems.remove(Stage.dropInfo["petite potion de hp"]["image"])
                        addInventory(gameScreenWindow)
                        Stage.messageTab.append(" vous avez utiliser une petite potion de hp")
                        addTextBox(gameScreenWindow)
                    else:
                        Hero.life = Hero.life + hpNeedToRestore
                        Hero.progressHeroPv = Hero.progressHeroPv + ((hpNeedToRestore*100)/ Hero.maxlife)
                        createHeroPanel(gameScreenWindow, Hero.life)
                        Stage.inventaire.remove(Stage.inventaire[0])
                        Stage.saveDropItems.remove(Stage.dropInfo["petite potion de hp"]["image"])
                        addInventory(gameScreenWindow)
                        Stage.messageTab.append(" vous avez utiliser une petite potion de hp")
                        addTextBox(gameScreenWindow)    
                else:
                    Stage.messageTab.append(" Vos points de vie sont déjas au maximum")
                    addTextBox(gameScreenWindow) 

            elif Stage.inventaire[0] == "petit bouclier":
                effect = Stage.dropInfo[Stage.inventaire[0]]["effect"]
                Hero.defense = Hero.defense + effect
                createHeroPanel(gameScreenWindow, Hero.life)          
                Stage.inventaire.remove(Stage.inventaire[0])
                Stage.saveDropItems.remove(Stage.dropInfo["petit bouclier"]["image"])
                addInventory(gameScreenWindow)
                Stage.messageTab.append(" vous avez utiliser petite bouclier, votre défense augmante de 20")
                addTextBox(gameScreenWindow)
            else:
                Stage.messageTab.append("Cette emplacement est vide")
                addTextBox(gameScreenWindow)
            
        #z
        elif event.key() == 90:

            if Stage.inventaire[1] == "petite potion de hp":
                effect = Stage.dropInfo[Stage.inventaire[1]]["effect"]
                if Hero.life < Hero.maxlife:
                    hpNeedToRestore = Hero.maxlife - Hero.life
                    if hpNeedToRestore >= 50:
                        Hero.life = Hero.life + effect
                        Hero.progressHeroPv = Hero.progressHeroPv + ((effect*100)/ Hero.maxlife)
                        createHeroPanel(gameScreenWindow, Hero.life)
                        Stage.inventaire.remove(Stage.inventaire[1])
                        Stage.saveDropItems.remove(Stage.dropInfo["petite potion de hp"]["image"])
                        addInventory(gameScreenWindow)
                        Stage.messageTab.append(" vous avez utiliser une petite potion de hp")
                        addTextBox(gameScreenWindow)
                    else:
                        Hero.life = Hero.life + hpNeedToRestore
                        Hero.progressHeroPv = Hero.progressHeroPv + ((hpNeedToRestore*100)/ Hero.maxlife)
                        createHeroPanel(gameScreenWindow, Hero.life)
                        Stage.inventaire.remove(Stage.inventaire[1])
                        Stage.saveDropItems.remove(Stage.dropInfo["petite potion de hp"]["image"])
                        addInventory(gameScreenWindow)
                        Stage.messageTab.append(" vous avez utiliser une petite potion de hp")
                        addTextBox(gameScreenWindow)    
                else:
                    Stage.messageTab.append(" Vos points de vie sont déjas au maximum")
                    addTextBox(gameScreenWindow) 

            elif Stage.inventaire[1] == "petit bouclier":
                effect = Stage.dropInfo[Stage.inventaire[1]]["effect"]
                Hero.defense = Hero.defense + effect
                createHeroPanel(gameScreenWindow, Hero.life)          
                Stage.inventaire.remove(Stage.inventaire[1])
                Stage.saveDropItems.remove(Stage.dropInfo["petit bouclier"]["image"])
                addInventory(gameScreenWindow)
                Stage.messageTab.append(" vous avez utiliser petite bouclier, votre défense augmante de 20")
                addTextBox(gameScreenWindow)
            else:
                Stage.messageTab.append("Cette emplacement est vide")
                addTextBox(gameScreenWindow)
        
        #E
        elif event.key() == 69:

            if Stage.inventaire[2] == "petite potion de hp":
                effect = Stage.dropInfo[Stage.inventaire[2]]["effect"]
                if Hero.life < Hero.maxlife:
                    hpNeedToRestore = Hero.maxlife - Hero.life
                    if hpNeedToRestore >= 50:
                        Hero.life = Hero.life + effect
                        Hero.progressHeroPv = Hero.progressHeroPv + ((effect*100)/ Hero.maxlife)
                        createHeroPanel(gameScreenWindow, Hero.life)
                        Stage.inventaire.remove(Stage.inventaire[2])
                        Stage.saveDropItems.remove(Stage.dropInfo["petite potion de hp"]["image"])
                        addInventory(gameScreenWindow)
                        Stage.messageTab.append(" vous avez utiliser une petite potion de hp")
                        addTextBox(gameScreenWindow)
                    else:
                        Hero.life = Hero.life + hpNeedToRestore
                        Hero.progressHeroPv = Hero.progressHeroPv + ((hpNeedToRestore*100)/ Hero.maxlife)
                        createHeroPanel(gameScreenWindow, Hero.life)
                        Stage.inventaire.remove(Stage.inventaire[2])
                        Stage.saveDropItems.remove(Stage.dropInfo["petite potion de hp"]["image"])
                        addInventory(gameScreenWindow)
                        Stage.messageTab.append(" vous avez utiliser une petite potion de hp")
                        addTextBox(gameScreenWindow)    
                else:
                    Stage.messageTab.append(" Vos points de vie sont déjas au maximum")
                    addTextBox(gameScreenWindow) 

            elif Stage.inventaire[2] == "petit bouclier":
                effect = Stage.dropInfo[Stage.inventaire[2]]["effect"]
                Hero.defense = Hero.defense + effect
                createHeroPanel(gameScreenWindow, Hero.life)          
                Stage.inventaire.remove(Stage.inventaire[2])
                Stage.saveDropItems.remove(Stage.dropInfo["petit bouclier"]["image"])
                addInventory(gameScreenWindow)
                Stage.messageTab.append(" vous avez utiliser petite bouclier, votre défense augmante de 20")
                addTextBox(gameScreenWindow)
            else:
                Stage.messageTab.append("Cette emplacement est vide")
                addTextBox(gameScreenWindow)
        #R
        elif event.key() == 82:

            if Stage.inventaire[3] == "petite potion de hp":
                effect = Stage.dropInfo[Stage.inventaire[3]]["effect"]
                if Hero.life < Hero.maxlife:
                    hpNeedToRestore = Hero.maxlife - Hero.life
                    if hpNeedToRestore >= 50:
                        Hero.life = Hero.life + effect
                        Hero.progressHeroPv = Hero.progressHeroPv + ((effect*100)/ Hero.maxlife)
                        createHeroPanel(gameScreenWindow, Hero.life)
                        Stage.inventaire.remove(Stage.inventaire[3])
                        Stage.saveDropItems.remove(Stage.dropInfo["petite potion de hp"]["image"])
                        addInventory(gameScreenWindow)
                        Stage.messageTab.append(" vous avez utiliser une petite potion de hp")
                        addTextBox(gameScreenWindow)
                    else:
                        Hero.life = Hero.life + hpNeedToRestore
                        Hero.progressHeroPv = Hero.progressHeroPv + ((hpNeedToRestore*100)/ Hero.maxlife)
                        createHeroPanel(gameScreenWindow, Hero.life)
                        Stage.inventaire.remove(Stage.inventaire[3])
                        Stage.saveDropItems.remove(Stage.dropInfo["petite potion de hp"]["image"])
                        addInventory(gameScreenWindow)
                        Stage.messageTab.append(" vous avez utiliser une petite potion de hp")
                        addTextBox(gameScreenWindow)    
                else:
                    Stage.messageTab.append(" Vos points de vie sont déjas au maximum")
                    addTextBox(gameScreenWindow) 

            elif Stage.inventaire[3] == "petit bouclier":
                effect = Stage.dropInfo[Stage.inventaire[3]]["effect"]
                Hero.defense = Hero.defense + effect
                createHeroPanel(gameScreenWindow, Hero.life)          
                Stage.inventaire.remove(Stage.inventaire[3])
                Stage.saveDropItems.remove(Stage.dropInfo["petit bouclier"]["image"])
                addInventory(gameScreenWindow)
                Stage.messageTab.append(" vous avez utiliser petite bouclier, votre défense augmante de 20")
                addTextBox(gameScreenWindow)
            else:
                Stage.messageTab.append("Cette emplacement est vide")
                addTextBox(gameScreenWindow)
        
        #T
        elif event.key() == 84:

            if Stage.inventaire[4] == "petite potion de hp":
                effect = Stage.dropInfo[Stage.inventaire[4]]["effect"]
                if Hero.life < Hero.maxlife:
                    hpNeedToRestore = Hero.maxlife - Hero.life
                    if hpNeedToRestore >= 50:
                        Hero.life = Hero.life + effect
                        Hero.progressHeroPv = Hero.progressHeroPv + ((effect*100)/ Hero.maxlife)
                        createHeroPanel(gameScreenWindow, Hero.life)
                        Stage.inventaire.remove(Stage.inventaire[4])
                        Stage.saveDropItems.remove(Stage.dropInfo["petite potion de hp"]["image"])
                        addInventory(gameScreenWindow)
                        Stage.messageTab.append(" vous avez utiliser une petite potion de hp")
                        addTextBox(gameScreenWindow)
                    else:
                        Hero.life = Hero.life + hpNeedToRestore
                        Hero.progressHeroPv = Hero.progressHeroPv + ((hpNeedToRestore*100)/ Hero.maxlife)
                        createHeroPanel(gameScreenWindow, Hero.life)
                        Stage.inventaire.remove(Stage.inventaire[4])
                        Stage.saveDropItems.remove(Stage.dropInfo["petite potion de hp"]["image"])
                        addInventory(gameScreenWindow)
                        Stage.messageTab.append(" vous avez utiliser une petite potion de hp")
                        addTextBox(gameScreenWindow)    
                else:
                    Stage.messageTab.append(" Vos points de vie sont déjas au maximum")
                    addTextBox(gameScreenWindow) 

            elif Stage.inventaire[4] == "petit bouclier":
                effect = Stage.dropInfo[Stage.inventaire[4]]["effect"]
                Hero.defense = Hero.defense + effect
                createHeroPanel(gameScreenWindow, Hero.life)          
                Stage.inventaire.remove(Stage.inventaire[4])
                Stage.saveDropItems.remove(Stage.dropInfo["petit bouclier"]["image"])
                addInventory(gameScreenWindow)
                Stage.messageTab.append(" vous avez utiliser petite bouclier, votre défense augmante de 20")
                addTextBox(gameScreenWindow)
            else:
                Stage.messageTab.append("Cette emplacement est vide")
                addTextBox(gameScreenWindow)
        
        #Y
        elif event.key() == 89:

            if Stage.inventaire[5] == "petite potion de hp":
                effect = Stage.dropInfo[Stage.inventaire[5]]["effect"]
                if Hero.life < Hero.maxlife:
                    hpNeedToRestore = Hero.maxlife - Hero.life
                    if hpNeedToRestore >= 50:
                        Hero.life = Hero.life + effect
                        Hero.progressHeroPv = Hero.progressHeroPv + ((effect*100)/ Hero.maxlife)
                        createHeroPanel(gameScreenWindow, Hero.life)
                        Stage.inventaire.remove(Stage.inventaire[5])
                        Stage.saveDropItems.remove(Stage.dropInfo["petite potion de hp"]["image"])
                        addInventory(gameScreenWindow)
                        Stage.messageTab.append(" vous avez utiliser une petite potion de hp")
                        addTextBox(gameScreenWindow)
                    else:
                        Hero.life = Hero.life + hpNeedToRestore
                        Hero.progressHeroPv = Hero.progressHeroPv + ((hpNeedToRestore*100)/ Hero.maxlife)
                        createHeroPanel(gameScreenWindow, Hero.life)
                        Stage.inventaire.remove(Stage.inventaire[5])
                        Stage.saveDropItems.remove(Stage.dropInfo["petite potion de hp"]["image"])
                        addInventory(gameScreenWindow)
                        Stage.messageTab.append(" vous avez utiliser une petite potion de hp")
                        addTextBox(gameScreenWindow)    
                else:
                    Stage.messageTab.append(" Vos points de vie sont déjas au maximum")
                    addTextBox(gameScreenWindow) 

            elif Stage.inventaire[5] == "petit bouclier":
                effect = Stage.dropInfo[Stage.inventaire[5]]["effect"]
                Hero.defense = Hero.defense + effect
                createHeroPanel(gameScreenWindow, Hero.life)          
                Stage.inventaire.remove(Stage.inventaire[5])
                Stage.saveDropItems.remove(Stage.dropInfo["petit bouclier"]["image"])
                addInventory(gameScreenWindow)
                Stage.messageTab.append(" vous avez utiliser petite bouclier, votre défense augmante de 20")
                addTextBox(gameScreenWindow)
            else:
                Stage.messageTab.append("Cette emplacement est vide")
                addTextBox(gameScreenWindow)
        
        #U
        elif event.key() == 85:

            if Stage.inventaire[6] == "petite potion de hp":
                effect = Stage.dropInfo[Stage.inventaire[6]]["effect"]
                if Hero.life < Hero.maxlife:
                    hpNeedToRestore = Hero.maxlife - Hero.life
                    if hpNeedToRestore >= 50:
                        Hero.life = Hero.life + effect
                        Hero.progressHeroPv = Hero.progressHeroPv + ((effect*100)/ Hero.maxlife)
                        createHeroPanel(gameScreenWindow, Hero.life)
                        Stage.inventaire.remove(Stage.inventaire[6])
                        Stage.saveDropItems.remove(Stage.dropInfo["petite potion de hp"]["image"])
                        addInventory(gameScreenWindow)
                        Stage.messageTab.append(" vous avez utiliser une petite potion de hp")
                        addTextBox(gameScreenWindow)
                    else:
                        Hero.life = Hero.life + hpNeedToRestore
                        Hero.progressHeroPv = Hero.progressHeroPv + ((hpNeedToRestore*100)/ Hero.maxlife)
                        createHeroPanel(gameScreenWindow, Hero.life)
                        Stage.inventaire.remove(Stage.inventaire[6])
                        Stage.saveDropItems.remove(Stage.dropInfo["petite potion de hp"]["image"])
                        addInventory(gameScreenWindow)
                        Stage.messageTab.append(" vous avez utiliser une petite potion de hp")
                        addTextBox(gameScreenWindow)    
                else:
                    Stage.messageTab.append(" Vos points de vie sont déjas au maximum")
                    addTextBox(gameScreenWindow) 

            elif Stage.inventaire[6] == "petit bouclier":
                effect = Stage.dropInfo[Stage.inventaire[6]]["effect"]
                Hero.defense = Hero.defense + effect
                createHeroPanel(gameScreenWindow, Hero.life)          
                Stage.inventaire.remove(Stage.inventaire[6])
                Stage.saveDropItems.remove(Stage.dropInfo["petit bouclier"]["image"])
                addInventory(gameScreenWindow)
                Stage.messageTab.append(" vous avez utiliser petite bouclier, votre défense augmante de 20")
                addTextBox(gameScreenWindow)
            else:
                Stage.messageTab.append("Cette emplacement est vide")
                addTextBox(gameScreenWindow)
        
        #I
        elif event.key() == 73:

            if Stage.inventaire[7] == "petite potion de hp":
                effect = Stage.dropInfo[Stage.inventaire[7]]["effect"]
                if Hero.life < Hero.maxlife:
                    hpNeedToRestore = Hero.maxlife - Hero.life
                    if hpNeedToRestore >= 50:
                        Hero.life = Hero.life + effect
                        Hero.progressHeroPv = Hero.progressHeroPv + ((effect*100)/ Hero.maxlife)
                        createHeroPanel(gameScreenWindow, Hero.life)
                        Stage.inventaire.remove(Stage.inventaire[7])
                        Stage.saveDropItems.remove(Stage.dropInfo["petite potion de hp"]["image"])
                        addInventory(gameScreenWindow)
                        Stage.messageTab.append(" vous avez utiliser une petite potion de hp")
                        addTextBox(gameScreenWindow)
                    else:
                        Hero.life = Hero.life + hpNeedToRestore
                        Hero.progressHeroPv = Hero.progressHeroPv + ((hpNeedToRestore*100)/ Hero.maxlife)
                        createHeroPanel(gameScreenWindow, Hero.life)
                        Stage.inventaire.remove(Stage.inventaire[7])
                        Stage.saveDropItems.remove(Stage.dropInfo["petite potion de hp"]["image"])
                        addInventory(gameScreenWindow)
                        Stage.messageTab.append(" vous avez utiliser une petite potion de hp")
                        addTextBox(gameScreenWindow)    
                else:
                    Stage.messageTab.append(" Vos points de vie sont déjas au maximum")
                    addTextBox(gameScreenWindow) 

            elif Stage.inventaire[7] == "petit bouclier":
                effect = Stage.dropInfo[Stage.inventaire[7]]["effect"]
                Hero.defense = Hero.defense + effect
                createHeroPanel(gameScreenWindow, Hero.life)          
                Stage.inventaire.remove(Stage.inventaire[7])
                Stage.saveDropItems.remove(Stage.dropInfo["petit bouclier"]["image"])
                addInventory(gameScreenWindow)
                Stage.messageTab.append(" vous avez utiliser petite bouclier, votre défense augmante de 20")
                addTextBox(gameScreenWindow)
            else:
                Stage.messageTab.append("Cette emplacement est vide")
                addTextBox(gameScreenWindow)
        
        #O
        elif event.key() == 79:

            if Stage.inventaire[8] == "petite potion de hp":
                effect = Stage.dropInfo[Stage.inventaire[8]]["effect"]
                if Hero.life < Hero.maxlife:
                    hpNeedToRestore = Hero.maxlife - Hero.life
                    if hpNeedToRestore >= 50:
                        Hero.life = Hero.life + effect
                        Hero.progressHeroPv = Hero.progressHeroPv + ((effect*100)/ Hero.maxlife)
                        createHeroPanel(gameScreenWindow, Hero.life)
                        Stage.inventaire.remove(Stage.inventaire[8])
                        Stage.saveDropItems.remove(Stage.dropInfo["petite potion de hp"]["image"])
                        addInventory(gameScreenWindow)
                        Stage.messageTab.append(" vous avez utiliser une petite potion de hp")
                        addTextBox(gameScreenWindow)
                    else:
                        Hero.life = Hero.life + hpNeedToRestore
                        Hero.progressHeroPv = Hero.progressHeroPv + ((hpNeedToRestore*100)/ Hero.maxlife)
                        createHeroPanel(gameScreenWindow, Hero.life)
                        Stage.inventaire.remove(Stage.inventaire[8])
                        Stage.saveDropItems.remove(Stage.dropInfo["petite potion de hp"]["image"])
                        addInventory(gameScreenWindow)
                        Stage.messageTab.append(" vous avez utiliser une petite potion de hp")
                        addTextBox(gameScreenWindow)    
                else:
                    Stage.messageTab.append(" Vos points de vie sont déjas au maximum")
                    addTextBox(gameScreenWindow) 

            elif Stage.inventaire[8] == "petit bouclier":
                effect = Stage.dropInfo[Stage.inventaire[8]]["effect"]
                Hero.defense = Hero.defense + effect
                createHeroPanel(gameScreenWindow, Hero.life)          
                Stage.inventaire.remove(Stage.inventaire[8])
                Stage.saveDropItems.remove(Stage.dropInfo["petit bouclier"]["image"])
                addInventory(gameScreenWindow)
                Stage.messageTab.append(" vous avez utiliser petite bouclier, votre défense augmante de 20")
                addTextBox(gameScreenWindow)
            else:
                Stage.messageTab.append("Cette emplacement est vide")
                addTextBox(gameScreenWindow)

        #P
        elif event.key() == 80:

            if Stage.inventaire[9] == "petite potion de hp":
                effect = Stage.dropInfo[Stage.inventaire[9]]["effect"]
                if Hero.life < Hero.maxlife:
                    hpNeedToRestore = Hero.maxlife - Hero.life
                    if hpNeedToRestore >= 50:
                        Hero.life = Hero.life + effect
                        Hero.progressHeroPv = Hero.progressHeroPv + ((effect*100)/ Hero.maxlife)
                        createHeroPanel(gameScreenWindow, Hero.life)
                        Stage.inventaire.remove(Stage.inventaire[9])
                        Stage.saveDropItems.remove(Stage.dropInfo["petite potion de hp"]["image"])
                        addInventory(gameScreenWindow)
                        Stage.messageTab.append(" vous avez utiliser une petite potion de hp")
                        addTextBox(gameScreenWindow)
                    else:
                        Hero.life = Hero.life + hpNeedToRestore
                        Hero.progressHeroPv = Hero.progressHeroPv + ((hpNeedToRestore*100)/ Hero.maxlife)
                        createHeroPanel(gameScreenWindow, Hero.life)
                        Stage.inventaire.remove(Stage.inventaire[9])
                        Stage.saveDropItems.remove(Stage.dropInfo["petite potion de hp"]["image"])
                        addInventory(gameScreenWindow)
                        Stage.messageTab.append(" vous avez utiliser une petite potion de hp")
                        addTextBox(gameScreenWindow)    
                else:
                    Stage.messageTab.append(" Vos points de vie sont déjas au maximum")
                    addTextBox(gameScreenWindow) 

            elif Stage.inventaire[9] == "petit bouclier":
                effect = Stage.dropInfo[Stage.inventaire[9]]["effect"]
                Hero.defense = Hero.defense + effect
                createHeroPanel(gameScreenWindow, Hero.life)          
                Stage.inventaire.remove(Stage.inventaire[9])
                Stage.saveDropItems.remove(Stage.dropInfo["petit bouclier"]["image"])
                addInventory(gameScreenWindow)
                Stage.messageTab.append(" vous avez utiliser petite bouclier, votre défense augmante de 20")
                addTextBox(gameScreenWindow)
            else:
                Stage.messageTab.append("Cette emplacement est vide")
                addTextBox(gameScreenWindow)
        

        #Q
        elif event.key() == 81:

            if Stage.inventaire[10] == "petite potion de hp":
                effect = Stage.dropInfo[Stage.inventaire[10]]["effect"]
                if Hero.life < Hero.maxlife:
                    hpNeedToRestore = Hero.maxlife - Hero.life
                    if hpNeedToRestore >= 50:
                        Hero.life = Hero.life + effect
                        Hero.progressHeroPv = Hero.progressHeroPv + ((effect*100)/ Hero.maxlife)
                        createHeroPanel(gameScreenWindow, Hero.life)
                        Stage.inventaire.remove(Stage.inventaire[10])
                        Stage.saveDropItems.remove(Stage.dropInfo["petite potion de hp"]["image"])
                        addInventory(gameScreenWindow)
                        Stage.messageTab.append(" vous avez utiliser une petite potion de hp")
                        addTextBox(gameScreenWindow)
                    else:
                        Hero.life = Hero.life + hpNeedToRestore
                        Hero.progressHeroPv = Hero.progressHeroPv + ((hpNeedToRestore*100)/ Hero.maxlife)
                        createHeroPanel(gameScreenWindow, Hero.life)
                        Stage.inventaire.remove(Stage.inventaire[10])
                        Stage.saveDropItems.remove(Stage.dropInfo["petite potion de hp"]["image"])
                        addInventory(gameScreenWindow)
                        Stage.messageTab.append(" vous avez utiliser une petite potion de hp")
                        addTextBox(gameScreenWindow)    
                else:
                    Stage.messageTab.append(" Vos points de vie sont déjas au maximum")
                    addTextBox(gameScreenWindow) 

            elif Stage.inventaire[10] == "petit bouclier":
                effect = Stage.dropInfo[Stage.inventaire[10]]["effect"]
                Hero.defense = Hero.defense + effect
                createHeroPanel(gameScreenWindow, Hero.life)          
                Stage.inventaire.remove(Stage.inventaire[10])
                Stage.saveDropItems.remove(Stage.dropInfo["petit bouclier"]["image"])
                addInventory(gameScreenWindow)
                Stage.messageTab.append(" vous avez utiliser petite bouclier, votre défense augmante de 20")
                addTextBox(gameScreenWindow)
            else:
                Stage.messageTab.append("Cette emplacement est vide")
                addTextBox(gameScreenWindow)
            
        #S
        elif event.key() == 83:

            if Stage.inventaire[11] == "petite potion de hp":
                effect = Stage.dropInfo[Stage.inventaire[11]]["effect"]
                if Hero.life < Hero.maxlife:
                    hpNeedToRestore = Hero.maxlife - Hero.life
                    if hpNeedToRestore >= 50:
                        Hero.life = Hero.life + effect
                        Hero.progressHeroPv = Hero.progressHeroPv + ((effect*100)/ Hero.maxlife)
                        createHeroPanel(gameScreenWindow, Hero.life)
                        Stage.inventaire.remove(Stage.inventaire[11])
                        Stage.saveDropItems.remove(Stage.dropInfo["petite potion de hp"]["image"])
                        addInventory(gameScreenWindow)
                        Stage.messageTab.append(" vous avez utiliser une petite potion de hp")
                        addTextBox(gameScreenWindow)
                    else:
                        Hero.life = Hero.life + hpNeedToRestore
                        Hero.progressHeroPv = Hero.progressHeroPv + ((hpNeedToRestore*100)/ Hero.maxlife)
                        createHeroPanel(gameScreenWindow, Hero.life)
                        Stage.inventaire.remove(Stage.inventaire[11])
                        Stage.saveDropItems.remove(Stage.dropInfo["petite potion de hp"]["image"])
                        addInventory(gameScreenWindow)
                        Stage.messageTab.append(" vous avez utiliser une petite potion de hp")
                        addTextBox(gameScreenWindow)    
                else:
                    Stage.messageTab.append(" Vos points de vie sont déjas au maximum")
                    addTextBox(gameScreenWindow) 

            elif Stage.inventaire[11] == "petit bouclier":
                effect = Stage.dropInfo[Stage.inventaire[11]]["effect"]
                Hero.defense = Hero.defense + effect
                createHeroPanel(gameScreenWindow, Hero.life)          
                Stage.inventaire.remove(Stage.inventaire[11])
                Stage.saveDropItems.remove(Stage.dropInfo["petit bouclier"]["image"])
                addInventory(gameScreenWindow)
                Stage.messageTab.append(" vous avez utiliser petite bouclier, votre défense augmante de 20")
                addTextBox(gameScreenWindow)
            else:
                Stage.messageTab.append("Cette emplacement est vide")
                addTextBox(gameScreenWindow)
        
        #D
        elif event.key() == 68:

            if Stage.inventaire[12] == "petite potion de hp":
                effect = Stage.dropInfo[Stage.inventaire[12]]["effect"]
                if Hero.life < Hero.maxlife:
                    hpNeedToRestore = Hero.maxlife - Hero.life
                    if hpNeedToRestore >= 50:
                        Hero.life = Hero.life + effect
                        Hero.progressHeroPv = Hero.progressHeroPv + ((effect*100)/ Hero.maxlife)
                        createHeroPanel(gameScreenWindow, Hero.life)
                        Stage.inventaire.remove(Stage.inventaire[12])
                        Stage.saveDropItems.remove(Stage.dropInfo["petite potion de hp"]["image"])
                        addInventory(gameScreenWindow)
                        Stage.messageTab.append(" vous avez utiliser une petite potion de hp")
                        addTextBox(gameScreenWindow)
                    else:
                        Hero.life = Hero.life + hpNeedToRestore
                        Hero.progressHeroPv = Hero.progressHeroPv + ((hpNeedToRestore*100)/ Hero.maxlife)
                        createHeroPanel(gameScreenWindow, Hero.life)
                        Stage.inventaire.remove(Stage.inventaire[12])
                        Stage.saveDropItems.remove(Stage.dropInfo["petite potion de hp"]["image"])
                        addInventory(gameScreenWindow)
                        Stage.messageTab.append(" vous avez utiliser une petite potion de hp")
                        addTextBox(gameScreenWindow)    
                else:
                    Stage.messageTab.append(" Vos points de vie sont déjas au maximum")
                    addTextBox(gameScreenWindow) 

            elif Stage.inventaire[12] == "petit bouclier":
                effect = Stage.dropInfo[Stage.inventaire[12]]["effect"]
                Hero.defense = Hero.defense + effect
                createHeroPanel(gameScreenWindow, Hero.life)          
                Stage.inventaire.remove(Stage.inventaire[12])
                Stage.saveDropItems.remove(Stage.dropInfo["petit bouclier"]["image"])
                addInventory(gameScreenWindow)
                Stage.messageTab.append(" vous avez utiliser petite bouclier, votre défense augmante de 20")
                addTextBox(gameScreenWindow)
            else:
                Stage.messageTab.append("Cette emplacement est vide")
                addTextBox(gameScreenWindow)
        
        #F
        elif event.key() == 70:

            if Stage.inventaire[13] == "petite potion de hp":
                effect = Stage.dropInfo[Stage.inventaire[13]]["effect"]
                if Hero.life < Hero.maxlife:
                    hpNeedToRestore = Hero.maxlife - Hero.life
                    if hpNeedToRestore >= 50:
                        Hero.life = Hero.life + effect
                        Hero.progressHeroPv = Hero.progressHeroPv + ((effect*100)/ Hero.maxlife)
                        createHeroPanel(gameScreenWindow, Hero.life)
                        Stage.inventaire.remove(Stage.inventaire[13])
                        Stage.saveDropItems.remove(Stage.dropInfo["petite potion de hp"]["image"])
                        addInventory(gameScreenWindow)
                        Stage.messageTab.append(" vous avez utiliser une petite potion de hp")
                        addTextBox(gameScreenWindow)
                    else:
                        Hero.life = Hero.life + hpNeedToRestore
                        Hero.progressHeroPv = Hero.progressHeroPv + ((hpNeedToRestore*100)/ Hero.maxlife)
                        createHeroPanel(gameScreenWindow, Hero.life)
                        Stage.inventaire.remove(Stage.inventaire[13])
                        Stage.saveDropItems.remove(Stage.dropInfo["petite potion de hp"]["image"])
                        addInventory(gameScreenWindow)
                        Stage.messageTab.append(" vous avez utiliser une petite potion de hp")
                        addTextBox(gameScreenWindow)    
                else:
                    Stage.messageTab.append(" Vos points de vie sont déjas au maximum")
                    addTextBox(gameScreenWindow) 

            elif Stage.inventaire[13] == "petit bouclier":
                effect = Stage.dropInfo[Stage.inventaire[13]]["effect"]
                Hero.defense = Hero.defense + effect
                createHeroPanel(gameScreenWindow, Hero.life)          
                Stage.inventaire.remove(Stage.inventaire[13])
                Stage.saveDropItems.remove(Stage.dropInfo["petit bouclier"]["image"])
                addInventory(gameScreenWindow)
                Stage.messageTab.append(" vous avez utiliser petite bouclier, votre défense augmante de 20")
                addTextBox(gameScreenWindow)
            else:
                Stage.messageTab.append("Cette emplacement est vide")
                addTextBox(gameScreenWindow)
        
        #G
        elif event.key() == 71:

            if Stage.inventaire[14] == "petite potion de hp":
                effect = Stage.dropInfo[Stage.inventaire[14]]["effect"]
                if Hero.life < Hero.maxlife:
                    hpNeedToRestore = Hero.maxlife - Hero.life
                    if hpNeedToRestore >= 50:
                        Hero.life = Hero.life + effect
                        Hero.progressHeroPv = Hero.progressHeroPv + ((effect*100)/ Hero.maxlife)
                        createHeroPanel(gameScreenWindow, Hero.life)
                        Stage.inventaire.remove(Stage.inventaire[14])
                        Stage.saveDropItems.remove(Stage.dropInfo["petite potion de hp"]["image"])
                        addInventory(gameScreenWindow)
                        Stage.messageTab.append(" vous avez utiliser une petite potion de hp")
                        addTextBox(gameScreenWindow)
                    else:
                        Hero.life = Hero.life + hpNeedToRestore
                        Hero.progressHeroPv = Hero.progressHeroPv + ((hpNeedToRestore*100)/ Hero.maxlife)
                        createHeroPanel(gameScreenWindow, Hero.life)
                        Stage.inventaire.remove(Stage.inventaire[14])
                        Stage.saveDropItems.remove(Stage.dropInfo["petite potion de hp"]["image"])
                        addInventory(gameScreenWindow)
                        Stage.messageTab.append(" vous avez utiliser une petite potion de hp")
                        addTextBox(gameScreenWindow)    
                else:
                    Stage.messageTab.append(" Vos points de vie sont déjas au maximum")
                    addTextBox(gameScreenWindow) 

            elif Stage.inventaire[14] == "petit bouclier":
                effect = Stage.dropInfo[Stage.inventaire[14]]["effect"]
                Hero.defense = Hero.defense + effect
                createHeroPanel(gameScreenWindow, Hero.life)          
                Stage.inventaire.remove(Stage.inventaire[14])
                Stage.saveDropItems.remove(Stage.dropInfo["petit bouclier"]["image"])
                addInventory(gameScreenWindow)
                Stage.messageTab.append(" vous avez utiliser petite bouclier, votre défense augmante de 20")
                addTextBox(gameScreenWindow)
            else:
                Stage.messageTab.append("Cette emplacement est vide")
                addTextBox(gameScreenWindow)
        
        #H
        elif event.key() == 72:

            if Stage.inventaire[15] == "petite potion de hp":
                effect = Stage.dropInfo[Stage.inventaire[15]]["effect"]
                if Hero.life < Hero.maxlife:
                    hpNeedToRestore = Hero.maxlife - Hero.life
                    if hpNeedToRestore >= 50:
                        Hero.life = Hero.life + effect
                        Hero.progressHeroPv = Hero.progressHeroPv + ((effect*100)/ Hero.maxlife)
                        createHeroPanel(gameScreenWindow, Hero.life)
                        Stage.inventaire.remove(Stage.inventaire[15])
                        Stage.saveDropItems.remove(Stage.dropInfo["petite potion de hp"]["image"])
                        addInventory(gameScreenWindow)
                        Stage.messageTab.append(" vous avez utiliser une petite potion de hp")
                        addTextBox(gameScreenWindow)
                    else:
                        Hero.life = Hero.life + hpNeedToRestore
                        Hero.progressHeroPv = Hero.progressHeroPv + ((hpNeedToRestore*100)/ Hero.maxlife)
                        createHeroPanel(gameScreenWindow, Hero.life)
                        Stage.inventaire.remove(Stage.inventaire[15])
                        Stage.saveDropItems.remove(Stage.dropInfo["petite potion de hp"]["image"])
                        addInventory(gameScreenWindow)
                        Stage.messageTab.append(" vous avez utiliser une petite potion de hp")
                        addTextBox(gameScreenWindow)    
                else:
                    Stage.messageTab.append(" Vos points de vie sont déjas au maximum")
                    addTextBox(gameScreenWindow) 

            elif Stage.inventaire[15] == "petit bouclier":
                effect = Stage.dropInfo[Stage.inventaire[15]]["effect"]
                Hero.defense = Hero.defense + effect
                createHeroPanel(gameScreenWindow, Hero.life)          
                Stage.inventaire.remove(Stage.inventaire[15])
                Stage.saveDropItems.remove(Stage.dropInfo["petit bouclier"]["image"])
                addInventory(gameScreenWindow)
                Stage.messageTab.append(" vous avez utiliser petite bouclier, votre défense augmante de 20")
                addTextBox(gameScreenWindow)
            else:
                Stage.messageTab.append("Cette emplacement est vide")
                addTextBox(gameScreenWindow)
        
        



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GameWindow()
    window.show()
    sys.exit(app.exec())
