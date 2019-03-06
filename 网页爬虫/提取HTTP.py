import urllib
import urllib.request
import re

httpregx=re.compile(r"(http://\S*?)[\"|\)]",re.IGNORECASE)
for line in urllib.request.urlopen("http://bbs.tianya.cn/post-140-393974-2.shtml"):
    mylist=httpregx.findall(line.decode("utf-8"))
    if mylist:
        print(mylist)