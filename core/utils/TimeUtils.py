from datetime import datetime, timedelta


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
