from PySide6.QtWidgets import QWidget


def createCellInYPositionInventory(widget):

    # Cette fonction récupère en paramettre
    # la ligne créer et y ajoute les cellules
    # Une cellule est un QWidget

    cellInventory = []
    x = 0
    # permet de placer les cellules les une a coté des autres sur une ligne
    xPosition = 0

    for x in range(1):

        X = QWidget(widget)
        X.setGeometry(xPosition, 0, 40, 40)
        X.setStyleSheet("border: 5px solid white;")
        x = x + 1
        xPosition = xPosition + 50
        # Une fois la cellule créer elle est ajouter dans une liste appeler cell
        cellInventory.append(X)
    # la fonction retourne la liste cell qui contient tout les QWidget créer pour une ligne donnée
    return cellInventory
