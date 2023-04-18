import sys


from PySide6.QtCore import Slot
from PySide6.QtGui import QIcon, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QCalendarWidget, QLabel, \
    QPushButton, QCheckBox, QSpinBox, QLCDNumber, QLineEdit, \
    QSlider, QProgressBar


class MainWindow(QMainWindow):

    # j'appel la fonction constructeur
    def __init__(self):

        # je rappel le constructeur parent
        super().__init__()

        # self représente la fenètre de l'app ici je donne un titre a la fenètre
        self.setWindowTitle("Calandar and form")

        # donner une taille minimum a la fenètre
        self.setMinimumSize(800, 600)
        self.setMaximumSize(800, 600)

        # afficher une infobule
        self.setToolTip("Calandar and form")

        # On change l'icône affichée dans le bandeau supérieur de la fenêtre.
        self.setWindowIcon(QIcon("test/icons/calandar.png"))

        # On retaille la fenêtre (800 pixels de large et 600 en hauteur).
        self.resize(800, 600)

        # Le type QWidget représente un conteneur de widgets (et il est lui-même un widget).

        # On crée une instance que l'on va mettre au centre de la fenêtre.
        centralArea = QWidget()
        hero = QWidget(centralArea)
        hero.setGeometry(700, 500, 50, 48)
        hero.setStyleSheet("background: url(test/sprites/sprite/Hero.png)")
        # top/bottom/right/left
        # hero.setStyleSheet("padding-right: 50px")

        # On lui met une couleur d'arrière-plan, histoire de bien le voir.
        # centralArea.setStyleSheet("background: #419eee")

        # On injecte ce widget en tant que zone centrale.
        self.setCentralWidget(centralArea)

        # On ajoute une barre de status
        statusBar = self.statusBar()

        # On place un message dans la barre de status
        statusBar.showMessage("c'est ma status bar")

        # On place maintenant chacun des composants souhaités dans la zone centrale.
        # Un calendriller
        calendar = QCalendarWidget(centralArea)
        calendar.setGeometry(10, 10, 300, 200)
        # On connecte le signal selectionChanged exposé par le calendier au slot dateSelected.
        calendar.selectionChanged.connect(self.dateSelected)

        # Une zone qui affiche des nombre
        lcd = QLCDNumber(self)
        lcd.display(1234)
        lcd.setGeometry(10, 220, 300, 70)

        # Un label
        label = QLabel("This is a label", centralArea)
        label.setGeometry(320, 10, 270, 30)

        # Un bouton
        button = QPushButton("This is a button", centralArea)
        button.setGeometry(320, 50, 270, 30)
        # je connect mon boutton a un gestionaire d'event (buttonClicked) qui écoute l'event click
        button.clicked.connect(self.buttonClicked)

        # un champ texte
        textBox = QLineEdit("This is a text box", centralArea)
        textBox.setGeometry(320, 90, 270, 30)

        # Une case a cocher
        checkBox = QCheckBox("This is a check box", centralArea)
        checkBox.setGeometry(320, 130, 270, 30)

        # Un champ pour sélectionner un nombre
        spinBox = QSpinBox(centralArea)
        spinBox.setValue(50)
        spinBox.setGeometry(320, 170, 270, 30)

        # Un slider
        slider = QSlider(Qt.Horizontal, centralArea)
        slider.setValue(50)
        slider.setGeometry(320, 220, 270, 30)
        # On connecte le signal valueChanged exposé par le slider au slot valueChanged.
        slider.valueChanged.connect(self.valueChanged)

        # Une barre de progrèssion
        progress = QProgressBar(centralArea)
        progress.setValue(50)
        progress.setGeometry(320, 260, 270, 30)

    def keyPressEvent(self, event):

        key = event.key()
        print(key)

    @Slot()  # un slot est un géstionnaire dévènement
    def buttonClicked(self):
        # je récupère l'éméteur de l'event qui est mon bouton
        btn = self.sender()
        print(f"Button <{btn.text()}> clicked")

    @Slot(int)
    def valueChanged(self, value: int):
        print(f"Slider selected value is {value}")

    @Slot()
    def dateSelected(self):
        # préciser se qu'est calendar (QCalendarWidget) va me permettre d'avoir l'aide a l'autocompletion
        # On dit que j'ai typé ma variable
        calendar: QCalendarWidget = self.sender()
        print(f"Selected date is {calendar.selectedDate()}")


if __name__ == "__main__":
    # On crée l'instance d'application en lui passant le tableau des arguments.
    app = QApplication(sys.argv)

    # Instancier votre fenêtre graphique.
    window = MainWindow()
    # et afficher votre fenêtre graphique.
    window.show()

    # On démarre la boucle de gestion des événements.
    sys.exit(app.exec())
