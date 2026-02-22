from core.sources.PlayableRadio import PlayableRadio
from core.factories.PlayableRadioFactory import PlayableRadioFactory

class DataLoader:
    
    @staticmethod
    def getData() -> list[PlayableRadio]:
        """
        Returns a list of radios chosen by the
        developer until user can import their own radios
        """
        return [PlayableRadioFactory.getRadioFromLocalFile("Test FM", "media/audio/Test FM.mp3")]
