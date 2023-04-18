def addSprite(mapCell, y, x, monsterDirection):
    sprite = mapCell[y][x]
    sprite.setStyleSheet(
        "{}".format(monsterDirection))

