import urllib
import urllib.request
import re

QQregx=re.compile(r"[1-9]\d{4,10}",re.IGNORECASE)
for line in urllib.request.urlopen("http://bbs.tianya.cn/post-140-393974-1.shtml"):
    line=line.decode("utf-8")
    if line.find("QQ")!=-1 or line.find("qq")!=-1 or line.find("Qq")!=-1:
        mylist=QQregx.findall(line)
        if mylist:
            print(mylist)