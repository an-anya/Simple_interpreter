var_map={}
term_map={}

def isoperator(x):
    if x in ('+', '-', '*', '/', "and", "or", '>', '<', '>=', '<=', '==', '!='):
        return True
    return False

def isvar(x):
    if x=="True" or x=="False" or x=="and" or x=="or":
        return False
    else:
        x.strip()
        for i in range(len(x)):
            if ord('a') <=ord(x[i])<= ord('z') or ord('A') <=ord(x[i])<= ord('Z'):
                pass
            else:
                return False
        return True

def value(x):
    if(x=="True"):
        return True
    if(x=="False"):
        return False
    if x in ('0','1','2','3','4','5','6','7','8','9'):
        return int(x)
    if x in var_map:
        return var_map[x]
    
def evaluate(op,val1,val2):
    if op=='+':
        return val1+val2
    elif op=="-":
        return val1-val2
    elif op=="*":
        return val1*val2
    elif op=="/":
        return val1/val2
    elif op==">":
        if val1>val2:
            return True
        return False
    elif op=="<":
        if val1<val2:
            return True
        return False
    elif op==">=":
        if val1>=val2:
            return True
        return False
    elif op=="<=":
        if val1<=val2:
            return True
        return False
    elif op=="==":
        if val1==val2:
            return True
        return False
    elif op=="!=":
        if val1!=val2:
            return True
        return False
    elif op=="and":
        return val1 and val2
    elif op=="or":
        return val1 or val2

Input = open("input_file.txt","r")
Lines = Input.readlines()
n = len(Lines)   # number of commands

data=[]
for line in Lines:
    line.strip()
    l =line.split()
    val1=0
    val2=0
    for i in range(2,len(l)-1):
        if not isoperator(l[i]) and not isvar(l[i]):
            if l[i] not in term_map:
                term_map[l[i]]=value(l[i])
                data.append(value(l[i]))
            else:
                continue
            val1=value(l[i])
        elif isvar(l[i]):
            if l[i] in var_map:
                val1=var_map[l[i]]
            else:
                print("statement wrong:error 1")
        else:
            if isvar(l[i+1]):
                if l[i+1] in var_map:
                    val2=var_map[l[i+1]]
                else:
                    print("statement wrong :error 2")
            elif isoperator(l[i+1]):
                print("wrong statement :error 3")
            else:
                if l[i+1] in term_map:
                    val2=term_map[l[i+1]]
                else:
                    term_map[l[i+1]]=value(l[i+1])
                    data.append(value(l[i+1]))
                    val2=value(l[i+1])

            finalval=evaluate(l[i],val1,val2)

            if str(finalval) not in term_map:
                data.append(finalval)
                term_map[str(finalval)]=finalval
                index=0
                for k in range(len(data)):
                    if data[k]==finalval:
                        index=k
                data.append((l[0],index))
                var_map[l[0]]=finalval
            else:
                index=0
                for k in range(len(data)):
                    if data[k]==finalval:
                        index=k
                data.append((l[0],index))
                var_map[l[0]]=finalval
            
print(data)