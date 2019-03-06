import os
from collections import deque

path=r"E:\movie"
queue=deque([])
queue.append(path)

while len(queue)!=0:
    path=queue.popleft()
    filelist=os.listdir(path)
    for filename in filelist:
        filepath=os.path.join(path,filename)
        if os.path.isdir(filepath):
            print("文件夹", filename)
            queue.append(filepath)

        else:
            print("文件", filename)