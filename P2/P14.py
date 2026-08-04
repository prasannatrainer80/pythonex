from gc import enable


def keyargs(**kwargs):
    print(kwargs)

keyargs(eid=100,ename="Sindhu",salary=88234.22)
keyargs(eid=101,ename="Jashwanth",status=True,salary=88234.22,dept="Dotnet")