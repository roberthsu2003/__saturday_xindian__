from ttkthemes import ThemedTk
from tkinter import ttk,messagebox
import tkinter as tk


class Window(ThemedTk):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("這是第一個視窗")
        #self.geometry("600x400")

        style = ttk.Style(self)
        
        style.configure('TLabel',font=('Ariel', 30),foreground='red') #修改內建的TLabel
        style.configure('Title.TLabel',font=('Ariel', 30),foreground='#000000') #自訂的TLabel style


        
        topFrame = ttk.Frame(self,borderwidth=2,relief='groove')
        title_label = ttk.Label(topFrame,text='全台空氣品質AQI',style='Title.TLabel')
        title_label.pack(pady=50,padx=20)
        topFrame.pack(expand=True,fill='x',padx=10,pady=30)

        middleFrame = ttk.Frame(self,borderwidth=2,relief='groove',padding=[10,10,10,10])
        left_btn = ttk.Button(middleFrame,text="左按鈕",command=self.click_left_button)
        left_btn.pack(side='left',expand=True,fill='x')
        right_btn = ttk.Button(middleFrame,text="右按鈕",command=self.click_right_button)
        right_btn.pack(side='right',expand=True,fill='x')
        middleFrame.pack(expand=True,fill='x',padx=10,pady=(0,30))

        bottomFrame = ttk.Frame(self,borderwidth=2,relief='groove',padding=[10,10,10,10])
        self.selectedVar = tk.StringVar()
        self.selectedVar.set('value 1')
        self.selectedVar.trace_add('write',self.on_radio_select)

        r1 = ttk.Radiobutton(bottomFrame,text='option 1', value='value 1',variable=self.selectedVar)
        r1.pack(side='left')

        r2 = ttk.Radiobutton(bottomFrame,text='option 2', value='value 2',variable=self.selectedVar)
        r2.pack(side='left')

        r3 = ttk.Radiobutton(bottomFrame,text='option 3', value='value 3',variable=self.selectedVar)
        r3.pack(side='left')
        
        bottomFrame.pack(expand=True,fill='x',padx=10,pady=(0,30))

        bottomFrame1 = ttk.Frame(self,borderwidth=2,relief='groove',padding=[10,10,10,10])
        self.aggrement = tk.StringVar()
        ttk.Checkbutton(bottomFrame1,
                        text='我同意',
                        variable=self.aggrement,
                        command=self.aggrement_change,
                        onvalue='我同意',
                        offvalue='我不同意').pack(side='right')      
        bottomFrame1.pack(expand=True,fill='x',padx=10,pady=(0,30))
        
        bottomFrame2 = ttk.Frame(self,borderwidth=2,relief='groove',padding=[10,10,10,10])
        self.day_selected = tk.StringVar()
        combobox = ttk.Combobox(bottomFrame2,
                                textvariable=self.day_selected,
                                values=['day1','day2','day3','day4','day5'],
                                state='readonly')        
        combobox.set('請選擇1天')
        combobox.bind('<<ComboboxSelected>>',self.day_changed)
        combobox.pack()
             
        bottomFrame2.pack(expand=True,fill='x',padx=10,pady=(0,30))

    def click_left_button(self):
        messagebox.showinfo("資訊","按左按鈕")

    def click_right_button(self):
        answer = messagebox.askyesno('是否要關機','三思')
        if answer:
            print("要關機")
            self.quit()

    def on_radio_select(self,*args):
       print(self.selectedVar.get())

    def aggrement_change(self):
        print(self.aggrement.get())

    def day_changed(self,event):
        print(self.day_selected.get())
         
        

def main():
    window = Window(theme="arc")
    window.mainloop()

if __name__ == '__main__':
    main()
    