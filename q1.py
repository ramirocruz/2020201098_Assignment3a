import json


def get_data_from_file():
    with open('org.json','r') as f:
        data = json.loads(f.read())
    return data


def findmin(ar):
    min = 1000
    for el in ar:
        if(level[el-1]<min):
            min=level[el-1]
    return min

def isEqual(ar):
    for i in range(len(ar)-1):
        if(ar[i]!=ar[i+1]):
            return False
    return True

def categorise_data():
    for el in data:
        for el2 in data[el]:
            ename[el2['eid']]=el2['name']
            try:
                par[el2['eid']]=el2['parent']
            except KeyError:
                par[el2['eid']]=None
            level[el2['eid']] = el



def format_input():
    global level
    level = [int(level[el][1:]) for el in level]
    inp=[int(el) for el in input().split()]
    return inp

data = get_data_from_file()
level = dict({})
par = dict({})
ename=dict({})
categorise_data()
inp=format_input()
lowestlvl = findmin(inp)
nodes=[]

def classifying_input():
    global inp
    global nodes
    for node in inp:
        while (level[node-1] >= lowestlvl):
            node=par[node]
            if(node==None):
                break
        nodes.append(node)
        if(node==None):
            nodes=None
            break

classifying_input()


def final_output():
    global nodes
    if(nodes==None):
        print("No common leader")
    else:
        while(isEqual(nodes)==False):
            nodes = [par[el] for el in nodes]
        
        print(nodes[0])
        for el in inp:
            print("Leader {} is {} levels above {}".format(ename[nodes[0]],level[el-1]-level[nodes[0]-1],ename[el]))


final_output()