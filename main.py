from tkinter import *
import pyttsx3

engine= pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
rate = engine.getProperty('rate')

def speak(audio):
    engine.say(audio)
    engine.setProperty('rate', rate-0.50)
    engine.runAndWait()
if __name__ == '__main__':
    speak("what do u want to be said, please write")
    root = Tk()
    root.geometry("243x153")
    def Zira():
        engine.setProperty('voice', voices[1].id)
    def David():
        engine.setProperty('voice', voices[0].id)

    def Speak():
        speak(arevalue.get())
    arevalue=StringVar()
    areEnter = Entry(root,bd=8, textvariable=arevalue).grid(row=0, column=1)
    are = Label(root,pady=10,bd=8,text="Write:").grid(row=0, column=0)

    Button(root,padx=10,bd=8,text="Speak", command=Speak).grid(row=1, column=1)

    r = Radiobutton(root, text="Friday", command=Zira, value=2).grid(row=2, column=0)
    r = Radiobutton(root, text="Jarvis", command=David, value=1).grid(row=3, column=0)

    root.mainloop()
