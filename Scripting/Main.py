import tkinter as tk
from tkinter import filedialog
from gi.repository import Notify
import sys
import os
from tkinter import *
# import  jpype     
# import  asposecells      
# from asposecells.api import Workbook

class Main:
    classno = {}
    def __init__(self):
        print("Hello")
    
    def Main_Folder_Link(self,subject_name):
        Notify.init("RPAISlate Software Admin")
        Notify.Notification.new("Please Choose Folder Where All materials of "+ subject_name+" Are Stored").show()
        path_file = filedialog.askdirectory()
        textb = {subject_name : path_file}
        self.classno.update(textb)
        print("hello")

    def textbook(self,subject_name):
        #toaster.show_toast("RPAISlate Software Admin", "Please Choose Folder Where TextBook Are Stored", threaded=True,icon_path=None, duration=4)  # 3 seconds
        Notify.init("RPAISlate Software Admin")
        Notify.Notification.new("Please Choose Folder Where TextBook Are Stored").show()
        path_file = filedialog.askdirectory()
        textb = {subject_name : path_file}
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

    def texttojsonconverter(self):
        list_of_txt_file = ["./Textbook.txt","./Lecture.txt","./Notes.txt","./home.txt"]
        for ele in list_of_txt_file:
            base = os.path.splitext(ele)[0]
            os.rename(ele, base + '.json')
        
    #/run/media/sudhanwa/ARCH_GUI_KD/Scripting/lectures.txt
    def WriteTextBook(self):
        with open('Textbook.txt', 'w') as f:
            f.write("{")
            list_of_keys = list(self.classno.keys())
            f_c_s = len(list_of_keys) ##List Of Subjects
            count1=0
            for i in list_of_keys:
                f.write("\t \"" + i + "\""+": [\n")
                listofile = os.listdir(self.classno[i]) ##List of subdirectory of that folder
                f_c_sf = len(listofile)
                for ele in listofile:
                    if(ele.startswith("t") or ele.startswith("T")):
                        list_of_main_Files = os.listdir((self.classno[i]+"/"+ele+"/"))
                        f_c_ssf = len(list_of_main_Files)
                        count2 = 0
                        for temp_ele in list_of_main_Files:
                            f.write("\t\t{\n")
                            f.write("\"title\": " + "\"" + temp_ele + "\",")
                            f.write("\"path\": " + ("\""+self.classno[i]+"/"+ele+"/"+temp_ele+"\"") + "")
                            count2+=1
                            if count2 == f_c_ssf:
                                f.write("\t }\n")
                            else:
                                print(count2)
                                print(f_c_ssf)
                                f.write("\t},\n")
                        count1+=1
                        if(count1 == f_c_sf):
                            f.write("\t]")
                        else:
                            f.write("\t],")
                        count1+=1
            f.write("}")
            
    
    #/run/media/sudhanwa/ARCH_GUI_KD/Scripting/lectures.txt
    def WriteLecture(self):
        with open('Lecture.txt', 'w') as f:
            f.write("{")
            list_of_keys = list(self.classno.keys())
            f_c_s = len(list_of_keys) ##List Of Subjects
            count1=0
            for i in list_of_keys:
                f.write("\t \"" + i + "\""+": [\n")
                listofile = os.listdir(self.classno[i]) ##List of subdirectory of that folder
                f_c_sf = len(listofile)
                for ele in listofile:
                    if(ele.startswith("l") or ele.startswith("L")):
                        list_of_main_Files = os.listdir((self.classno[i]+"/"+ele+"/"))
                        f_c_ssf = len(list_of_main_Files)
                        count2 = 0
                        for temp_ele in list_of_main_Files:
                            f.write("\t\t{\n")
                            f.write("\"title\": " + "\"" + temp_ele + "\",")
                            f.write("\"path\": " + ("\""+self.classno[i]+"/"+ele+"/"+temp_ele+"\"") + "")
                            count2+=1
                            if count2 == f_c_ssf:
                                f.write("\t }\n")
                            else:
                                print(count2)
                                print(f_c_ssf)
                                f.write("\t},\n")
                        count1+=1
                        if(count1 == f_c_sf):
                            f.write("\t]")
                        else:
                            f.write("\t],")
                        count1+=1
            f.write("}")

    #/run/media/sudhanwa/ARCH_GUI_KD/Scripting/lectures.txt
    def WriteNotes(self):
        with open('Notes.txt', 'w') as f:
            f.write("{")
            list_of_keys = list(self.classno.keys())
            f_c_s = len(list_of_keys) ##List Of Subjects
            count1=0
            for i in list_of_keys:
                f.write("\t \"" + i + "\""+": [\n")
                listofile = os.listdir(self.classno[i]) ##List of subdirectory of that folder
                f_c_sf = len(listofile)
                for ele in listofile:
                    if(ele.startswith("n") or ele.startswith("N")):
                        list_of_main_Files = os.listdir((self.classno[i]+"/"+ele+"/"))
                        f_c_ssf = len(list_of_main_Files)
                        count2 = 0
                        for temp_ele in list_of_main_Files:
                            f.write("\t\t{\n")
                            f.write("\"title\": " + "\"" + temp_ele + "\",")
                            f.write("\"path\": " + ("\""+self.classno[i]+"/"+ele+"/"+temp_ele+"\"") + "")
                            count2+=1
                            if count2 == f_c_ssf:
                                f.write("\t }\n")
                            else:
                                print(count2)
                                print(f_c_ssf)
                                f.write("\t},\n")
                        count1+=1
                        if(count1 == f_c_sf):
                            f.write("\t]")
                        else:
                            f.write("\t],")
                        count1+=1
            f.write("}")


    def WriteDetails(self):
        with open('home.txt', 'w') as f:
            f.write("{\n")
            f.write("\t \"class\""+ ": "+ class_name.get()+","+"\n")
            f.write("\t \"teacher\"" + ": \"" + teachers_name.get()+"\","+"\n")
            f.write("\t \"Subjects\"" + ": ["+"\n")
            list_of_keys = list(self.classno.keys())
            f_c = len(list_of_keys)
            count = 0
            for i in list_of_keys:
                f.write("{\n")
                f.write("\t\t \"" +"name"+"\""+": "+"\""+i+"\""+",")
                f.write("\t\t \"" +"url"+"\""+": "+"\""+self.classno[i]+"\"")
                count+=1
                if count == f_c:
                    f.write("\t }\n")
                else:
                    f.write("\t},\n")

            f.write("\t ]")
            f.write("}")


def call():
    list_of_subject = Subject_name.get().split(",")
    obj = Main()
    for i in list_of_subject:
        obj.Main_Folder_Link(i)
    obj.WriteDetails()
    obj.WriteLecture()
    obj.WriteNotes()
    obj.WriteTextBook()
    obj.texttojsonconverter()
    
    
if __name__ == "__main__" :    
    root = tk.Tk()
    win = Tk()
    root.withdraw()
    root.title("Teacher Folder Selection Window")
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
    win.resizable(0, 0)

    class_name = tk.Label(
        win,
        text="Class No",
        width=13,
        height=2,
        bd=5,
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
            fg= "white",
            # relief=RIDGE,
            font=("times", 25, "bold"),
            borderwidth=1,
            relief="groove")
    teachers_name.focus_set()
    teachers_name.place(x=165,y=199)

    ##Subjects Name :- 
    ##For Inputing Class Teachers Details
    Subject_name = tk.Label(
        win,
        text="Subject List",
        width=13,
        height=2,
        bd=5,
        # relief=RIDGE,
        font=("times new roman", 12),
        bg="black",
        fg="green",
        borderwidth=0,
    )
    Subject_name.place(x=52, y=261)

    Subject_name =  Entry(win,
            width=17,
            bd=5,
            validate="key",
            bg="grey",
            fg="white",
            # relief=RIDGE,
            font=("times", 25, "bold"),
            borderwidth=1,
            relief="groove")
    Subject_name.focus_set()
    Subject_name.place(x=165,y=263)
    
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