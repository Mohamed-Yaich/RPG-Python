from PySide6.QtWidgets import QWidget, QLabel, QProgressBar
from functions.game_functions.Hero import *


def createHeroPanel(gameWindow, life):

    heroPanel = QWidget(gameWindow)
    heroPanel.setGeometry(20, 65, 350, 140)
    heroPanel.setStyleSheet("border: none;" "background : none;")

    face = QWidget(heroPanel)
    face.setGeometry(1, 1, 140, 138)
    face.setStyleSheet(
        "background: url(test/sprites/hero/HeroFace.png);" "border: none")

    labelHero = QLabel("HERO lvl : {}".format(Hero.level), heroPanel)
    labelHero.setGeometry(180, 5, 100, 20)
    labelHero.setStyleSheet("border: none;" "color : white;" "font-weight : bold;")

    labelPV = QLabel("PV : {}".format(life), heroPanel)
    labelPV.setGeometry(150, 35, 85, 20)
    labelPV.setStyleSheet("border: none;" "color : white;" "font-weight : bold;")

    progressPV = QProgressBar(heroPanel)
    progressPV.setValue(Hero.progressHeroPv)
    progressPV.setGeometry(240, 35, 100, 20)
    progressPV.setStyleSheet("text-align: center;" "color : white;" "font-weight : bold;")

    labelSTR = QLabel("Force : {}".format(Hero.strength), heroPanel)
    labelSTR.setGeometry(150, 60, 100, 20)
    labelSTR.setStyleSheet("border: none;" "color : white;" "font-weight : bold;")

    labelDEF = QLabel("Défense : {}".format(Hero.defense), heroPanel)
    labelDEF.setGeometry(150, 85, 100, 20)
    labelDEF.setStyleSheet("border: none;" "color : white;" "font-weight : bold;")

    labelEXP = QLabel("EXP : ", heroPanel)
    labelEXP.setGeometry(150, 110, 40, 20)
    labelEXP.setStyleSheet("border: none;" "color : white;" "font-weight : bold;")

    progressEXP = QProgressBar(heroPanel)
    progressEXP.setValue(Hero.progressEXP)
    progressEXP.setGeometry(185, 110, 155, 20)
    progressEXP.setStyleSheet("text-align: center;" "color : white;" "font-weight : bold;")
