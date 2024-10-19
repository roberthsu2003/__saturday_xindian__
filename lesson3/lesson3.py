import tkinter as tk

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title("這是第一個視窗")
        self.geometry("600x400")



def main():
    window = Window()
    window.mainloop()

if __name__ == '__main__':
    main()
    