f=open('jan13.txt','r')
text=f.read()
total=0
tot_a=0
sent=""
for char in text:
    if char==".":
        if len(sent)>0:
            total+=1
            i=0
            while i<len(sent) and (sent[i]==' ' or sent[i]=='\n'):
                i+=1
            if i<len(sent) and sent[i]=="A":
                tot_a+=1
        sent=""
    else:
        sent+=char
if len(sent)>0:
    total+=1
    i=0
    while i < len(sent) and (sent[i] == ' ' or sent[i] == '\n'):
        i += 1
    if i<len(sent) and sent[i]=='A':
        tot_a+=1
print("total sentence",total)
print("start with a",tot_a)



