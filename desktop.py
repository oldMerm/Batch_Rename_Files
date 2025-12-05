from tkinter import *
import tkinter.ttk

import batch_rename_file as brf

if __name__ == "__main__":
    root = Tk()
    root.title("MermanUtils")
    root.geometry("400x300")
    root.config(bg="white")
    photo = tkinter.PhotoImage(file='icon.png')
    root.iconphoto(False, photo)

    lab1 = Label(root, text="Selection Tools", bg="white", font=("black", 15), width=20, height=1)
    lab1.pack()

    combobox = tkinter.ttk.Combobox()
    combobox.pack()

    combobox['value'] = "batch_rename_file"
    combobox.current(0)

    def on_combobox_select(event):
        option = combobox.get()
        if option == brf.product_name :
            pass # logic in future

    combobox.bind("<<ComboboxSelected>>",on_combobox_select)

    root.mainloop()