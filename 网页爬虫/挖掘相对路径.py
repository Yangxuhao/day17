import urllib.request
import urllib
import re

def getdata(url):
    try:
        data=urllib.request.urlopen(url).read().decode("utf-8")
        return data
    except:
        return ""

def getemail(data):
    maileregx = re.compile("([A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4})", re.IGNORECASE)
    try:
        mylist = maileregx.findall(data)
        return mylist
    except:
        return []
def gethttp(data):
    httpregx = re.compile(r"(http://\S*?)[\"|\)]", re.IGNORECASE)
    try:
        mylist = httpregx.findall(data)
        return mylist
    except:
        return []

def getabsUrl(url,data):#相对路径
    try:
        listUrl=[]
        regex=re.compile("href=\"(.*?)\"",re.IGNORECASE)
        httplist=regex.findall(data)
        newhttplist=httplist.copy()
        hostname=gethostname(url)
        for data in newhttplist:
            if data.find("http://")!=-1:
                httplist.remove(data)
            elif data.find("javascript")!=-1:
                httplist.remove(data)
        if hostname!=None:
            for i in range(len(httplist)):
                httplist[i]=hostname+httplist[i]
        return httplist
    except:
        return []
def gethostname(httpstr):
    httpregx = re.compile(r"(http://\S*?)/", re.IGNORECASE)
    try:
        mylist = httpregx.findall(httpstr)
        if len(mylist)==0:
            return none
        else:
            return mylist[0]
    except:
        return []
def getallUrl(data):
    mylist = gethttp(pagedata)
    mylist2 = getabsUrl(mylist[0],pagedata)
    alllist=[]
    alllist.extend(mylist)
    alllist.extend(mylist2)
    return alllist
pagedata=getdata("http://bbs.tianya.cn/post-140-393974-2.shtml")
# mylist=gethttp(pagedata)
# # hostname=gethostname(mylist[0])
# # print("hostname",hostname)
# print("path",getabsUrl(mylist[0],pagedata))
print(getallUrl(pagedata))