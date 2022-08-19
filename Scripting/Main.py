import tkinter as tk
from tkinter import filedialog
from gi.repository import Notify
import sys


# from ipaddress import ip_address
# from lib2to3.pgen2.token import NEWLINE
from tkinter import *

class Main:
    classno = {}
    
    def __init__(self):
        # self.textbook()
        # self.ClassNotes()
        # self.VideoLecture()
        # self.printdetails()
        print("hello")
        
        
    def textbook(self):
        #toaster.show_toast("RPAISlate Software Admin", "Please Choose Folder Where TextBook Are Stored", threaded=True,icon_path=None, duration=4)  # 3 seconds
        Notify.init("RPAISlate Software Admin")
        Notify.Notification.new("Please Choose Folder Where TextBook Are Stored").show()
        path_file = filedialog.askdirectory()
        textb = {'TextBook' : path_file}
        self.classno.update(textb)

    def VideoLecture(self):
        #toaster.show_toast("RPAISlate Software Admin", "Please Choose Folder Where VideoLecture Are Stored", threaded=True,icon_path=None, duration=4)
        Notify.init("RPAISlate Software Admin")
        Notify.Notification.new("Please Choose Folder Where VideoLecture Are Stored").show()
        path_file = filedialog.askdirectory()
        textb = {'VideLecture' : path_file}
        self.classno.update(textb)
    
    def ClassNotes(self):
        #toaster.show_toast("RPAISlate Software Admin", "Please Choose Folder Where ClassNotes Are Stored", threaded=True,icon_path=None, duration=4)
        Notify.init("RPAISlate Software Admin")
        Notify.Notification.new("Please Choose Folder Where ClassNotes Are Stored").show()
        path_file = filedialog.askdirectory()
        textb = {'ClassNotes' : path_file}
        self.classno.update(textb)

    def printdetails(self):
        print(self.classno)
        
    def Exit():
        sys.exit()


def call():
    if(len(class_name.get()) < 0):
        print("Empty")
    else:
        print(class_name.get())
    obj = Main()
    

if __name__ == "__main__" :    
    root = tk.Tk()
    win = Tk()
    # toaster = ToastNotifier()
    root.withdraw()
    obj = Main()

    ##GUI
    titl = tk.Label(win, bg="black", relief="flat", bd=10, font=("arial", 35))
    titl.pack(fill=X)

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
    ##For Inputing Class Number
    class_name = tk.Label(
        win,
        text="Class No",
        width=13,
        height=2,
        bd=5,
        # relief=RIDGE,
        font=("times new roman", 12),
        bg="black",
        fg="green",
        borderwidth=0,

    )
    class_name.place(x=52, y=140)

    class_name= Entry(win,
            width=17,
            bd=5,
            validate="key",
            bg="grey",
            fg="white",
            # relief=RIDGE,
            font=("times", 25, "bold"),
            borderwidth=1,
            relief="groove")
    class_name.focus_set()
    class_name.place(x=165,y=139)

    ##For Inputing Class Teachers Details
    teachers_name = tk.Label(
        win,
        text="Teacher's Name",
        width=13,
        height=2,
        bd=5,
        # relief=RIDGE,
        font=("times new roman", 12),
        bg="black",
        fg="green",
        borderwidth=0,

    )
    teachers_name.place(x=52, y=201)

    teachers_name =  Entry(win,
            width=17,
            bd=5,
            validate="key",
            bg="grey",
            fg="red",
            # relief=RIDGE,
            font=("times", 25, "bold"),
            borderwidth=1,
            relief="groove")
    teachers_name.focus_set()
    teachers_name.place(x=165,y=199)

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


    win.mainloop()
