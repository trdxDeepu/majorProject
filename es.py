import tkinter as tk
from tkinter import *
import speech_recognition as sr
from chatbot import Chatbot

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.chatlog = Text(self)
        self.chatlog.pack(side="top", fill="both", expand=True)

        self.entry = Entry(self)
        self.entry.pack(side="left", fill="both", expand=True)

        self.send_button = Button(self, text="Send", command=self.send_message)
        self.send_button.pack(side="right")

    def send_message(self):
        message = self.entry.get()
        response = chatbot.get_response(message)
        self.chatlog.insert(END, "You: " + message + "\n")
        self.chatlog.insert(END, "Bot: " + str(response) + "\n")
        self.entry.delete(0, END)

    def speech_recognition(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            try:
                message = r.recognize_google(audio)
                response = chatbot.get_response(message)
                self.chatlog.insert(END, "You: " + message + "\n")
                self.chatlog.insert(END, "Bot: " + str(response) + "\n")
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))

root = tk.Tk()
root.geometry("400x400")
app = Application(master=root)
chatbot = Chatbot(root)
app.mainloop()