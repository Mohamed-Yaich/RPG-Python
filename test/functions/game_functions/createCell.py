from PySide6.QtWidgets import QWidget


def createCellInYPosition(widget):

    # Cette fonction récupère en paramettre
    # la ligne créer et y ajoute les cellules
    # Une cellule est un QWidget

    cell = []
    x = 0
    # permet de placer les cellules les une a coté des autres sur une ligne
    xPosition = 0

    for x in range(14):

        X = QWidget(widget)
        X.setGeometry(xPosition, 0, 125, 123)
        X.setStyleSheet("border: none;" "background: none")
        xPosition = xPosition + 49
        x = x + 1
        # Une fois la cellule créer elle est ajouter dans une liste appeler cell
        cell.append(X)
    # la fonction retourne la liste cell qui contient tout les QWidget créer pour une ligne donnée
    return cell
