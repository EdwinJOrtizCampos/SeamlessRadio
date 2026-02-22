import os
import sys

class ResourcePath:
    """
    Helps using resources from paths,
    wether app is compiled or not
    """
    
    @staticmethod
    def getFrom(rel_path: str) -> str:
        if hasattr(sys, '_MEIPASS'):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, rel_path)
