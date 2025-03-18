f=open("python.txt","r")
f1=open("fourth.txt","w")
num=1
for line in f:
    f1.write(f"{num}:{line}")
    num+=1
print("serial numbers added")