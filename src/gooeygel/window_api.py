from tkinter import *
from config import window_render_config
from mainmenu import GooeyMenu

def createWindow():
    root = Tk()
    menu = Menu(root)
    root.config(menu=menu)

    GooeyMenuPi = GooeyMenu()
    filemenu = Menu(menu, tearoff=0)
    menu.add_cascade(label='File', menu=filemenu)
    filemenu.add_command(label='New')
    filemenu.add_command(label='Import', command=GooeyMenuPi.openFile)
    filemenu.add_command(label='Export', command=GooeyMenuPi.printOpenFile)
    filemenu.add_separator()
    filemenu.add_command(label='Exit', command=root.quit)

    datamenu = Menu(menu, tearoff=0)
    menu.add_cascade(label='Data', menu=datamenu)
    datamenu.add_command(label='Import Data')
    datamenu.add_command(label='Export Data')
    export_as_menu = Menu(datamenu, tearoff=0)
    export_as_menu.add_command(label='Excel')
    export_as_menu.add_command(label='CSV')
    datamenu.add_cascade(label='Export Data As...', menu=export_as_menu)
    

    helpmenu = Menu(menu, tearoff=0)
    menu.add_cascade(label='Help', menu=helpmenu)
    helpmenu.add_command(label='About')

    root.title(window_render_config['Window Title'])
    root.geometry(window_render_config['Window Size'])
    
    button = Button(root, text="stop", width=25, command=root.quit)
    button.pack()

    root.mainloop()