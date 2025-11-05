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
lvname = 'Unytitled level'
blockx = []
blocky = []
blocklen = []
blockwid = []
blocktype = []
blockname = []
blockcol = []
playerspawn = [0, 0]
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
def setspawn(x, y):
    global playerspawn
    playerspawn = [x, y]
def download(List):
    global blockx, blocky, blocklen, blockwid, blocktype, blockname, blockcol, playerspawn, lvname
    blockx = List[0]
    blocky = List[1]
    blocklen = List[2]
    blockwid = List[3]
    blocktype = List[4]
    blockname = List[5]
    blockcol = List[6]
    playerspawn = List[7]
    lvname = List[8]
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
            break

w = Tk()
w.geometry('1350x690')

def setlevelname(name):
    global w, lvname
    lvname = name
    w.title(name)












#edit mode starts here
''' 
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

commands:

- Ctrl (control): shows all block coordinates
- Shift: shows fps

possible blocks:

-  createblock((x position), (y position), (length), (width), (type), (name), (fill), (outline))
-  setspawn((spawn x), (spawn y))
-  download((List))
-  deleteblock((name))
-  setlevelname((name))
'''
download([[100], [250], [150], [50], ['block'], ['block1'], [[None, '#000000']], [200, 200], 'untitled level'])
setlevelname('template level')


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

print([blockx, blocky, blocklen, blockwid, blocktype, blockname, blockcol, playerspawn, lvname])
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

