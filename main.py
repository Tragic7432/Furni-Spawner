from tkinter import *
from g_python.gextension import Extension
from g_python.hpacket import HPacket

extension_info = {
    "title": "Furni Spawner",
    "description": "Spawn furnis client-side",
    "author": "Toxicwave",
    "version": "1.0"
}

extension_settings = {
    "use_click_trigger": False,
    "can_leave": True,
    "can_delete": True
}
ext = Extension(extension_info, args=['-p', '9092'], extension_settings=extension_settings)
ext.start()


furni_id = 1

def spawnIt():
   global furni_id
   item_id = itemid.get()
   x_loc = xloc.get()
   y_loc = yloc.get()
   ext.send_to_client(HPacket('ObjectAdd',furni_id, item_id, x_loc, y_loc, 0, '0.00', '1.0', 0, 0, '0', -1, 1, 5896864, 'admin'))
   furni_id += 1


window = Tk()
window.title("Furni Spawner")
window.geometry("400x400")
window.resizable(False, False)
itemid = IntVar(window)
xloc = IntVar(window)
yloc = IntVar(window)
window.iconphoto(False, PhotoImage(file='icon.png'))
frame_alt = Frame(window, bg='#FFADD4')
frame_alt.place(relx=0, rely=0.5, relwidth=1, relheight=0.2)
frame_ust = Frame(window, bg='#FFADD4')
frame_ust.place(relx=0, rely=0, relwidth=1, relheight=0.5)
frame_enalt = Frame(window, bg='#FFADD4')
frame_enalt.place(relx=0, rely=0.7, relwidth=1, relheight=0.3)
L1 = Label(frame_alt, padx=20, bg='#FFADD4', fg='#ffffff', text="Item ID:", font="Verdana 20 bold")
L1.pack(side = LEFT)
E1 = Entry(frame_alt, bd =5, textvariable = itemid)
E1.pack(side = LEFT)
L3 = Label(frame_ust, padx=20, bg='#FFADD4', fg='#ffffff', text=":Y", font="Verdana 20 bold")
L3.pack(side = RIGHT)
L2 = Label(frame_ust, padx=20, bg='#FFADD4', fg='#ffffff', text="X:", font="Verdana 20 bold")
L2.pack(side = LEFT)
sp2 = Spinbox(frame_ust, width=5, from_=1, to=500, textvariable = xloc)
sp2.pack(side = LEFT)
sp = Spinbox(frame_ust,width=5, from_=1, to=500, textvariable = yloc)
sp.pack(side = RIGHT)
B = Button(frame_enalt, relief='groove', bg='#ffffff', bd=10, text='Send', font='Cooper 15 bold', command = spawnIt)
B.pack(side = BOTTOM)
window.mainloop()