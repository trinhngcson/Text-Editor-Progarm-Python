import os
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *


def change_color():
    color = colorchooser.askcolor(title= "Pick color")
    text_area.config(fg= color[1])

def change_font(*args):
    text_area.config(font=(font_name.get(),size_box.get()))

def new_file():
    win.title("Untitled")
    text_area.delete(1.0, END)

def open_file():
    file = askopenfilename(defaultextension = ".txt", 
                        file=[("All files", "*.*"), ("Text Documents", "*.txt")])
    try:
        win.title(os.path.basename(file))

        text_area.delete(1.0,END)

        file = open(file, "r")

        text_area.insert(1.0, file.read().encode("windows-1252").decode("utf-8"))

    except Exception:
        print("Cant read file")
    finally:
        file.close()
def save_file():
    file = filedialog.asksaveasfile(initialfile= win.title(),defaultextension = '.txt',
                                    filetype = [("All Files","*.*"),("Text Documents","*.txt")])
    if file is None:
        return
    else:
        try:    
            file.write(text_area.get(1.0,END).encode("utf-8").decode("windows-1252"))
        except Exception as e:
            showwarning("Warning","{}".format(e))
        finally:   
            file.close()
    
def cut():
    text_area.event_generate("<<Cut>>")


def copy():
    text_area.event_generate("<<Copy>>")

def paste():
    text_area.event_generate("<<Paste>>")

def about():
    showinfo("About this program","This is a program written by you!!!")

def quit():
    answer = askyesnocancel("Text Editor", "Do you want to save changes to {}".format(win.title()))
    if answer:
        showinfo("aaa","aaa")
        win.destroy()
    elif answer is None:
        return
    else:
        win.destroy()


win = Tk()
win.title("Text Editor Program")
file = None

win_width = 500
win_height = 500
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()

x =int ((screen_width / 2 ) - (win_width / 2))
y =int ((screen_height / 2 ) - (win_height / 2))
win.geometry("{}x{}+{}+{}".format(win_width,win_height, x ,y))

font_name = StringVar()
font_name.set("Arial")


font_size = StringVar(win)
font_size.set("25")


text_area = Text(win, font=(font_name.get(),font_size.get()))


scroll_bar = Scrollbar(text_area)
win.grid_rowconfigure(0, weight = 1)
win.grid_columnconfigure(0, weight = 1)
text_area.grid(sticky=N + E + S + W)
scroll_bar.pack(side=RIGHT, fill = Y)
text_area.config(yscrollcommand= scroll_bar.set)

frame = Frame(win)
frame.grid()

btnColor = Button(frame, text = "Color",command=change_color) 
btnColor.grid(row=0, column= 0)

font_box = OptionMenu(frame, font_name, *font.families(), command=change_font)
font_box.grid(row= 0, column= 1)

size_box = Spinbox(frame, from_=1, to = 100,width=5, textvariable=font_size,command= change_font)
size_box.grid(row= 0, column= 2)

menu_bar = Menu(win)
win.config(menu= menu_bar)

file_menu = Menu(menu_bar, tearoff= 0)
menu_bar.add_cascade(label="File",menu = file_menu)
file_menu.add_command(label= "New", command=new_file)
file_menu.add_command(label= "Open", command=open_file)
file_menu.add_command(label= "Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label= "Quit", command=quit)

edit_menu = Menu(menu_bar, tearoff= 0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)

help_menu = Menu(menu_bar,tearoff= 0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)

win.mainloop()