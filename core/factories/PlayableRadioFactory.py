from core.sources.Mp3Radio import Mp3Radio
from core.sources.PlayableRadio import PlayableRadio
from pathlib import Path
from core.utils.ResourcePath import ResourcePath

class PlayableRadioFactory:
    """
    Returns PlayableRadios based on criteria
    such as the extension of the filename they wrap
    """
    @staticmethod
    def getRadioFromLocalFile(radio_name: str, path: str, freq:str = None) -> PlayableRadio:
        assert isinstance(radio_name, str), "Radio name must be a string"
        parsed_path = Path(ResourcePath.getFrom(path))
        assert parsed_path.exists(), f"Audio source doesn't exist: {parsed_path}"
        
        match (extension := parsed_path.suffix):
            case '.mp3':
                return Mp3Radio(radio_name, parsed_path.as_posix(), freq)
            case _:
                raise ValueError(f"{extension} files are not supported")
