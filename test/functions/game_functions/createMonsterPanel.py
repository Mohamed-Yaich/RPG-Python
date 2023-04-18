from PySide6.QtWidgets import QWidget, QLabel, QProgressBar
from functions.game_functions.Hero import *
from functions.game_functions.stages.Stage import *


def createMonsterPanel(gameWindow, name, life, strength, defense, level, progress, face_image,):

    monsterPanel = QWidget(gameWindow)
    monsterPanel.setGeometry(20, 225, 350, 140)
    monsterPanel.setStyleSheet("border: none;" "background : none;")

    face = QWidget(monsterPanel)
    face.setGeometry(1, 1, 140, 138)
    face.setStyleSheet(
        "{}".format(face_image))

    labelMonster = QLabel("{} lvl : {}".format(name, level), monsterPanel)
    labelMonster.setGeometry(170, 5, 130, 20)
    labelMonster.setStyleSheet("border: none;" "color : white;" "font-weight : bold;")

    labelPV = QLabel("PV : {}".format(life), monsterPanel)
    labelPV.setGeometry(150, 40, 85, 20)
    labelPV.setStyleSheet("border: none;" "color : white;" "font-weight : bold;")


    progressPV = QProgressBar(monsterPanel)
    progressPV.setValue(progress)
    progressPV.setGeometry(240, 40, 100, 20)
    progressPV.setStyleSheet("text-align: center;" "color : white;" "font-weight : bold;")

    labelSTR = QLabel("Force : {}".format(strength), monsterPanel)
    labelSTR.setGeometry(150, 65, 100, 20)
    labelSTR.setStyleSheet("border: none;" "color : white;" "font-weight : bold;")

    labelDEF = QLabel("Défense : {}".format(defense), monsterPanel)
    labelDEF.setGeometry(150, 90, 100, 20)
    labelDEF.setStyleSheet("border: none;" "color : white;" "font-weight : bold;")

