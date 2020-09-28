
#initialised all the required modules for this project

from tkinter import  Label,Frame,Button,Text,StringVar,Tk,Entry,LabelFrame
import tkinter.messagebox
import requests




class Whether:
    def __init__(self,root):
        
        self.root=root
        self.root.title("Whether App")
        self.root.geometry("500x300")
        self.root.resizable(0,0)
        self.root.iconbitmap("whether.ico")


        #textvariable for tkinter moduel which is used in entry    
        search_what=StringVar()

        



    #====================================================


        #this button is providing styling to given button when ever you hover on it 
        def on_enter1(e):
            But_search['background']="black"
            But_search['foreground']="cyan"
        def on_leave1(e):
            But_search['background']="SystemButtonFace"
            But_search['foreground']="SystemButtonText"

            

        #this will clear the text from textbox
        def clear():
            TXT.delete('1.0',"end")


            
         #this methods/function will provide us all data /by clicking on it
        def search():
            try:
                
                if search_what.get()=="":
                    tkinter.messagebox.askretrycancel("Information","Your internet is not working please try agin",icon="info")
                else:
                    whether_key='43ee602cd3f013c1a0c2fa793155236e'   #api key
                    url='https://api.openweathermap.org/data/2.5/weather'    #url of website
                    params={'APPID':whether_key,"q":search_what.get()}     #paramst whith api key and qurey what to search 
                    response=requests.get(url,params=params)                   #using request library we will extract all the given information 
                    whether=response.json()                                                 #and convert the inforamtion in json format
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

        #intial frame
        Main_Frame=Frame(self.root,width=500,height=300,relief="ridge",bd=3)
        Main_Frame.place(x=0,y=0)

        
        #top frame
        top_frame=Frame(Main_Frame,width=495,height=90,relief="ridge",bd=3)
        top_frame.place(x=0,y=0)

        
         #bottom frame
        Bottom_Frame=Frame(Main_Frame,width=495,height=205,relief="ridge",bd=3)
        Bottom_Frame.place(x=0,y=90)
        

        #====================Top-Frame========================================

        #search label city   
        lab_top=LabelFrame(top_frame,text="Search Whether",font=('times new roman',12,'bold'),width=490,height=85,bg="#db025f")
        lab_top.place(x=0,y=0)

        
        #search entry to write city name
        Ent_search=Entry(lab_top,font=('times new roman',14,'bold'),width=30,bd=2,textvariable=search_what)
        Ent_search.place(x=20,y=10)


        
        #search funtion will execute by clicking this button
        But_search=Button(lab_top,text="Search",font=('times new roman',11,'bold'),relief="ridge",bd=3,width=14,cursor="hand2",command=search)
        But_search.place(x=330,y=8)
        But_search.bind("<Enter>",on_enter1)
        But_search.bind("<Leave>",on_leave1)

        #=============Bottom_frame==================
        #textbox in bottom frame to provide the information about given whether
        TXT=Text(Bottom_Frame,width=53,height=10,font=('times new roman',13,'bold'),bg="#afc5f8",bd=5)
        TXT.place(x=0,y=0)


if __name__ == "__main__":
    root=Tk()
    app=Whether(root)
    root.mainloop()




