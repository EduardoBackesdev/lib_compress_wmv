import os
import shutil

class upload_file:
    
    def upload(self, a:str):
        
        if not a.lower().endswith(".wmv"):
            return 0
        
        if not os.path.isfile(a):
             return 0
         
        size = os.path.getsize(a)
         
        if size > 500 * 1024 * 1024:
             return 0 
         
        try:
            shutil.copy("./temp", a)
            return 1
        except Exception as a:
            print(a)
            return 0     