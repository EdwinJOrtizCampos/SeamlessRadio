from PySide6.QtWidgets import (
    QMainWindow, QLabel, QDial,
    QPushButton, QWidget, QTableView
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Signal, QModelIndex

from core.sources.PlayableRadio import PlayableRadio
from core.RadioPlayer import RadioPlayer
from core.utils.DataLoader import DataLoader
from core.utils.TimeUtils import TimeWatcherThread
from core.models.RadioTableModel import RadioTableModel

from view.ui.MainWindow_ui import Ui_MainWindow

class MainWindow(QMainWindow):
    
    volumeChanged = Signal(int)
    radioChanged  = Signal(PlayableRadio)
    
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.dial_volume           : QDial = self.ui.dial_volume
        self.dial_tune             : QDial = self.ui.dial_tune
        self.button_previous       : QPushButton = self.ui.button_previous
        self.button_next           : QPushButton = self.ui.button_next
        self.widget_no_audio       : QWidget = self.ui.widget_no_audio
        self.label_current_time    : QLabel = self.ui.label_current_time
        self.label_radio_name      : QLabel = self.ui.label_radio_name
        self.label_radio_freq      : QLabel = self.ui.label_radio_freq
        self.label_radio_thumbnail : QLabel = self.ui.label_radio_icon
        self.dummy_spacer          : QWidget = self.ui.dummy_compensator_widget
        self.table_radios          : QTableView = self.ui.table_radio_list

        
        self.playlist: list[PlayableRadio] = DataLoader.getData()
        self.timer_thread = TimeWatcherThread(self)
        self.radio_controller = RadioPlayer(self)
        
        self.table_radios.setModel(RadioTableModel(self, self.playlist))

        self.dial_tune.setRange(0, len(self.playlist) - 1)
        self.current_radio_idx = self.dial_tune.value()
        
        self.dial_volume.valueChanged.connect(self.on_volume_dial_changed)
        self.dial_tune.sliderReleased.connect(self.on_tune_dial_song_selected)
        self.dial_tune.valueChanged.connect(self.on_tune_dial_changed)
        self.button_next.clicked.connect(self.on_button_next_radio_clicked)
        self.button_previous.clicked.connect(self.on_button_prev_radio_clicked)
        self.timer_thread.time_changed.connect(self.label_current_time.setText)
        self.table_radios.clicked.connect(self.on_table_radio_clicked)

        self.on_tune_dial_changed()
        self.on_tune_dial_song_selected()
        self.on_volume_dial_changed(50)
        self.timer_thread.start()
        
    def on_volume_dial_changed(self, volume: float) -> None:
        self.current_radio_idx = self.dial_tune.value()
        self.widget_no_audio.setVisible(volume == 0)
        # TODO: Check where this `+6` padding is coming from
        self.dummy_spacer.setFixedWidth([0, self.widget_no_audio.width()+6][volume==0])
        self.volumeChanged.emit(volume)
    
    def on_tune_dial_song_selected(self) -> None:
        radio_to_play: PlayableRadio = self.playlist[self.dial_tune.value()]
        
        # ! Changing tracks using `on_tune_dial_changed` breaks stuff.
        # ! We'll change songs only when the dial is released.
        # ? self.label_radio_name.setText(radio_to_play.name)
        # ? self.label_radio_freq.setText(f"{choice(range(100))}.{choice(range(100))}MHz")
        self.radioChanged.emit(radio_to_play)
    
    def on_tune_dial_changed(self) -> None:
        radio_to_play: PlayableRadio = self.playlist[self.dial_tune.value()]
        self.label_radio_name.setText(radio_to_play.name)
        self.label_radio_freq.setText(f"{radio_to_play.freq}MHz")
        self.label_radio_freq.setText(f"{radio_to_play.freq}MHz")
        self.label_radio_thumbnail.setPixmap(QPixmap(radio_to_play.thumbnail))

    def on_button_next_radio_clicked(self) -> None:
        self.current_radio_idx += 1
        if self.current_radio_idx > self.dial_tune.maximum():
            self.current_radio_idx = 0
        self.dial_tune.setValue(self.current_radio_idx)
        self.on_tune_dial_song_selected()
            
    def on_button_prev_radio_clicked(self) -> None:
        self.current_radio_idx -= 1
        if self.current_radio_idx < self.dial_tune.minimum():
            self.current_radio_idx = self.dial_tune.maximum()
        self.dial_tune.setValue(self.current_radio_idx)
        self.on_tune_dial_song_selected()
        
    def closeEvent(self, event):
        if self.timer_thread.isRunning():
            self.timer_thread.stop()
            self.timer_thread.quit()
            self.timer_thread.wait()
        event.accept()

    def on_table_radio_clicked(self, index: QModelIndex) -> None:
        if self.current_radio_idx == index.column(): return
        self.current_radio_idx = index.column()
        self.dial_tune.setValue(self.current_radio_idx)
        self.on_tune_dial_song_selected()