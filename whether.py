from tkinter import  Label,Frame,Button,Text,StringVar,Tk,Entry,LabelFrame

import tkinter.messagebox
import requests

class whether_app:
    def __init__(self,root):
        self.root=root
        self.root.title("Whether App")
        self.root.geometry("500x300")
        self.root.resizable(0,0)
        self.root.iconbitmap("whether.ico")


        search_what=StringVar()

        



    #====================================================
        def on_enter1(e):
            But_search['background']="black"
            But_search['foreground']="cyan"
  
        def on_leave1(e):
            But_search['background']="SystemButtonFace"
            But_search['foreground']="SystemButtonText"    

        def clear():
            TXT.delete('1.0',"end")

        def search():
            try:
                
                if search_what.get()=="":
                    tkinter.messagebox.askretrycancel("Information","Your internet is not working please try agin",icon="info")

                else:
                    whether_key='43ee602cd3f013c1a0c2fa793155236e'
                    url='https://api.openweathermap.org/data/2.5/weather'
                    params={'APPID':whether_key,"q":search_what.get()}
                    response=requests.get(url,params=params)
                    whether=response.json()
                    #print("Name",whether['name'])
                    a=whether['weather'][0]['description']
                    #print(whether['main']['temp'])
                    #print(whether['main']['humidity'])
                    #print(whether['wind']['speed'])
                    #print(whether['sys']['country'])
                    #print(whether['timezone'])

                    clear()
                    TXT.insert("end","Name : ")
                    TXT.insert("end",whether['name'])
                    TXT.insert("end","\n")
                    TXT.insert("end","Whether description : ")
                    TXT.insert("end",a)
                    TXT.insert("end","\n")
                    TXT.insert("end","Temperature : ")
                    TXT.insert("end",whether['main']['temp'])
                    TXT.insert("end","\n")
                    TXT.insert("end","humidity : ")
                    TXT.insert("end",whether['main']['humidity'])
                    TXT.insert("end","\n")
                    TXT.insert("end","Wind Speed : ")
                    TXT.insert("end",whether['wind']['speed'])
                    TXT.insert("end","\n")
                    TXT.insert("end","Country : ")
                    TXT.insert("end",whether['sys']['country'])
                    TXT.insert("end","\n")
                    TXT.insert("end","Timezone : ")
                    TXT.insert("end",whether['timezone'])
            except:
                tkinter.messagebox.askretrycancel("Info","Somthing went wrong or network error")


                
    #=====================Frame=======================
        Main_Frame=Frame(self.root,width=500,height=300,relief="ridge",bd=3)
        Main_Frame.place(x=0,y=0)

        top_frame=Frame(Main_Frame,width=495,height=90,relief="ridge",bd=3)
        top_frame.place(x=0,y=0)

        Bottom_Frame=Frame(Main_Frame,width=495,height=205,relief="ridge",bd=3)
        Bottom_Frame.place(x=0,y=90)

        #============================================================
        lab_top=LabelFrame(top_frame,text="Search Whether",font=('times new roman',12,'bold'),width=490,height=85,bg="#db025f")
        lab_top.place(x=0,y=0)

        Ent_search=Entry(lab_top,font=('times new roman',14,'bold'),width=30,bd=2,textvariable=search_what)
        Ent_search.place(x=20,y=10)

        But_search=Button(lab_top,text="Search",font=('times new roman',11,'bold'),relief="ridge",bd=3,width=14,cursor="hand2",command=search)
        But_search.place(x=330,y=8)
        But_search.bind("<Enter>",on_enter1)
        But_search.bind("<Leave>",on_leave1)

        #===============================
        TXT=Text(Bottom_Frame,width=53,height=10,font=('times new roman',13,'bold'),bg="#afc5f8",bd=5)
        TXT.place(x=0,y=0)


if __name__ == "__main__":
    root=Tk()
    app=whether_app(root)
    root.mainloop()
