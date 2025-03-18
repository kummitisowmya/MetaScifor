f=open("second.txt","r")
lnum=1
for line in f:
    num=False
    for char in line:
        if char.isdigit():
            num=True
            break
    if num:
        print(f"line:{lnum}")
    lnum+=1
