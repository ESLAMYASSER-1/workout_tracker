#work out app 
import tkinter as tk 
import customtkinter as ctk
from tkcalendar import DateEntry
import mysql.connector
import datetime
from PIL import ImageTk, Image

def CREATEdb():
    conn= mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="engeslam@8505611.mysql"
    )
    mycursor=conn.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS Workout;")
CREATEdb()
conn= mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="engeslam@8505611.mysql",
    database="Workout"
)
mycursor=conn.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS Exersices (Exersice_id int PRIMARY KEY AUTO_INCREMENT, Exersice_name VARCHAR(255) UNIQUE);INSERT INTO Exersices(Exersice_name) VALUES('Squats'),('Lunges'),('Push-ups'),('Pull-ups'),('Plank'),('Burpees');CREATE TABLE IF NOT EXISTS _History (Day_id int PRIMARY KEY AUTO_INCREMENT,Day_Exersices VARCHAR(255),Day_Date DATE);",multi=True)
conn.commit()

root = tk.Tk()
root.geometry("1000x800")


class Exercises:
    
    def __init__(self):
        self.today=datetime.date.today()
        self.mainFrame=tk.Frame(root,width=1000,height=800,bg="#FF8C00")
        self.mainFrame.pack()
        self.mainFrame.pack_propagate(0)


        self.MainTitle=tk.Label(self.mainFrame,text="FlexiFit",font="Helvatica 30 bold",justify="center",fg="black",bg="#FFA500")
        self.MainTitle.pack(pady=10)
        def showhistory():
            for x in root.winfo_children():
                x.destroy()
            ShowExercises()
        self.showHistory=tk.Button(self.mainFrame,text="Show History",font="Verdana 15 bold",command=showhistory)
        self.showHistory.place(x=800,y=40)


        self.innerFrame1=tk.Frame(self.mainFrame,width=1000,height=299,bg="black")
        self.innerFrame1.pack(pady=(30,0))
        self.innerFrame1.pack_propagate(0)

        self.innerFrame2=tk.Frame(self.mainFrame,width=1000,height=299,bg="black")
        self.innerFrame2.pack()#pady=(375,0)
        self.innerFrame2.pack_propagate(0)

        savebtn = tk.Button(self.mainFrame,text="SAVE",font="Arial 15 bold",command=self.save).place(x=900,y=720)
        datelbl=tk.Label(self.mainFrame,text="Date:",font="Cuntry 20 bold",bg="#FF8C00").place(x=50,y=725)
        date_lbl= tk.Label(self.mainFrame,text=self.today,font="Cuntry 20 bold",bg="#FF8C00").place(x=130,y=725)

        self.AddFrames()
    def save(self):
        
        arr = [self.innerFrame1,self.innerFrame2]
        values=[]
        self.exercises=[]
        for f in arr:
            frames=f.winfo_children()
            for x in frames:
                for check in x.winfo_children():
                    try:
                        values.append(check.get())
                    except:
                        pass
        for i in range(6):
            if i==0 and values[i]==1:
                self.exercises.append("Burpees")
            elif i==1 and values[i]==1:
                self.exercises.append("Lunges")
            elif i==2 and values[i]==1:
                self.exercises.append("Plank")
            elif i==3 and values[i]==1:
                self.exercises.append("Pull-ups")
            elif i==4 and values[i]==1:
                self.exercises.append("Push-ups")
            elif i==5 and values[i]==1:
                self.exercises.append("Squats")
        sqlstatement1="DELETE FROM _history WHERE Day_Date ='%s'"%self.today
        mycursor.execute(sqlstatement1)
        conn.commit()
        for ex in self.exercises:
            sqlstatement2="INSERT INTO _history(Day_Exersices,Day_Date) values('%s','%s') "%(ex,self.today)
            mycursor.execute(sqlstatement2)
            conn.commit()
    def AddFrames(self):
        mycursor.execute("SELECT Exersice_name FROM Exersices;")
        Exercises =mycursor.fetchall()
        for ex in Exercises:
            if ex[0]=="Burpees":
                Exersice_image="res\-burpees-exercise-illustration.jpg"
            elif ex[0]=="Lunges":
                Exersice_image="res\Lunges.png"
            elif ex[0]=="Plank":
                Exersice_image="res\plank-exercise-illustration.jpg"
            elif ex[0]=="Pull-ups":
                Exersice_image="res\pullup.jpg"
            elif ex[0]=="Squats":
                Exersice_image="res\squat-exercise-illustration.jpg"
            elif ex[0]=='Push-ups':
                Exersice_image="res\push-up-exercise-illustration.jpg"
            else:
                Exersice_image="res\imageburpees.gif"
            
            
            img = Image.open(Exersice_image)
            img=img.resize((250,250))
            photo=ImageTk.PhotoImage(img)

            self.toFrame=self.innerFrame1
            if len(self.innerFrame1.winfo_children())>2:
                self.toFrame=self.innerFrame2
            
            self.frame=tk.Frame(self.toFrame,width=300,height=100,bg="#FFA500")
            self.frame.pack(fill=tk.BOTH, side=tk.LEFT,padx=17,pady=(5,0))
            self.frame.pack_propagate(0)
            
            self.label=tk.Label(self.frame,image=photo)
            self.label.pack(expand=True)
            self.check = ctk.CTkCheckBox(self.frame)
            self.check.pack()
            self.check.photo=photo
class ShowExercises:
    
    def __init__(self):
        self.today=datetime.date.today()
        self.mainFrame=tk.Frame(root,width=1000,height=800,bg="#FFC04D")
        self.mainFrame.pack()
        self.mainFrame.pack_propagate(0)


        self.MainTitle=tk.Label(self.mainFrame,text="FlexiFit",font="Helvatica 30 bold",justify="center",fg="black")
        self.MainTitle.pack(pady=10)


        self.innerFrame1=tk.Frame(self.mainFrame,width=1000,height=299,bg="black")
        self.innerFrame1.pack(pady=(110,0))
        self.innerFrame1.pack_propagate(0)

        self.innerFrame2=tk.Frame(self.mainFrame,width=1000,height=299,bg="black")
        self.innerFrame2.pack()#pady=(375,0)
        self.innerFrame2.pack_propagate(0)

        def back():
            for x in root.winfo_children():
                x.destroy()
            Exercises()
        self.backbtn = tk.Button(self.mainFrame,text="<",font="Cuntry 20 bold",relief="flat",command=back).place(x=40,y=40)
        self.history=DateEntry(self.mainFrame,date_pattern='yyyy-MM-dd',width=15,font="Arial 15 bold")
        self.history.place(x=800,y=30)
        def x():
            for x in self.innerFrame1.winfo_children():
                x.destroy()
            for x in self.innerFrame2.winfo_children():
                x.destroy()
            self.AddFrames(self.history.get_date())
        self.showbtn = tk.Button(self.mainFrame,text="SHOW",font="Arial 15 bold",command=lambda:x())
        self.showbtn.place(x=830,y=110)
        
    def AddFrames(self,day):
        slqstatement="SELECT Day_Exersices FROM _history WHERE Day_Date='%s';"%day
        mycursor.execute(slqstatement)
        Exercises =mycursor.fetchall()
        for ex in Exercises:
            if ex[0]=="Burpees":
                Exersice_image="res\-burpees-exercise-illustration.jpg"
            elif ex[0]=="Lunges":
                Exersice_image="res\Lunges.png"
            elif ex[0]=="Plank":
                Exersice_image="res\plank-exercise-illustration.jpg"
            elif ex[0]=="Pull-ups":
                Exersice_image="res\pullup.jpg"
            elif ex[0]=="Squats":
                Exersice_image="res\squat-exercise-illustration.jpg"
            elif ex[0]=='Push-ups':
                Exersice_image="res\push-up-exercise-illustration.jpg"
            else:
                Exersice_image="res\imageburpees.gif"
            
            
            img = Image.open(Exersice_image)
            img=img.resize((250,250))
            photo=ImageTk.PhotoImage(img)

            self.toFrame=self.innerFrame1
            if len(self.innerFrame1.winfo_children())>2:
                self.toFrame=self.innerFrame2
            
            self.frame=tk.Frame(self.toFrame,width=300,height=100,bg="#FFA500")
            self.frame.pack(fill=tk.BOTH, side=tk.LEFT,padx=17,pady=(5,0))
            self.frame.pack_propagate(0)
            
            self.label=tk.Label(self.frame,image=photo)
            self.label.pack(expand=True)
            self.check = ctk.CTkCheckBox(self.frame)
            self.check.pack()
            self.check.photo=photo

Exercises()
root.mainloop()