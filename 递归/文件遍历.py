import os

def getall(path,treeshow):
    filelist = os.listdir(path)
    for filename in filelist:
        filepath=os.path.join(path,filename)
        if os.path.isdir(filepath):
            print(treeshow,"文件夹"+filename)
            treeshow += "  "
            getall(filepath,treeshow)
        else:
            print(treeshow,"文件"+filename)

getall(r"D:\尹成python","")