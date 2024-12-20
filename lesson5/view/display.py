from tkinter.simpledialog import Dialog
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

class CustomDialog(Dialog):
    def __init__(self, parent, title=None,youbikes=[]):
        
        self.youbikes = youbikes
        super().__init__(parent, title)
        

    def body(self, master):
        # 創建對話框主體。返回應具有初始焦點的控件。
        # define columns
        

        columns = ('sna', 'mday', 'total','rent','return')

        tree = ttk.Treeview(master, columns=columns, show='headings')

        # define headings
        tree.heading('sna', text='站點')
        tree.heading('mday', text='日期')
        tree.heading('total', text='總車輛數')
        tree.heading('rent', text='可借')
        tree.heading('return', text='可還')

        # generate sample data
        

        # add data to the treeview
        for site in self.youbikes:
            tree.insert('', tk.END, values=(site['sna'],site['mday'],site['total'],site['available_rent_bikes'],site['available_return_bikes']))


        def item_selected(event):
            for selected_item in tree.selection():
                item = tree.item(selected_item)
                record = item['values']
                # show a message
                showinfo(title='Information', message=','.join(record))


        tree.bind('<<TreeviewSelect>>', item_selected)

        tree.pack(side='left')

        # add a scrollbar
        scrollbar = ttk.Scrollbar(master, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side='left',fill='y')
        

    def apply(self):
        # 當用戶按下確定時處理數據
        #self.result = self.name_entry.get()
        pass
        
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