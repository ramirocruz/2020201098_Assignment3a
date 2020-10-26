import json
with open('org.json','r') as f:
    data = json.loads(f.read())
level = dict({})
par = dict({})
ename=dict({})
def isless(par1,par2):
    return int(par1[1:]) < int(par2[1:])
def calclevel(par1,par2):
    return int(par1[1:]) - int(par2[1:])
for el in data:
    for el2 in data[el]:
        ename[el2['eid']]=el2['name']
        try:
            par[el2['eid']]=el2['parent']
        except KeyError:
            par[el2['eid']]=None
        level[el2['eid']] = el

inp1,inp2 = input().split()
inp1=int(inp1)
inp2=int(inp2)
if isless(level[inp1],level[inp2]):
    one=inp1
    two=inp2
else:
    one=inp2
    two=inp1

while isless(level[one],level[two]):
    two=par[two]

while par[one]!=par[two]:
    one=par[one]
    two=par[two]

if(par[one]==None):
    print("No common leader")
else:
    print(par[one])
    print("Leader {} is {} levels above {}".format(ename[par[one]],calclevel(level[inp1],level[par[one]]),ename[inp1]))
    print("Leader {} is {} levels above {}".format(ename[par[one]],calclevel(level[inp2],level[par[one]]),ename[inp2]))


               
            