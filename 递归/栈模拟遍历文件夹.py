import os
def getall(path,treeshow):
    mystack=[]
    mystack.append(path)

    while len(mystack)!=0:
        pathname=mystack.pop()
        filelist=os.listdir(path)
        for filename in filelist:
            filepath = os.path.join(path,filename)
            if os.path.isdir(filepath):
                print(treeshow+"文件夹",filename)
                treeshow+="     "
                getall(filepath,treeshow)
            else:
                print(treeshow+"文件",filename)

getall("E:\\movie","")