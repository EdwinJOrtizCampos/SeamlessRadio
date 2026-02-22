from datetime import datetime, timedelta
from PySide6.QtCore import Signal, QThread
import time

class TimeUtils:
    """
    Provides time references for radios
    """
    
    @staticmethod
    def getBaseStartTime() -> int:
        """
        Provides a common start time
        for all radios to seem like they've
        playing "live" from a standard time reference
        """
        start_date = datetime(2001, 8, 16)
        now = datetime.now()
        
        time_diff: timedelta = now - start_date
        return int(time_diff.total_seconds())

class TimeWatcherThread(QThread):
    time_changed = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self._running = True
        self._last_time = None

    def run(self):
        while self._running:
            current_time = datetime.now().strftime("%H:%M")
            
            if current_time != self._last_time:
                self._last_time = current_time
                self.time_changed.emit(current_time)

            time.sleep(1)

    def stop(self):
        self._running = False
        self.wait()
