import os
from turtle import title


class SubDIr:

    def __init__(self) -> None:
        pass

    def writeTextBook(self):
        with open('lectures.txt', 'w') as f:
            f.write("{")
            list_of_keys = list(self.classno.keys())
            f_c_s = len(list_of_keys)
            count1=0
            for i in f_c_s:
                f.write("\t \"" + i + "\""+": [\n")
                listofile = os.listdir(f_c[i])
                f_c_sf = len(listofile)
                count = 0
                for ele in listofile:
                    f.write("\t\t{\n")
                    f.write("\"title\": " + "\"" + ele + "\",")
                    f.write("\"path\": " + (f_c[i]+"\""+ele) + "")
                    if count == f_c_sf:
                        f.write("\t ]\n")
                    else:
                        f.write("\t},\n")
                    count+=1
                if(count1 == f_c_s):
                    f.write("\t]")
                else:
                    f.write("\t],")
                count1+=1
            f.write("}")

