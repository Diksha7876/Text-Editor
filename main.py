import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def openfile(item ,textedit):
    path= askopenfilename(filetypes=[("Text Files","*.txt")])

    if not path:
        return

    textedit.delete(1.0,tk.END)
    with open(path,"r") as a:
        con=a.read()
        textedit.insert(tk.END, con)
    item.title(f"Open File:{path}")

def savefile(item,textedit):
    path=asksaveasfilename(filetypes=[("Text Files","*.txt")])

    if not path:
        return

    with open(path,"w") as a:
        con=textedit.get(1.0,tk.END)
        a.write(con)
    item.title(f"Open File:{path}")
def test():
    item = tk.Tk()
    item.title("Text Editor")
    item.rowconfigure(0,minsize=380)
    item.columnconfigure(1,minsize=480)

    textedit=tk.Text(item,font="Arial 18")
    textedit.grid(row=0,column=1)

    frame=tk.Frame(item,relief=tk.RAISED,bd=2)
    save=tk.Button(frame,text="Save", command= lambda: savefile(item,textedit))
    open=tk.Button(frame,text="Open", command= lambda: openfile(item,textedit))

    save.grid(row=0,column=0,padx=4,pady=4,sticky="ew")
    open.grid(row=1,column=0,padx=4,sticky="ew")
    frame.grid(row=0,column=0,sticky="ns")
    item.bind("<Control-s>", lambda x: savefile(item,textedit))
    item.bind("<Control-s>", lambda x: openfile(item, textedit))
    item.mainloop()

test()