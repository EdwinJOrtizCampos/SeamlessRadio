from core.sources.PlayableRadio import PlayableRadio
from mutagen.mp3 import MP3

class Mp3Radio(PlayableRadio):
    """
    Represents anything that involves a
    PlayableRadio from a .mp3 file
    """
    
    def __init__(self, name: str, path: str):
        self._name = name
        self._path = path
        
    @property
    def path(self) -> None:
        return self._path

    @property        
    def name(self) -> str:
        return self._name
    
    def __len__(self) -> int:
        return int(MP3(self.path).info.length)
