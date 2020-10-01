import tkinter as tk
import tkinter.messagebox as tkmsb
import tkinter.font as tkFont
window = tk.Tk()

def callback():

    tkmsb.showinfo("Hello!, Nice to Meet you!")


fontstyle=tkFont.Font(family="Lucida Grande")
window.title("Avinash's Program") # sets the title of our window
label = tk.Label(text="Hello Programmers!",width=500,height=500,font=fontstyle,background="#ffffff",foreground="#0078d7")
window.geometry("500x500") # sets the size of our window
button1 = tk.Button(master=window,text="Click Me!",background="#0078d7",foreground="#ffffff",command=(lambda: callback())).place(x=30,y=450)
button2 = tk.Button(master=window,text="Quit!",background="#0078d7",foreground="#ffffff",command=window.quit).place(x=380,y=450)

label.pack()
tk.mainloop()