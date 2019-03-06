import tkinter
import tkinter.ttk
import os
import 网页爬虫.BFS_class

class TreeWindows:
    def __init__(self):
        self.win=tkinter.Tk()
        self.win.geometry("500x500")


        self.e=tkinter.StringVar()
        self.entry=tkinter.Entry(self.win,width=50,textvariable=self.e)
        self.e.set("请输入网址")

        self.button=tkinter.Button(self.win,text="搜索",width=10,command=self.getdata)
        self.entry.grid(row=0,column=0)
        self.button.grid(row=0,column=1)

    def show(self):
        self.win.mainloop()
    def getdata(self):

        urlstr = self.e.get()
        print(urlstr)
        if urlstr!="":
            data=网页爬虫.BFS_class.BFS(urlstr)
            print(data)


treeview = TreeWindows()
treeview.show()