import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from controller import *
import tkinter.messagebox

class Aplication:
    def __init__(self):
        self.window = tk.Tk()
        self.obj = PasswordController()
        self.random_password = tk.StringVar()
        self.selected = tk.StringVar()
        self.labelvar = tk.StringVar()

        #WINDOWS SETTINGS
        self.window.title("PASSWORD GENERATOR")
        self.window.geometry("550x340+675+300") #DIMENSIONS AND POSITION OF THE WINDOW IN THE SCREEN (X, Y)
        self.window.resizable(0, 0) #MAKE THE WINDOW UNRESIZABLE
        self.window.iconbitmap("./images/lock.ico") #WINDOW ICON

        #DRAW A LINE
        self.canvas = Canvas(self.window, width = 520, height = 30)
        self.canvas.place(x = 15, y = 35)
        self.canvas.create_line(0, 25, 520, 25, fill = 'black')

        #CREATE A STANDARD STYLE FOR TITLES
        self.t_style = ttk.Style()
        self.t_style.configure("BW.TLabel", foreground="black", font=("Helvetica", 24))
        #CREATE A STANDARD STYLE FOR SUBTITLES
        self.s_style = ttk.Style()
        self.s_style.configure("WB.TLabel", foreground="black", font=("Helvetica", 14))
        #SPECIAL STYLE
        self.sp_style = ttk.Style()
        self.sp_style.configure("GB.TLabel", foreground="green", font=("Helvetica", 16))
        
        #TEXT LABELS
        self.label1 = ttk.Label(self.window, text="Password Generator", style="BW.TLabel").place(x = 140, y = 10)
        self.label2 = ttk.Label(self.window, text="Length:", style="WB.TLabel").place(x = 20, y = 80)

        self.label3 = ttk.Label(self.window, textvariable=self.labelvar, style="GB.TLabel").place(x = 350, y = 260)

        #RADIO BUTTONS
        self.rdbtn1 = ttk.Radiobutton(self.window, text="Short", variable=self.selected, value="0").place(x = 100, y = 120)
        self.rdbtn2 = ttk.Radiobutton(self.window, text="Medium", variable=self.selected, value="1").place(x = 185, y = 120)
        self.rdbtn3 = ttk.Radiobutton(self.window, text="Large", variable=self.selected, value="2").place(x = 285, y = 120)
        self.rdbtn4 = ttk.Radiobutton(self.window, text="Extra Large", variable=self.selected, value="3").place(x = 370, y = 120)

        #TEXTBOX
        self.txtbox = ttk.Entry(self.window, textvariable = self.random_password, state = "disable", justify = "center", font = ("Argentum Sans", 24)).place(x = 90, y = 180)

        #BUTTONS -> generate FUNCTION & copy FUNCTION
        self.btn1 = ttk.Button(text = "Copy", command = self.copy).place(x = 237, y = 240)
        self.btn2 = ttk.Button(text = "Generate", command = self.generate).place(x = 237, y = 280)

        self.window.mainloop()

    def generate(self):
        try:
            self.labelvar.set("")
            self.random_password.set("")
            value = int(self.selected.get())
            self.random_password.set(self.obj.process_password(value))
        except:
            tkinter.messagebox.showwarning("Error", "Select a length")

    def copy(self):
        if self.random_password.get() != "":
            self.window.clipboard_clear()
            self.window.clipboard_append(self.random_password.get())
            self.labelvar.set("Copied!")
        else:
            tkinter.messagebox.showwarning("Error", "Generate a password first")

if __name__ == "__main__": 
    Aplication = Aplication()