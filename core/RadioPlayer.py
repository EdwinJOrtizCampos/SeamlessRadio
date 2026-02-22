from PySide6.QtWidgets import QMainWindow
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import QUrl, QObject

from core.sources.PlayableRadio import PlayableRadio


class RadioPlayer(QObject):
    def __init__(self, parent: QMainWindow):
        super().__init__(parent)
        
        self._current_volume = 50
        self.audio_output = QAudioOutput()
        self.audio_player = QMediaPlayer()
        
        self.audio_player.setAudioOutput(self.audio_output)
        self.audio_player.setLoops(QMediaPlayer.Loops.Infinite)

        self.parent().volumeChanged.connect(self.change_volume)
        self.parent().radioChanged.connect(self.on_radio_selected)
        self.audio_player.mediaStatusChanged.connect(self._on_media_status)

    def load_radio(self, radio: PlayableRadio):
        self.audio_player.stop()
        self.pending_offset = int(radio.current_time_s * 1000)
        self.audio_player.setSource(QUrl.fromLocalFile(radio.path))

    def _on_media_status(self, status):

        if status == QMediaPlayer.MediaStatus.LoadedMedia:
            self.audio_output.setVolume(self._current_volume / 100)

            if self.pending_offset > 0:
                self.audio_player.setPosition(self.pending_offset)

            self.audio_player.play()

    def change_volume(self, value: float):
        self._current_volume = value
        self.audio_output.setVolume(self._current_volume / 100)

    def on_radio_selected(self, radio: PlayableRadio):
        self.load_radio(radio)
