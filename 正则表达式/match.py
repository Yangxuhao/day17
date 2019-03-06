import re
# print(re.match("abc","abc"))#match严格匹配从左边第一个开始匹配

'''
line="gaoqinghua is a boy not a girl"
matchobj = re.match(r"(.*)is(.*)",line)
print(matchobj)
print(matchobj.group(0))
'''
#match的两种风格
#预编译
pat=re.compile("(.*)is(.*)")
line="gaoqinghua is a boy not a girl"
matchobj=pat.match(line)
print(matchobj)
print(matchobj.group(0))
print(matchobj.group(1))
print(matchobj.group(2))
