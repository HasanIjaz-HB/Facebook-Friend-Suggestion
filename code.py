usid=input("Enter a user id to suggest some friends: ")
file=open("friendship.txt","r")
content=file.readlines()
file.close()
userd={}

for line in content:
    if line:
        usrid=line.split('\t')[0].strip()
        if usrid in userd:
            userd[usrid]+=[line.split('\t')[1].strip()]
        else:
            userd[usrid]=[line.split('\t')[1].strip()]
    if line:
        usrid=line.split('\t')[1].strip()
        if usrid in userd:
            userd[usrid]+=[line.split('\t')[0].strip()]
        else:
            userd[usrid]=[line.split('\t')[0].strip()]

    #print(userd[usid])

if usid in userd:         
           
    friendfreq={}
    for friend in userd[usid]:
        for friend2 in userd[friend]:
            if friend2 != usid and friend2 not in userd[usid]:
                if friend2 in friendfreq:
                    friendfreq[friend2]=friendfreq[friend2]+1
                else:
                    friendfreq[friend2]=1

    if len(friendfreq)==0:
        print("There is no friend to suggest")
    else:
        #print(friendfreq)
        values=list(friendfreq.values())
        mx=[]
        mxvalue=max(values)
        #print(values)
        #print(mxvalue)
        #print(friendfreq.items())
        for x,y in friendfreq.items():
            if y==mxvalue:
                mx.append(int(x))
        #print(mx)
        output=""
        while len(mx)>0:
            mn=min(mx)
            r=mx.index(mn)
            mx.pop(r)
            output+=str(mn)
            output+=", "
        print(output[:len(output)-2])
else:
    print("There is no such user")
