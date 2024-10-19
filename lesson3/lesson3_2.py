from ttkthemes import ThemedTk
from tkinter import ttk

class Window(ThemedTk):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("這是第一個視窗")
        self.geometry("600x400")
        btn1 = ttk.Button(self,text='按鈕1',command=self.user_click1)
        btn1.pack()

        btn2 = ttk.Button(self,text='按鈕2',command=self.user_click2)
        btn2.pack()

        btn3 = ttk.Button(self,text='按鈕3',command=self.user_click3)
        btn3.pack()

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
    