import sys
from PySide6.QtCore import QUrl
from PySide6.QtMultimedia import QMediaPlayer, QMediaContent


player = QMediaPlayer()
music = QMediaContent(QUrl.fromLocalFile("path/to/music.mp3"))
player.setMedia(music)

player.play()


player.setPlaybackRate(-1)
player.setPosition(0)
