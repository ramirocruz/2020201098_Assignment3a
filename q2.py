import sys

monthdayslist=[31,28,31,30,31,30,31,31,30,31,30,31]
monthmap={"jan":1,"feb":2,"mar":3,"apr":4,"may":5,"jun":6,"jul":7,"aug":8,"sep":9,"oct":10,"nov":11,"dec":12,"january":1,"february":2,"march":3,"april":4,"may":5,"june":6,"july":7,"august":8,"september":9,"october":10,"november":11,"december":12}

def isleap(year):
    if(year%400==0):
        return True
    elif(year%4==0):
        if(year%100==0):
            return False
        return True
    return False

def leapdays(year):
    return (year//400 + year//4 - year//100)

def interdays(year):
    if(year==0):
        return 0
    return 365*year + leapdays(year)

def monthdays(month,year):
    total=0
    i=1
    while(i < month):
        total+=monthdayslist[i-1]
        i+=1
    if(isleap(year) and month>1):
        return total+1
    return total    

def calcdays(day,month,year):
    penyear = max(year-1,0)
    total=interdays(penyear)
    total+=monthdays(month,year)
    total+=day
    return total

def parse(date):
    if(date.find(" ")!=-1):
        date= date.split()  
    elif(date.find(",")!=-1):
        date= date.split(",")
    elif(date.find(".")!=-1):
        date= date.split(".")
    elif(date.find("-")!=-1):
        date= date.split("-")
    elif(date.find("/")!=-1):
        date= date.split("/")
 

    date=[el.strip() for el in date]
    return date

def v_day(day,month,year):
    if(len(day)<3):
        try:
            day=int(day)
        except ValueError:
            return -1
    elif(len(day)<5):
        try:
            day=int(day[0:-2])
        except ValueError:
            return -1
    else:
        return -1
    
    if(day<1 or day>31):
        return -1
    
    if(day>monthdayslist[month-1]):
        if(month==1 and isleap(year)):
            if(day==29):
                return day
    
        return -1
    return day

def v_month(month):
    if(len(month)<3):
        try:
            month=int(month)
        except ValueError:
            return -1
    else:
        try:
            month=monthmap[month.lower()]
        except KeyError:
            try:
                month=monthmap[month.lower()[:-1]]
            except KeyError:
                return -1
    if(month < 1 and month > 12):
        return -1
    return month

def v_year(year):
    try:
        year=int(year)
    except ValueError:
        return -1
    if(year<0):
        return -1
    return year

def validate(day,month,year,result):
    year=v_year(year)
    if(year==-1):
        return False
    month=v_month(month)
    if(month==-1):
        return False
    day=v_day(day,month,year)
    if(day==-1):
        return False
    result[:]=[day,month,year]
    return True

def diffdays(date1,date2,dateformat):
    date1=parse(date1)
    date2=parse(date2)
    d1=[]
    d2=[]
   
    if(len(date1) !=3 or len(date2)!=3):
        return -1
    

    res1=False
    res2=False
    
    if(dateformat==None):
        res1=validate(date1[0],date1[1],date1[2],d1)
        res2=validate(date2[0],date2[1],date2[2],d2)
  
    else:
        if(dateformat=="dmy"):
            res1=validate(date1[0],date1[1],date1[2],d1)
            res2=validate(date2[0],date2[1],date2[2],d2)
        elif(dateformat=="mdy"):
            res1=validate(date1[1],date1[0],date1[2],d1)
            res2=validate(date2[1],date2[0],date2[2],d2)
        else:
            return -1


    if(res1 and res2):
        day1=calcdays(d1[0],d1[1],d1[2])
        day2=calcdays(d2[0],d2[1],d2[2])
        diff=abs(day1-day2)
        return diff
    return -1



with open("date_calculator.txt","r") as f:
    data=f.read().split("\n")
data = [el[el.find(":")+1:].strip() for el in data]

date1=data[0]
date2=data[1]

argc = len(sys.argv)

dateformat=None
if(argc==2):
    dateformat = sys.argv[1].lower()
    dateformat=parse(dateformat)
    temp=""
    for el in dateformat:
        temp+=el[0]
    dateformat=temp



val = diffdays(date1,date2,dateformat)

if(val==-1):
    val="Invalid Dates"

with open ("output.txt","w") as f:
    f.write(str(val))

