from tkinter import *
from time import *
from math import *
code = 0
try:
    from keyboard import *
    code = 1
except:
    print('please install module "keyboard" to access most of this program. \nyou can do this by typing "pip install keyboard" in the terminal.')
mousex = 0
mousey = 0
lvname = 'Untitled level'
blockx = []
blocky = []
blocklen = []
blockwid = []
blocktype = []
blockname = []
blockcol = []
playerspawn = [0, 0]
blockmove = []
def createblock(x, y, len, wid, type, name, fill, out):
    global blockx, blocky, blocklen, blockwid, blocktype, blockname, blockcol
    if not name in blockname:
        blockx.append(x)
        blocky.append(y)
        blocklen.append(len)
        blockwid.append(wid)
        blocktype.append(type)
        blockname.append(name)
        blockcol.append([fill, out])
        blockmove.append([0, 0])
def setspawn(x, y):
    global playerspawn
    playerspawn = [x, y]
def download(List):
    global blockx, blocky, blocklen, blockwid, blocktype, blockname, blockcol, playerspawn, lvname, blockmove
    blockx = List[0]
    blocky = List[1]
    blocklen = List[2]
    blockwid = List[3]
    blocktype = List[4]
    blockname = List[5]
    blockcol = List[6]
    playerspawn = List[7]
    # since create.py is frequently updating, adding new features may change the length of List
    if len(List) == 9:
        blockmove = List[8]
    else:
        blockmove = []
        for i in range(len(blockname)):
            blockmove.append([0, 0])
            
    if len(List) == 10:
            lvname = List[9]
    else:
        lvname = 'Untitled level'



def deleteblock(name):
    global blockx, blocky, blocklen, blockwid, blocktype, blockname, blockcol
    for i in range(len(blockname)):
        if blockname[i] == name:
            blockx.pop(i)
            blocky.pop(i)
            blocklen.pop(i)
            blockwid.pop(i)
            blockname.pop(i)
            blockcol.pop(i)
            blocktype.pop(i)
            blockmove.pop(i)
            break

w = Tk()
w.geometry('1350x690')

def setlevelname(name):
    global w, lvname
    lvname = name
    w.title(name)

def setMove(name, xmove, ymove):
    global blockmove
    for i in range(len(blockname)):
        if blockname[i] == name:
            blockmove[i] = [xmove, ymove]
            break












#edit mode starts here
''' 

installs:
- keyboard (pip install keyboard)

possible blocks (in block type):
-  block (fill = None, outline = #000000)
-  danger (fill = None, outline = #000000)
-  water (fill = None, outline = #000000)
-  ladder (fill = None, outline = #000000)
-  enemy (fill = None, outline = #000000)
-  moveblock (fill = #000000, outline = #000000)
-  end (fill = green, outline = #000000)


also, the rules are:
-  the block name should always be different
- the player and block spawn should be within the window (1350x690)
- the block length and width should be positive numbers
-  the block type should be one of the listed types above
-  the fill and outline should be color values (like 'red', '#ff0000', etc. or None for no fill)
-  there should be only one 'end' block per level (working on code to have more than one)

commands:

- Ctrl (control): shows all block coordinates
- Shift: shows fps

possible blocks:

-  createblock((x position), (y position), (length), (width), (type), (name), (fill), (outline))
-  setspawn((spawn x), (spawn y))
-  download((List))
-  deleteblock((name))
-  setlevelname((name))
-  setMove((name), (xmove), (ymove)) -- (only works for moveblock and enemy)

HELP:
- contact me with akimromanov@icloud.com or 010791@britishschool.be for any help
'''

download([[100], [250], [150], [50], ['block'], ['block1'], [[None, '#000000']], [200, 200]])
setlevelname('template level')
deleteblock('block1')
createblock(100, 250, 150, 50, 'block', 'block1', 'gray', 'black')
createblock(300, 300, 150, 50, 'block', 'block2', 'gray', 'black')
createblock(300, 275, 25, 25, 'danger', 'danger1', "#ba0000", '#ff0000')
createblock(500, 260, 150, 50, 'block', 'block3', 'gray', 'black')
createblock(700, 220, 150, 50, 'end', 'End', "#06c300", "#09ff00")


#edit mode ends here














c = Canvas(w, width=1350, height=690)
c.pack(anchor='w')

fps = 0
ttime = 0

def mouse_update():
    global mousex, mousey
    mousex = w.winfo_pointerx() - w.winfo_rootx()
    mousey = w.winfo_pointery() - w.winfo_rooty()

def square(x1, y1, x2, y2, Fill, out):
    c.create_rectangle(x1, y1, x2, y2, outline=out, fill=Fill)

print([blockx, blocky, blocklen, blockwid, blocktype, blockname, blockcol, playerspawn, blockmove, lvname])
Time_ = 0
while 1:
    Time_ = time()
    c.delete('all')
    try:
        square(playerspawn[0], playerspawn[1], playerspawn[0] + 20, playerspawn[1] + 20, None, '#0d00ff')
        if is_pressed('shift') and code == 1:
            c.create_text(50, 50, text=f'fps: {fps}', fill='#000000', font=('Arial', 15), anchor='w')
        for i in range(len(blockname)):
            square(blockx[i],blocky[i],blockx[i] + blocklen[i],blocky[i] + blockwid[i], blockcol[i][0], blockcol[i][1])
            if is_pressed('Ctrl') and code == 1:
                c.create_text(blockx[i] - 30, blocky[i] - 10, text=f'{blockx[i]}, {blocky[i]}', fill='#000000', font=('Arial', 8))
                c.create_text(blockx[i] + blocklen[i] + 30, blocky[i] - 10, text=f'{blockx[i] + blocklen[i]}, {blocky[i]}', fill='#000000', font=('Arial', 8))
                c.create_text(blockx[i] - 30, blocky[i] + blockwid[i] + 10, text=f'{blockx[i]}, {blocky[i] + blockwid[i]}', fill='#000000', font=('Arial', 8))
                c.create_text(blockx[i] + blocklen[i] + 30, blocky[i] + blockwid[i] + 10, text=f'{blockx[i] + blocklen[i]}, {blocky[i] + blockwid[i]}', fill='#000000', font=('Arial', 8))
    except:
        pass


    square(5, 5, 1350, 690, None, '#000000')

    mouse_update()

    c.create_text(mousex + 30, mousey - 10, text=f'{mousex}, {mousey}', fill='#000000', font=('Arial', 8))
    c.update()

    if round(time()) % 2 == 0 and floor(time()) != ttime:
        ttime = floor(time())
        fps = round(1 / (time() - Time_))

w.mainloop()

