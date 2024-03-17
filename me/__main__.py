from customtkinter import *
from tkinter import *

root = CTk(fg_color='#919203')
root.overrideredirect(True)
root.minsize(308, 134)
root.maxsize(308, 134)
root.attributes('-transparentcolor', '#919203')

ln1 = Frame(root, height=1, width=308 - 10, bg='#0058ee')
ln1.place(x=5, y=0)
ln2 = Frame(root, height=1, width=2, bg='#0058ee')
ln2.place(x=3, y=1)
ln3 = Frame(root, height=1, width=1, bg='#0058ee')
ln3.place(x=2, y=2)
ln4 = Frame(root, height=2, width=1, bg='#0058ee')
ln4.place(x=1, y=3)
ln5 = Frame(root, height=root.winfo_height(), width=1, bg='#0058ee')
ln5.place(x=0, y=5)
ln6 = Frame(root, height=1, width=2, bg='#0058ee')
ln6.place(x=308 - 5, y=1)
ln7 = Frame(root, height=1, width=1, bg='#0058ee')
ln7.place(x=308 - 3, y=2)
ln8 = Frame(root, height=2, width=1, bg='#0058ee')
ln8.place(x=308 -2, y=3)
ln9 = Frame(root, height=root.winfo_height(), width=1, bg='#0058ee')
ln9.place(x=308 -1, y=5)
ln10 = Frame(root, height=1, width=308, bg='#0058ee')
ln10.place(x=0, y=133)
ln11 = Frame(root, height=1, width=308-10, bg='#3d95ff')#
ln11.place(x=5, y=1)
ln12 = Frame(root, height=1, width=308-6, bg='#2b90ff')#
ln12.place(x=3, y=2)
ln13 = Frame(root, height=1, width=308-3, bg='#0372ff')#
ln13.place(x=1, y=3)
ln14 = Frame(root, height=1, width=308-2, bg='#0365f1')#
ln14.place(x=1, y=4)
ln15 = Frame(root, height=1, width=308-1, bg='#005cec')#
ln15.place(x=1, y=5)
ln16 = Frame(root, height=1, width=308, bg='#0058e6')#
ln16.place(x=1, y=6)
ln17 = Frame(root, height=1, width=308, bg='#0055e5')#
ln17.place(x=1, y=7)
ln18 = Frame(root, height=1, width=308, bg='#0054e3')#
ln18.place(x=1, y=8)
ln19 = Frame(root, height=7, width=308, bg='#0055e5')#
ln19.place(x=1, y=9)
ln20 = Frame(root, height=1, width=308, bg='#0058eb')#
ln20.place(x=1, y=16)
ln21 = Frame(root, height=1, width=308, bg='#0058ee')#
ln21.place(x=1, y=17)
ln22 = Frame(root, height=1, width=308, bg='#005bf2')#
ln22.place(x=1, y=18)
ln23 = Frame(root, height=1, width=308, bg='#005bf2')#
ln23.place(x=1, y=19)
ln24 = Frame(root, height=2, width=308, bg='#026afe')#
ln24.place(x=1, y=20)
ln25 = Frame(root, height=1, width=308, bg='#036eff')#
ln25.place(x=1, y=22)
ln26 = Frame(root, height=2, width=308, bg='#026afe')#
ln26.place(x=1, y=23)
ln27 = Frame(root, height=1, width=308, bg='#0060f9')#
ln27.place(x=1, y=25)
ln28 = Frame(root, height=1, width=308, bg='#004de3')#
ln28.place(x=1, y=26)
ln29 = Frame(root, height=1, width=308, bg='#0043cf')#
ln29.place(x=1, y=27)
ln30 = Frame(root, height=134, width=1, bg='#0734da')
ln30.place(x=1, y=28)
ln31 = Frame(root, height=134, width=1, bg='#166aee')
ln31.place(x=2, y=28)
ln32 = Frame(root, height=134, width=1, bg='#0855dd')
ln32.place(x=2, y=28)
ln33 = Frame(root, height=1, width=308, bg='#003edd')
ln33.place(x=3, y=132)
ln34 = Frame(root, height=1, width=308, bg='#003edd')
ln34.place(x=2, y=131)
ln35 = Frame(root, height=1, width=308, bg='#0048f1')
ln35.place(x=2, y=130)
ln36 = Frame(root, height=134, width=1, bg='#0734da')
ln36.place(x=308-1, y=28)
ln37 = Frame(root, height=134, width=1, bg='#166aee')
ln37.place(x=308-2, y=28)
ln38 = Frame(root, height=134, width=1, bg='#0855dd')
ln38.place(x=308-3, y=28)

Win = Frame(root, width=308-6, height=134-32)
Win.place(x=3, y=28)

_x = None
_y = None

def start_move(event):
    global _x, _y
    _x = event.x
    _y = event.y

def stop_move(event):
    global _x, _y
    _x = None
    _y = None

def on_move(event):
    global _x, _y
    deltax = event.x - _x
    deltay = event.y - _y
    x = root.winfo_x() + deltax
    y = root.winfo_y() + deltay
    root.geometry(f"+{x}+{y}")

eln1 = Frame(root, width=1, height=17)
eln1.place(x=281, y=6)
eln2 = Frame(root, width=1, height=1)
eln2.place(x=282, y=23)
eln3 = Frame(root, width=17, height=1)
eln3.place(x=283, y=24)
eln4 = Frame(root, width=1, height=1)
eln4.place(x=300, y=23)
eln5 = Frame(root, width=1, height=17)
eln5.place(x=301, y=6)
eln6 = Frame(root, width=1, height=1)
eln6.place(x=300, y=5)
eln6 = Frame(root, width=17, height=1)
eln6.place(x=283, y=4)
eln6 = Frame(root, width=1, height=1)
eln6.place(x=282, y=5)
eln7 = Frame(root, width=1, height=17, bg='#af3516')#
eln7.place(x=300, y=6)
eln8 = Frame(root, width=17, height=1, bg='#af3516')#
eln8.place(x=283, y=23)
eln9 = Frame(root, width=17, height=1, bg='#e25633')#
eln9.place(x=283, y=5)
eln10 = Frame(root, width=1, height=17, bg='#e25633')#
eln10.place(x=282, y=6)
efn1 = Frame(root, width=17, height=17, bg='#e24b22')#
xl = CTkLabel(root, text='\u00D7', width=0.5, height=0.5, fg_color='#e24b22', font=("Arial", 17, "bold"))
xl.place(x=286.5,y=5)
efn1.place(x=283, y=6)

xl.bind('<Button-1>', lambda event:root.destroy())
eln7.bind('<Button-1>', lambda event:root.destroy())
eln8.bind('<Button-1>', lambda event:root.destroy())
eln9.bind('<Button-1>', lambda event:root.destroy())
eln10.bind('<Button-1>',lambda event: root.destroy())
efn1.bind('<Button-1>', lambda event:root.destroy())

#from ln11 to ln29
ln11.bind("<ButtonPress-1>", start_move)
ln11.bind("<ButtonRelease-1>", stop_move)
ln11.bind("<B1-Motion>", on_move)
ln12.bind("<ButtonPress-1>", start_move)
ln12.bind("<ButtonRelease-1>", stop_move)
ln12.bind("<B1-Motion>", on_move)
ln13.bind("<ButtonPress-1>", start_move)
ln13.bind("<ButtonRelease-1>", stop_move)
ln13.bind("<B1-Motion>", on_move)
ln14.bind("<ButtonPress-1>", start_move)
ln14.bind("<ButtonRelease-1>", stop_move)
ln14.bind("<B1-Motion>", on_move)
ln15.bind("<ButtonPress-1>", start_move)
ln15.bind("<ButtonRelease-1>", stop_move)
ln15.bind("<B1-Motion>", on_move)
ln16.bind("<ButtonPress-1>", start_move)
ln16.bind("<ButtonRelease-1>", stop_move)
ln16.bind("<B1-Motion>", on_move)
ln17.bind("<ButtonPress-1>", start_move)
ln17.bind("<ButtonRelease-1>", stop_move)
ln17.bind("<B1-Motion>", on_move)
ln18.bind("<ButtonPress-1>", start_move)
ln18.bind("<ButtonRelease-1>", stop_move)
ln18.bind("<B1-Motion>", on_move)
ln19.bind("<ButtonPress-1>", start_move)
ln19.bind("<ButtonRelease-1>", stop_move)
ln19.bind("<B1-Motion>", on_move)
ln20.bind("<ButtonPress-1>", start_move)
ln20.bind("<ButtonRelease-1>", stop_move)
ln20.bind("<B1-Motion>", on_move)
ln21.bind("<ButtonPress-1>", start_move)
ln21.bind("<ButtonRelease-1>", stop_move)
ln21.bind("<B1-Motion>", on_move)
ln22.bind("<ButtonPress-1>", start_move)
ln22.bind("<ButtonRelease-1>", stop_move)
ln22.bind("<B1-Motion>", on_move)
ln23.bind("<ButtonPress-1>", start_move)
ln23.bind("<ButtonRelease-1>", stop_move)
ln23.bind("<B1-Motion>", on_move)
ln24.bind("<ButtonPress-1>", start_move)
ln24.bind("<ButtonRelease-1>", stop_move)
ln24.bind("<B1-Motion>", on_move)
ln25.bind("<ButtonPress-1>", start_move)
ln25.bind("<ButtonRelease-1>", stop_move)
ln25.bind("<B1-Motion>", on_move)
ln26.bind("<ButtonPress-1>", start_move)
ln26.bind("<ButtonRelease-1>", stop_move)
ln26.bind("<B1-Motion>", on_move)
ln27.bind("<ButtonPress-1>", start_move)
ln27.bind("<ButtonRelease-1>", stop_move)
ln27.bind("<B1-Motion>", on_move)
ln28.bind("<ButtonPress-1>", start_move)
ln28.bind("<ButtonRelease-1>", stop_move)
ln28.bind("<B1-Motion>", on_move)
ln29.bind("<ButtonPress-1>", start_move)
ln29.bind("<ButtonRelease-1>", stop_move)
ln29.bind("<B1-Motion>", on_move)

root.mainloop()