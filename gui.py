import tkinter as tk
import random

def password_maker(term_one,term_two):
    
    string = []
    string_one = ""
    string_two = ""
    special = ""
    characters = "@#$%&*!?"
    
    #select a part of term_one
    while len(string_one) < 3:
        string_one = (term_one[0:random.randint(0,len(term_one))])
    
    
    #make random characters capital
    
    string_one[0:random.randint(0,len(string_one)-1)].upper()
    
    string.append(string_one)
    
    #select a part of term_two
    while len(string_two) < 2:
        string_two =(term_two[0:random.randint(0,len(term_two))])
    
    string.append(string_two)
    
    #select a range of special characters
    special += characters[random.randint(0,len(characters)-1)]
    string.append(special)
    
    #Adding random characters for extra secure password
    extra_char = (chr(random.randint(97,122)) + chr(random.randint(65,90)) + chr(random.randint(65,90)))
    string.append(extra_char)

    #Shuffling of the list to produce random combinations of the elements
    random.shuffle(string)
    final_string = "".join(map(str,string))

    result = tk.Label(text=final_string,width=40,height=10,foreground="#ffffff",background="#000000",font=('systemfixed',12))
    result.place(x=10,y=340)

def run_gui():

    root = tk.Tk()
    
    root.title("Power Pass - Strong Password Generator")
    root.geometry("700x600")
    root.minsize(700,600)
    root.maxsize(700,600)
    root.config(bg="#ffffff")
    logo = tk.PhotoImage(file="Power-Pass.png")
    logo_label = tk.Label(image=logo,width=560,height=180)
    
    logo_label.image = logo
    logo_label.place(x=58,y=10)



    field_one = tk.Label(text="Enter Your Name : ",width=20,height=2,foreground="#000000",background="#ffffff",font=('systemfixed',12,"bold"))
    field_one.place(x=0,y=200)
    name_entry = tk.Entry(background="#cbe6fc",foreground="#000000")
    name_entry.place(x=500,y=208)
    field_two = tk.Label(text = "Enter any No. (D.O.B,Code etc) :",width=35,height=2,foreground="#000000",background="#ffffff",font=('systemfixed',12,"bold"))
    field_two.place(x=-5,y=250)
    number_entry = tk.Entry(background="#cbe6fc",foreground="#000000")
    number_entry.place(x=500,y=258)
    key_button = tk.PhotoImage(file="key.png")
    generate_button = tk.Button(image=key_button,command = (lambda: password_maker(name_entry.get(),number_entry.get())))
    generate_button.place(x=510,y=380)
    root.iconphoto(False,key_button)



    root.mainloop()
    field_one.pack()
    field_two.pack()
    name_entry.pack()
    number_entry.pack()
    generate_button.pack()
    


if __name__ == "__main__":

    run_gui()
