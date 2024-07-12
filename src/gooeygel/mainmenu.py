from tkinter import *
from tkinter.filedialog import askopenfilename

class GooeyMenu:

    def __init__(self):
        self.current_accessed_file = None
        pass

    def openFile(self):
        self.current_accessed_file = askopenfilename()
    
    def printOpenFile(self):
        print(self.current_accessed_file)