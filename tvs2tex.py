# -*- encording: utf8-*-
import tkinter as tk

class Application(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master.title('tvs2tex')
        self.master.geometry('1000x500')
        # caption の入力
        captitle = tk.Label(self, text=u'表タイトル')
        captitle.grid(row=0, column=0)
        capbox = tk.Entry(self, width=30)
        capbox.grid(row=0, column=1, padx=10, pady=10)

        # label の入力
        labtitle = tk.Label(self, text=u'ラベル')
        labtitle.grid(row=1, column=0)
        labbox = tk.Entry(self, width=30)
        labbox.grid(row=1, column=1)

        # 表の入力
        intitle = tk.Label(self, text='入力')
        intitle.grid(row=2, column=0, padx=10, pady=20, sticky=tk.W)


        # 表の出力
        outtitle = tk.Label(self, text='出力')
        outtitle.grid(row=2, column=3, padx=30, pady=20, sticky=tk.E)




if __name__=='__main__':
    f = Application()
    f.pack()
    f.mainloop()
