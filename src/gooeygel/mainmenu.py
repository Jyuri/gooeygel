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

    def newFile(self):
        pass

    def importFile(self):
        pass

    def exportFile(self):
        pass

    def importData(self):
        pass

    def exportData(self):
        pass

    def aboutSoftware(self):
        pass

    def addons(self):
        pass