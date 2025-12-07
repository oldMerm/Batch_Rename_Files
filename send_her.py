import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("无聊的创作")
root.geometry("300x150")
root.resizable(False, False)

label = tk.Label(root,text="可以和我聊会天吗？")
label.pack(pady = 20)

btn_bar = tk.Frame(root)
btn_bar.pack()

def ok():
    res = tk.messagebox.showinfo("good", "希望有个愉快的旅程")
    root.quit()

def refuse():
    while True:
        res = tk.messagebox.askyesno("Are you sure? 0_o", '点击"否"以重新斟酌😀')
        if not res:
            break


tk.Button(btn_bar, text="同意",  width=18, command=ok).pack(side='left',  padx=15)
tk.Button(btn_bar, text="拒绝",  width=3, command=refuse).pack(side='left',  padx=15)

root.mainloop()