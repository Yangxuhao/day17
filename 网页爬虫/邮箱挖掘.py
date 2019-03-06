import urllib
import urllib.request
import re

maileregx=re.compile("([A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4})",re.IGNORECASE)
for line in urllib.request.urlopen("http://bbs.tianya.cn/post-140-393974-2.shtml"):
    mylist=maileregx.findall(line.decode("utf-8"))
    if mylist:
        print(mylist)