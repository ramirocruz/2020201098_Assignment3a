from functools import cmp_to_key
from datetime import date
import glob

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

emp=[]  
def get_data_from_file():
    global emp
    for filename in glob.glob('Employee*.txt'):
        with open(filename,"r") as f:
            emp.append(f.read())
    emp = [eval(el) for el in emp]

get_data_from_file()
ename=[]
d=[]
t=[]
def categorise_data():
    global ename
    global d
    global t
    global emp
    for emp1 in emp:
        for i in emp1:
            ename.append(i)
            for el in emp1[i]:
                d.append(el)
                t.append(emp1[i][el])

categorise_data()

def format_data():
    global t
    for t1 in t:
        t1[:] = [i.replace(" ","") for i in t1]
        t1[:] = [i.split('-') for i in t1]

format_data()

vacant=[]
totalmerged=[]

def get_free_time():
    global totalmerged
    global vacant
    for t1 in t:
        merged=[]
        open1=[]
        first="9:00AM"
        second="5:00PM"
        for interval in t1:
            
            if(diff(interval[0],first)==0):
                first=interval[1]
                continue
            merged.append([first,interval[0]])
            open1.append("{} - {}".format(first,interval[0]))
            first=interval[1]
        if(diff(t1[-1][1],second)!=0):
            merged.append([t1[-1][1],second])
            open1.append("{} - {}".format(t1[-1][1],second))
        vacant.append(open1)
        totalmerged.append(merged)


def comp(list1,list2):
    val = diff(list1[0],list2[0])
    if(val==0):
        return diff(list1[1],list2[1])
    return val

get_free_time()

merged = totalmerged[0]

slot=int(float(input().strip())*60)

def find_common_slot():
    global merged
    global totalmerged
    for i in range(1,len(totalmerged)):
        merged.extend(totalmerged[i])
        merged.sort(key=cmp_to_key(comp))
        ans=[]
        for i in range(len(merged)-1):
            if(diff(merged[i][1],merged[i+1][0]) >= slot):
                ans.append([merged[i+1][0],addtime(merged[i+1][0],slot)])
        merged=ans


find_common_slot()

try:
    newans={'{}'.format(d[0]):merged[0]}
except IndexError:
    newans={}

D=[]
tmp=[]
def format_dates():
    global D
    global tmp
    for d1 in d:
        tmp = [int(x) for x in d1.split('/')]
        D.append(date(tmp[2],tmp[1],tmp[0]))

format_dates()

def checkdate(D):
    for i in range(len(D)-1):
        if(D[i]!=D[i+1]):
            return False        
    return True


def generate_op():
    res="Available slot\n"
    for i in range(len(ename)):
        res+="{}: {}\n".format(ename[i],vacant[i])


    res+="Slot Duration: {} hour\n".format(slot/60)
    if(not checkdate(D) or len(merged)==0):
        res+="No Slots Available"
    else:
        res+=str(newans)
    
    return res

res = generate_op()
with open("output.txt","w") as f:
    f.write(res)

print(res)