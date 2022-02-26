from tkinter import *
from tkinter import messagebox


def open_file(file_path):
    fp = None
    try:
        fp = open(file_path)
    except IOError:
        print("Could not read file: ", file_path)

    return fp


file_text = ""
fp = open_file("readme.html")
if fp is not None:
    for one_line in fp:
        file_text = file_text + one_line

    fp.close()

    top = Tk()
    top.title("readme.html")
    c = Canvas(top,width=600)
    c.pack(side='left', expand=1, fill=BOTH)

    myentry_vertscroll = Scrollbar(c)
    myentry_vertscroll.pack(side=RIGHT, fill=Y)

    mytext = Text(c, state=NORMAL, yscrollcommand=myentry_vertscroll.set)
    mytext.pack (side='left', expand=1, fill=BOTH)
    mytext.insert(END,file_text)
    mytext.config(state=DISABLED)

    top.mainloop()