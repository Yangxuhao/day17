import tkinter
import tkinter.ttk
import os

class TreeWindows:
    def __init__(self):
        self.win=tkinter.Tk()
        self.tree = tkinter.ttk.Treeview(self.win)
        self.tree.pack()
        self.ysb = tkinter.ttk.Scrollbar(self.win,orient="vertical",command=self.tree.yview())
        self.xsb = tkinter.ttk.Scrollbar(self.win,orient="horizontal",command=self.tree.xview())
        self.tree.configure(yscroll=self.ysb.set,xscroll=self.xsb.set)
        self.tree.grid(row=0,column=0)
        self.xsb.grid(row=1,column=0,sticky="ew")
        self.ysb.grid(row=0,column=1,sticky="ns")
        self.tree.grid()

        self.tree.heading("#0",text="Path",anchor="w")
        self.tree.bind("<<TreeviewSelect>>",self.gosel)
        filepath=r"E:\google"
        root=self.tree.insert("",'end',text=filepath,open=True)
        self.loadtree(root,filepath)

        self.e = tkinter.StringVar()
        self.entry=tkinter.Entry(self.win,textvariable=self.e)
        self.e.set("请选择文件")
        self.entry.grid(row=0,column=2)

    def show(self):
        self.win.mainloop()
    def gosel(self,event):
        self.select=event.widget.selection()
        for idx in self.select:
            print(self.tree.item(idx)["text"])
            self.e.set(self.tree.item(idx)["text"])
            #self.entry = tkinter.Entry(self.win, textvariable=idx["text"])

    def loadtree(self,parent,rootpath):
        for path in os.listdir(rootpath):
            abspath = os.path.join(rootpath,path)
            oid = self.tree.insert(parent,'end',text=path,open=True)
            if os.path.isdir(abspath):
                #print("文件夹",abspath)
                self.loadtree(oid,abspath)

treeview = TreeWindows()
treeview.show()