from tkinter import *
import os
from tkinter import filedialog
from tkinter import messagebox

root= Tk()
root.title("Notepad")
root.minsize(width=400,height=400)

menu = Menu(root)
root.config(menu=menu)
filename = None
def exitcommand():
	           root.destroy()
def newfile():
	         root.title("Untitled-Notepad")
	         text.delete(0.0,END)
def savefile():
	          f= filedialog.asksaveasfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),
                                                ("Text Documents","*.txt")])
	          if f=="":
	          	      f=None
	          else:
	          	   file=open(f,"w")
	          	   file.write(text.get(1.0,END))
	          	   file.close()
	          	   root.title(os.path.basename(f)+"-Notepad")

	        
def openfile():
	           f= filedialog.askopenfilename(defaultextension=".txt",
                                  filetypes=[("All Files","*.*"),
                                      ("Text Documents","*.txt")])
	           if f=="":
	           	       messagebox.showerror("Oops!","Cannot open file")
	           else:	       
	                root.title(os.path.basename(f)+"-Notepad")
	                contents= open(f,"r")
	                text.insert(0.0,contents.read())
	                contents.close()
def help():
			messagebox.showinfo("About Notepad","Just another text editor.")
def cut():
			text.event_generate("<<Cut>>")
def copy():
			text.event_generate("<<Copy>>")
def paste():
			text.event_generate("<<Paste>>")

text= Text(root)
text.pack(fill="both",expand=True)
filemenu = Menu(menu)
menu.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="New",command=newfile)
filemenu.add_command(label="Open",command=openfile)
filemenu.add_command(label="Save",command=savefile)

filemenu.add_separator()
filemenu.add_command(label="Exit",command=exitcommand)
editmenu= Menu(menu)
menu.add_cascade(label="Edit",menu=editmenu)
editmenu.add_command(label="Cut: Ctrl+X",command=cut)
editmenu.add_command(label="Copy: Ctrl+C",command=copy)
editmenu.add_command(label="Paste: Ctrl+V",command=paste)
helpmenu= Menu(menu)
menu.add_cascade(label="Help",menu=helpmenu)
helpmenu.add_command(label="About Notepad",command=help)
root.mainloop()