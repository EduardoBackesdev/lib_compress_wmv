from pathlib import Path
import os

class compression:
    
    def __init__(self):
        self.c = Path("./temp/copy.mp3")
    
    def compress(self):
        if not self.c.exists():
            return 0
        
        file_binarie = open(self.c, 'rb')
        
        