from abc import ABC, abstractmethod
import hashlib
from core.utils.TimeUtils import TimeUtils

class PlayableRadio(ABC):
    """
    Base class for every playable radio in this app.
    Allows enforcing some properties
    """
    
    @property
    @abstractmethod
    def path(self) -> None:
        """
        A source path to load when trying to access this
        radio's contents. QMediaPlayer should be able to
        handle almost any audio format we pass from this path
        """
        ...
    
    @property        
    @abstractmethod
    def name(self) -> str:
        """
        Every radio must have a name
        """
        ...

    @property        
    @abstractmethod
    def thumbnail(self) -> str:
        """
        Every radio must have a thumbnail
        """
        ...
    
    @property        
    def freq(self) -> str:
        """
        Every radio must have a frequency (i.e: 12.23MHz)
        This is just a mock value for pseudo realism
        """
        first_half = int(hashlib.sha1(self.name[:len(self.name)//2].encode("utf-8")).hexdigest(), 16) % (10 ** 2)
        second_half = int(hashlib.sha1(self.name[len(self.name)//2:].encode("utf-8")).hexdigest(), 16) % (10 ** 2)
        return f"{first_half}.{second_half}"
        
    @abstractmethod
    def __len__(self) -> int:
        """
        Returns the duration of this radio station, in seconds
        """
        ...
    
    @property
    def __random_offset_s(self) -> int:
        """
        Provides a constant random seed to simulate
        randomness between different radios
        """
        name_hash_int  = int(hashlib.sha1(self.name.encode("utf-8")).hexdigest(), 16)
        
        return TimeUtils.getBaseStartTime() + name_hash_int
    
    @property
    def current_time_s(self) -> int:
        """
        Returns a consistent real time reference
        for seamless behavior
        """
        return self.__random_offset_s % len(self)
