import random,math,timeit
a = 10
#generates fake random numbers
def semirandom():
    global a
    a = (a * 8) % 11
    return a
#turn negative values into positive ones
def normalise(val):
    return math.sqrt(val**2)
class ListTools:
    def __init__(self,arr):
        self.list = arr
        self.i = 0
    #this version does have to load the list again and use it
    def eping_pong(self):
        lst = self.list+list(reversed(self.list[1:-1]))
        self.iters=0
        while True:
            if self.i >= len(lst):
                self.i = 0
            yield self.iters,lst[self.i]
            self.i += 1
            self.iters +=1

    #this is usually slower but doesn't have to write a new list
    def ping_pong(self):
        self.iters = 0
        incr = 1
        while True:
            if self.i >= len(self.list):
                self.i -=2
                incr = -1
            elif self.i < 1:
                self.i = 0
                incr = 1
            yield self.iters,self.list[self.i]
            self.i += incr
            
            self.iters +=1
    #goes through list, then goes back to list[0]
    def loop(self):
        self.iters=0
        while True:
            if self.i >= len(self.list):
                self.i = 0
            yield self.iters,self.list[self.i]
            self.i += 1
            self.iters +=1


def normalise_list(vals,method):
    return [method(val) for val in vals]
def negative_normalise(val):
    val = float(val)
    if val > 0:
        return -1 * val
    else:
        return val
#sticky caps is where parts of a sentence are randomly capitalised, e.g. hElLo PeRsoN
def sticky_caps(mystr):
    newstr=""
    for i in range(len(mystr)):
        r = random.randint(0,1)
        if r == 0:
            newstr += mystr[i].lower()
        else:
            newstr += mystr[i].upper()

    return newstr
def keepcase(string):
    out=[]
    lowers= "abcdefghijklmnopqrstuvwxyz"
    for i,char in enumerate(string):
        if char in lowers:
            out.append((i,False))
        elif char in lowers.upper():
            out.append((i,True))
        else:
            out.append((i,None))
    return out

            

def owoify(mystr):
    cases = keepcase(mystr)
    mystr = mystr.lower()
    replacers = [["r", "w"],["l", "w"],
    ["no", "nu"],["has", "haz"],["have", "haz"],
    ["you", "uu"],["the ", "da "]]
    for repl in replacers:
        mystr = mystr.replace(repl[0],repl[1])
    newstr=""
    for k in cases:
        if k[0] < len(mystr):
            if k[1] == True:
                newstr += mystr[k[0]].upper()
            elif k[1] == False:
                newstr += mystr[k[0]].lower()
            else:
                newstr += mystr[k[0]]
    return newstr
def myrstrip(string,detect):
    mystr = str(string)
    mystr = mystr[::-1]
    outstr=''
    found = 0
    finding = True
    for char in mystr:
        if char == detect and finding:
            found += 1
            continue
        finding = False
        outstr += char

    outstr = outstr[::-1]
    return string,found
#rounds no to amount of sigfigs
def sig_fig(no,sig):
    return round(no, sig - int(math.floor(math.log10(abs(no)))) - 1)


#lossless compression
def compress(items):
    tmp=[]
    
    for i,item in enumerate(items):
        a = len(tmp) - 1
        if a == -1:
            tmp.append([item,1])
        elif tmp[a][0] == item:
           tmp[a][1] += 1
        else:
            tmp.append([item,1])
    return tmp
def median(items):
    items = sorted(items)
    l = float(len(items)-1)
    l = l/2
    if l.is_integer():
        l = int(l)
        return items[l]
    else:
        low = items[math.floor(l)]
        high = items[math.ceil(l)]
        l = (high + low) / 2
        return l
def mode(items):
    items = sorted(items,key=lambda x: x[1],reverse=True)
    last = items[0][1]
    out=[]
    for item in items:
        if item[1] == last:
            out.append(item)
        else:
            return out
#sum compressedd list without decompression
def sum_compress(items):
    total = 0
    for item in items:
        total += item[0]*item[1]
    return total
def len_compress(items):
    total = 0
    for item in items:
        total += item[1]
    return total
def avg_compress(items):
    return sum_compress(items) / len_compress(items)
#decompresses stuff compressed by the function above
def decompress(items):
    tmp =[]
    for item in items:
        for _ in range(item[1]):
            tmp.append(item[0])
    return tmp

#makes sure vars are of correct type
#sample input of_type([(var1,int),(var2,float)])
def of_type(stuff):
    for s in stuff:
        if type(s[0]) not in s[1]:
            return False
    return True
#keeps value within bounds, eg clamp(0,(1,5)) returns 1
def clamp(val,clamp):
    if not of_type([(clamp,[tuple])]):
        return None
    val = float(val)
    low = float(clamp[0])
    high = float(clamp[1])
    if val > high:
        return high
    elif val < low:
        return low
    else:
        return val
#returns smallest item in list, biggest item in list and range of list
efficient_range = lambda x: [min(x),max(x),max(x)-min(x)]

