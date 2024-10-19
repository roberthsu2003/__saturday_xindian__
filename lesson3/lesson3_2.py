from ttkthemes import ThemedTk
from tkinter import ttk

class Window(ThemedTk):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("這是第一個視窗")
        self.geometry("600x400")
        style = ttk.Style(self)
        style.configure('TButton',font=('Ariel',15))

        btn1 = ttk.Button(self,text='按鈕1',command=self.user_click1)
        btn1.pack(ipadx=20,ipady=10,pady=10,side='left')

        btn2 = ttk.Button(self,text='按鈕2',command=self.user_click2)
        btn2.pack(ipadx=20,ipady=10,side='left')

        btn3 = ttk.Button(self,text='按鈕3',command=self.user_click3)
        btn3.pack(ipadx=20,ipady=10,pady=10,side='left')

    def user_click1(self):
        print('使用者按下按鈕1')

    def user_click2(self):
        print('使用者按下按鈕2')

    def user_click3(self):
        print('使用者按下按鈕3')



def main():
    window = Window(theme="arc")
    window.mainloop()

if __name__ == '__main__':
    main()
    