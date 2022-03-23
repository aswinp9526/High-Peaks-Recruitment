f1= open(r"C:\Users\student\Desktop\input.txt","r")
vals=[]
cmp={}
fx=f1.read().split("\n")
f1.close()
f2=open(r"C:\Users\student\Desktop\output.txt","w")
cnt=int(fx[0].split(":")[-1][1:])

for j in fx[4:]:
    ele=j.split(":")
    cst=int(ele[-1][1:])
    cmp[cst]=ele[0]
    vals.append(cst)
vals=sorted(vals)    

mn=vals[-1]
splits=(len(vals)-cnt+1)
for j in range(splits):
   spt=vals[j:j+cnt]
   dif= spt[-1]-spt[0]
   if(dif<=mn):
       mn=dif
       goodie=spt
       


k=str("Here the goodies that are selected for distribution are:\n")
f2.write(k)

f2.write("\n")

for j in spt:
    k=str(cmp[j])+":"+str(j)
    f2.write(k)
    f2.write("\n")
f2.write("\n")    
k="And the difference between the chosen goodie with highest price and the lowest price is "+str(mn)    
f2.write(k)
f2.close()