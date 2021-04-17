# My versions of the python bultin functions

# my range is inclusive,inclusive unlike the built in, which is inclusive exclusive
def newrange(start,stop=None):
    if stop:
        i = start
    else:
        i = 0
        stop = start
    
    out = []
    while i <= stop:
        out.append(i)
        i += 1
    return out

def length(item):
    index = 0
    while True:
        try:
            _ = item[index]
            index +=1
        except:
            break
    return index
def mini(nos):
    m = nos[0]
    for no in nos:
        if no < m:
            m = no
    return m
def maxi(nos):
    m = nos[0]
    for no in nos:
        if no > m:
            m = no
    return m
