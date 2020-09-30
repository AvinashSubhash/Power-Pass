import tkinter as tk
window = tk.Tk()

window.title("Avinash's Program") # sets the title of our window
label = tk.Label(text="Hello Programmers!",width=1920,height=1080,font="Snas",background="#ffffff",foreground="#0078d7")
window.geometry("1920x1080") # sets the size of our window
button1 = tk.Button(master=window,text="Click Me!",background="#0078d7",foreground="#ffffff")

label.pack()
tk.mainloop()