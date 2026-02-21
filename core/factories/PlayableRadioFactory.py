from core.sources.Mp3Radio import Mp3Radio
from core.sources.PlayableRadio import PlayableRadio
from pathlib import Path

class PlayableRadioFactory:
    """
    Returns PlayableRadios based on criteria
    such as the extension of the filename they wrap
    """
    @staticmethod
    def getRadioFromLocalFile(radio_name: str, path: str) -> PlayableRadio:
        assert isinstance(radio_name, str), "Radio name must be a string"
        assert Path(path).exists(), f"Audio source doesn't exist: {path}"
        
        match (extension := Path(path).suffix):
            case '.mp3':
                return Mp3Radio(radio_name, path)
            case _:
                raise ValueError(f"{extension} files are not supported")
