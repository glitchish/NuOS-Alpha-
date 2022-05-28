import time
from tkinter import *
from tkinter import ttk
import Pmw
import os
"""Setting Up the OS"""
nuos = Tk()
Pmw.initialise(nuos)
nuos.geometry("1920x1080")
nuos.title('Nu OS')

Label(nuos,
      text="Welcome to NuOS Alpha! Written in Python 3 Tkinter by Glitchish"
      ).pack()


def close_nuos():
    nuos.destroy()
    exit("NuOS was Shut-Off")  # This may not work, IDK Y


close = Button(nuos,
               text="×",
               command=close_nuos,
               height=1,
               width=1,
               bd="0.5px")

close_nuos_tooltip = Pmw.Balloon(close)
close_nuos_tooltip.bind(close,
                        'Shut-Off NuOS')

close.place(rely=1.0,
            relx=1.0,
            x=0,
            y=0,
            anchor=SE)

nuos.attributes('-fullscreen', True)

mainloop()
"""Clear the console of unnecessary errors"""
os.system("cls||clear")
