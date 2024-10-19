from ttkthemes import ThemedTk
from tkinter import ttk

class Window(ThemedTk):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("這是第一個視窗")
        self.geometry("600x400")

        style = ttk.Style(self)
        
        #style.configure('TLabel',font=('Ariel', 30),foreground='red') #修改內建的TLabel
        style.configure('Title.TLabel',font=('Ariel', 30),foreground='blue') #自訂的TLabel style


        label = ttk.Label(self,text='Hello! Tkinter!',style='Title.TLabel')
        label.pack()



def main():
    window = Window(theme="arc")
    window.mainloop()

if __name__ == '__main__':
    main()
    