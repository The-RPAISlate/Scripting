import tkinter as tk
from tkinter import Entry, Tk, filedialog
from gi.repository import Notify
import sys




def call():
    pass


class UIPage2:
    def __init__(self) -> None:
        pass

    def UI(self):
        root = tk.Tk()
        win = Tk()
        root.withdraw()
        # obj = Main()

        ##GUI
        titl = tk.Label(win, bg="black", relief="flat", bd=10, font=("arial", 35))
        titl.pack(fill='x')

        title1=tk.Label(win, text = "Enter", bg = "black", fg = "dark orange", font=("arial", 27),borderwidth=0)
        title1.place(x=115,y=12)

        title2=tk.Label(win, text = "your", bg = "black", fg = "white", font=("arial", 27),borderwidth=0)
        title2.place(x=212,y=12)

        title3=tk.Label(win, text = "Details", bg = "black", fg = "green", font=("arial", 27),borderwidth=0)
        title3.place(x=290,y=12)

        win.geometry("500x500")
        # win.pack_propagate(0)
        win.resizable(0, 0)

        

        # Create an Entry widget to accept User Input
        folder= tk.Label(
        win,
        text="Folder Name",
        width=10,
        height=2,
        
        bd=5,
        # relief=RIDGE,
        font=("times new roman", 12),
        bg="black",
        fg="green",
        borderwidth=0,

        )
        folder.place(x=100, y=140)

        folder_name= Entry(win,
                width=17,
                bd=5,
                validate="key",
                bg="grey",
                fg="red",
                # relief=RIDGE,
                font=("times", 25, "bold"),
                borderwidth=1,
                relief="groove")
        folder_name.focus_set()
        folder_name.place(x=110,y=140)


        class_name= Entry(win,
                width=17,
                bd=5,
                validate="key",
                bg="grey",
                fg="red",
                # relief=RIDGE,
                font=("times", 25, "bold"),
                borderwidth=1,
                relief="groove")
        class_name.focus_set()
        class_name.place(x=107,y=260)

        submit = tk.Button(
                win,
                text="Submit",
                command=call,
                bd=10,
                font=("times new roman", 18),
                bg="black",
                fg="red",
                height=0,
                width=10,
                # relief=RIDGE,
                borderwidth=0
            )
        submit.place(x=290, y=380)
        
        
        exit = tk.Button(
                win,
                text="Exit",
                command= quit,
                bd=10,
                font=("times new roman", 18),
                bg="black",
                fg="red",
                height=0,
                width=10,
                # relief=RIDGE,
                borderwidth=0
            )
        exit.place(x=90, y=380)


        win.mainloop()\


if __name__ == "__main__":
    obj = UIPage2()
    obj.UI()