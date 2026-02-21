import sys
import os
sys.path.append(os.getcwd())

from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QSlider, QFileDialog
)
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import QUrl, Qt

from core.factories.PlayableRadioFactory import PlayableRadioFactory
from core.sources.PlayableRadio import PlayableRadio

class MP3PlayerDemo(QWidget):
    def __init__(self, playlist: list[PlayableRadio]):
        super().__init__()
        if not playlist:
            print("No radio tracks detected")
            sys.exit(0)
            
        self.setWindowTitle("Demo MP3 Player")
        self.playlist = playlist
        self.current_index = 0

        layout = QVBoxLayout(self)

        self.radio_label = QLabel("", self)
        layout.addWidget(self.radio_label)

        self.prev_btn = QPushButton("Anterior", self)
        self.prev_btn.clicked.connect(self.prev_radio)
        layout.addWidget(self.prev_btn)

        self.next_btn = QPushButton("Siguiente", self)
        self.next_btn.clicked.connect(self.next_radio)
        layout.addWidget(self.next_btn)

        self.vol_slider = QSlider(Qt.Horizontal, self)
        self.vol_slider.setRange(0, 100)
        self.vol_slider.setValue(50)
        self.vol_slider.valueChanged.connect(self.change_volume)
        layout.addWidget(QLabel("Volumen:"))
        layout.addWidget(self.vol_slider)

        self.audio_output = QAudioOutput()
        self.audio_player = QMediaPlayer()
        self.audio_player.setAudioOutput(self.audio_output)
        self.audio_player.setLoops(QMediaPlayer.Loops.Infinite)

        self.load_radio(self.playlist[self.current_index])

    def load_radio(self, radio: PlayableRadio):
        self.radio_label.setText(f"Reproduciendo: {radio.name}")
        self.audio_player.setSource(QUrl.fromLocalFile(radio.path))
        self.audio_output.setVolume(self.vol_slider.value() / 100)
        
        offset_ms = radio.current_time_s * 1000
        self.audio_player.setPosition(offset_ms)
        self.audio_player.play()

    def change_volume(self, value):
        self.audio_output.setVolume(value / 100)

    def next_radio(self):
        self.current_index = (self.current_index + 1) % len(self.playlist)
        self.load_radio(self.playlist[self.current_index])

    def prev_radio(self):
        self.current_index = (self.current_index - 1) % len(self.playlist)
        self.load_radio(self.playlist[self.current_index])

if __name__ == "__main__":
    app = QApplication(sys.argv)

    playlist = [
        PlayableRadioFactory.getRadioFromLocalFile("Test FM", "media/audio/Test FM.mp3"),
    ]

    player = MP3PlayerDemo(playlist)
    player.resize(300, 200)
    player.show()

    sys.exit(app.exec())
