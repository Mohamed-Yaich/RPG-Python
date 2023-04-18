def close_game(self):
    self.close()
    self.close_game_signal.emit()