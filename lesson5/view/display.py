from tkinter.simpledialog import Dialog
import tkinter as tk

class CustomDialog(Dialog):
    def __init__(self, parent, title=None):
        print("abc")
        super().__init__(parent, title)
        

    def body(self, master):
        # 創建對話框主體。返回應具有初始焦點的控件。
        tk.Label(master, text="請輸入你的名字:").grid(row=0)
        self.name_entry = tk.Entry(master)
        self.name_entry.grid(row=0, column=1)
        return self.name_entry

    def apply(self):
        # 當用戶按下確定時處理數據
        self.result = self.name_entry.get()
        
    def buttonbox(self):
        # Add custom buttons (overriding the default buttonbox)
        box = tk.Frame(self)
        self.ok_button = tk.Button(box, text="確定", width=10, command=self.ok)
        self.ok_button.pack(padx=5, pady=5)
        self.bind("<Return>", self.ok)
        box.pack()

    def ok(self, event=None):
        # Override the ok method
        print("OK button was clicked!")
        super().ok()