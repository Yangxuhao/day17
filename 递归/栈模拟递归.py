
mystack=[]
mystack.append(5)
while len(mystack)!=0:
    data=mystack.pop()
    print(data)
    if data==0:
        break
    else:

        mystack.append(data-1)
