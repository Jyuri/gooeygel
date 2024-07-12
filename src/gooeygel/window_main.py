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
    filemenu.add_command(label='Open', command=GooeyMenuPi.openFile)
    filemenu.add_command(label='Save', command=GooeyMenuPi.printOpenFile)
    filemenu.add_command(label='Save As...', command=GooeyMenuPi.printOpenFile)
    filemenu.add_separator()
    filemenu.add_command(label='Exit', command=root.quit)

    datamenu = Menu(menu, tearoff=0)
    menu.add_cascade(label='Data', menu=datamenu)
    datamenu.add_command(label='New Dataset')
    datamenu.add_command(label='Open Dataset')
    datamenu.add_command(label='Save Dataset')
    export_as_menu = Menu(datamenu, tearoff=0)
    datamenu.add_cascade(label='Save Dataset As...', menu=export_as_menu)
    export_as_menu.add_command(label='Excel')
    export_as_menu.add_command(label='CSV')
    datamenu.add_separator()
    datamenu.add_command(label='Add to Dataset')
    datamenu.add_command(label='Find in Dataset')
    datamenu.add_command(label='Remove from Dataset')

    helpmenu = Menu(menu, tearoff=0)
    menu.add_cascade(label='Help', menu=helpmenu)
    helpmenu.add_command(label='About')
    helpmenu.add_command(label='API')
    helpmenu.add_command(label='Changelog')

    toolsmenu = Menu(menu, tearoff=0)
    menu.add_cascade(label='Tools', menu=toolsmenu)
    toolsmenu.add_command(label='Addons')

    root.title(window_render_config['Window Title'])
    root.geometry(window_render_config['Window Size'])


    return root