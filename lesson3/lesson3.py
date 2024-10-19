import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title("這是第一個視窗")
        self.geometry("600x400")

        style = ttk.Style(self)
        
        #style.configure('TLabel',font=('Ariel', 30),foreground='red') #修改內建的TLabel
        style.configure('Title.TLabel',font=('Ariel', 30),foreground='blue') #自訂的TLabel style


        label = ttk.Label(self,text='Hello! Tkinter!',style='Title.TLabel')
        label.pack()



def main():
    window = Window()
    window.mainloop()

if __name__ == '__main__':
    main()
    