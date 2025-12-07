import tkinter as tk
from tkinter import ttk

from javabean_json_converter import JavaFrame  # 保留导入，实际暂未使用


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MermanUtils")
        self.geometry("600x400")
        self.resizable(False, False)

        # ---- icon ----
        photo = tk.PhotoImage(file='icon.png')
        self.iconphoto(False, photo)

        # ---- menu ----
        menubar = tk.Menu(self)
        file_menu = tk.Menu(menubar, tearoff=0)
        converter_menu = tk.Menu(file_menu, tearoff=0)

        menubar.add_cascade(label="Selection", menu=file_menu)
        file_menu.add_cascade(label="home", command=self.home_page)
        file_menu.add_cascade(label="jsonConverter", menu=converter_menu)
        file_menu.add_cascade(label="exit", command=self.quit)
        converter_menu.add_command(label="Java", command=self.show_java_page)

        self.config(bg="white", menu=menubar)

        # ---- main container ----
        container = tk.Frame(self, bg="white")
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (HomePage, JavaFrame):
            name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        # start default page
        self.show_frame("HomePage")

    # init and show the components
    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()
    def home_page(self):
        self.show_frame("HomePage")
    def show_java_page(self):
        self.show_frame("JavaFrame")

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="white")
        tk.Label(self, text="Wellcome to oldmerman's first project about Python!").pack(expand=True)

if __name__ == "__main__":
    App().mainloop()