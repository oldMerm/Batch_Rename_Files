import tkinter as tk
from tkinter import messagebox

class JavaFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="white")
        tk.Label(self,text="input").place(x=10,y=0)
        self.j_text1 = tk.Text(self, width=30, height=20)
        self.j_text1.place(x=10, y=20, anchor="nw")
        tk.Label(self,text="output").place(x=300,y=0)
        self.j_text2 = tk.Text(self, width=30, height=20)
        self.j_text2.place(x=300, y=20, anchor="nw")
        self.j_btn = tk.Button(self, text="converter", width=10, height=2, command=self.converter_j)
        self.j_btn.place(x=10, y=300)

    # ---- 空函数，逻辑不变 ----
    def converter_j(self):
        cont = self.j_text1.get('1.0', 'end-1c')
        s = convert(cont)
        if s is None:
            tk.messagebox.showinfo("Error","javabean format failed")
            return
        self.j_text2.delete('1.0', 'end')
        self.j_text2.insert('1.0', s)

def convert(lines):
    # print("Please paste the original data (Ctrl+D end to input):")
    # try:
    #     lines = sys.stdin.read()
    # except KeyboardInterrupt:
    #     print("\nCancelled.")
    #     return None
    str_list = [item.strip() for item in lines.strip().replace("\n", "").split(";") if item]
    res_list = []
    for i in str_list:
        s = i.strip().split()
        if len(s) < 2:
            return None
        key = s[-1]
        if "Id" in key or "Type" in key:
            val = 1
        elif "List" in key:
            val = "[]"
        else:
            val = '"object String"'
        res_list.append(f'"{key}": {val}')

    return "{\n" + ",\n".join(res_list) + "\n}" if res_list else None