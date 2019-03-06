import urllib
import urllib.request

# mystr=urllib.request.urlopen("http://www.baidu.com").read()
# print(mystr.decode("utf-8"))

for line in urllib.request.urlopen("http://www.baidu.com"):
    print(line.decode("utf-8"),end="")