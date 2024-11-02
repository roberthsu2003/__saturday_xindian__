from ttkthemes import ThemedTk
from tkinter import ttk

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
        topFrame.pack(expand=True,fill='both',padx=10,pady=30)

        bottomFrame = ttk.Frame(self)
        bottomFrame.pack()



def main():
    window = Window(theme="arc")
    window.mainloop()

if __name__ == '__main__':
    main()
    