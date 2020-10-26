from functools import cmp_to_key
from datetime import date
def diff(time1,time2):
    pos1=time1.find(":")
    h1=int(time1[:pos1])
    m1=int(time1[pos1+1:pos1+3])
    val1=0
    if(time1[pos1+3].lower()=='a'):
        val1=h1*60 + m1
    else:
        if(h1==12):
            val1=h1*60 + m1
        else:
            val1=(h1+12)*60 + m1
    pos1=time2.find(":")
    h1=int(time2[:pos1])
    m1=int(time2[pos1+1:pos1+3])
    val2=0
    if(time2[pos1+3].lower()=='a'):
        val2=h1*60 + m1
    else:
        if(h1==12):
            val2=h1*60 + m1
        else:
            val2=(h1+12)*60 + m1
    # print(val1-val2)
    return val1-val2

def addtime(t,dur):
    t=diff(t,"00:00AM")
    t+=dur
    h=t//60
    m=str(t%60)
    if(len(m)==1):
        m='0'+m
    if(h==12):
        return "{}:{}PM".format(h,m)
    elif(h>12):
        return "{}:{}PM".format(h-12,m)
    return "{}:{}AM".format(h,m)

    
with open("Employee1.txt","r") as f:
    emp1=f.read()
with open("Employee2.txt","r") as f:
    emp2=f.read()

emp1=eval(emp1)
emp2=eval(emp2)

for i in emp1:
    for el in emp1[i]:
        ename1=i
        d1=el
        t1=emp1[i][el]

for i in emp2:
    for el in emp2[i]:
        ename2=i
        d2=el
        t2=emp2[i][el]

# print(ename1,d1,t1)
# print(ename2,d2,t2)

t1 = [i.replace(" ","") for i in t1]
t2 = [i.replace(" ","") for i in t2]

t1=[i.split('-') for i in t1]
# print(t1)

merged=[]
open1=[]
first="9:00AM"
second="5:00PM"
for interval in t1:
    # print(interval[0],interval[1],first)
    if(diff(interval[0],first)==0):
        first=interval[1]
        continue
    merged.append([first,interval[0]])
    open1.append("{} - {}".format(first,interval[0]))
    first=interval[1]
if(diff(t1[-1][1],second)!=0):
    merged.append([t1[-1][1],second])
    open1.append("{} - {}".format(t1[-1][1],second))

# print(open1)

t2=[i.split('-') for i in t2]
# print(t2)

open2=[]
first="9:00AM"
second="5:00PM"
for interval in t2:
    if(diff(interval[0],first)==0):
        first=interval[1]
        continue
    merged.append([first,interval[0]])
    open2.append("{} - {}".format(first,interval[0]))
    first=interval[1]
if(diff(t2[-1][1],second)!=0):
    merged.append([t2[-1][1],second])
    open2.append("{} - {}".format(t2[-1][1],second))

# print(open2)  


def comp(list1,list2):
    val = diff(list1[0],list2[0])
    if(val==0):
        return diff(list1[1],list2[1])
    return val
# print(merged)
merged.sort(key=cmp_to_key(comp))
# print(merged)
slot=int(float(input().strip())*60)
ans=[]
for i in range(len(merged)-1):
    if(diff(merged[i][1],merged[i+1][0]) >= slot):
        ans.append("{} - {}".format(merged[i+1][0],addtime(merged[i+1][0],slot)))
        break

newans={'{}'.format(d1):ans}

D1,M1,Y1=[int(x) for x in d1.split('/')]
D2,M2,Y2=[int(x) for x in d2.split('/')]
d1=date(Y1,M1,D1)
d2=date(Y2,M2,D2)

# print(ans)

res="Available slot\n"
res+="{}: {}\n".format(ename1,open1)
res+="{}: {}\n\n".format(ename2,open2)
res+="Slot Duration: {} hour\n".format(slot/60)
if(d1!=d2 or len(ans)==0):
    res+="No Slots Available"
else:
    res+=str(newans)

with open("output.txt","w") as f:
    f.write(res)