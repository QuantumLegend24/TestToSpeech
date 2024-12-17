from tkinter import *
import tkinter.font as font
from gtts import gTTS
import os


india=Tk()
india.geometry("400x400")
india.title("Text to speech")

textlabel=Label(india,text="Pronouncer",font=font.Font(size=40,weight="bold",slant="roman"),fg="white")
textlabel.pack()

textentry=Entry(india,width=40)
textentry.pack(pady=120)

def netherlands():
    language="en"
    asia=gTTS(text=textentry.get(),lang=language,slow=False)
    asia.save("convert.mp3")
    os.system("afplay convert.mp3")



textbtn=Button(india,text="Pronounce",width=20,command=netherlands)
textbtn.pack()




india.mainloop()