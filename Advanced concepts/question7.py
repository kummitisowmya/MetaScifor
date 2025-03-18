f=open("seven.txt","r")
f1=f.read()
words=f1.split()
clear=[words[0]]
for i in range(1,len(words)):
    if words[i]!=words[i-1]:
        clear.append(words[i])
clear=" ".join(clear)
f=open("seven.txt","w")
f.write(clear)
print("duplicates removed")
