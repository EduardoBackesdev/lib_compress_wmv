from pathlib import Path
import os

class compression:
    
    def __init__(self):
        self.c = Path("./temp/copy.wav")
    
    def compress(self):
        if not self.c.exists():
            return 0
        
        file_binarie = open(self.c, 'rb')
        
        