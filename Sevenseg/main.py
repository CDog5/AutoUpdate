allowed='012356789abcdefhjnprtuy'
class Segment:
    def __init__(self,ison):
        self.on = ison
class SevenSeg:
    def __init__(self,char):
        self.segs = []
        for i in range(7):
            self.segs.append(Segment(False))
        res = self.segres(char)
        for i, res1 in enumerate(res):
            self.segs[i] = res1
    # from top to bottom, left to right
    def segres(self,char):
        char = char.lower()
        if char == '0':
            return [True,True,True,False,True,True,True]
        elif char == '1':
            return [False,False,True,False,False,True,False]
        elif char == '2':
            pass
        elif char == '3':
            pass
        elif char == '5':
            pass
        elif char == '6':
            pass
        elif char == '7':
            pass
        elif char == '8':
            pass
        elif char == '9':
            pass
        elif char == 'a':
            pass
        elif char == 'b':
            pass
        elif char == 'c':
            pass
        elif char == 'd':
            pass
        elif char == 'e':
            pass
        elif char == 'f':
            pass
        elif char == 'h':
            pass
        elif char == 'j':
            pass
        elif char == 'n':
            pass
        elif char == 'p':
            pass
        elif char == 'r':
            pass
        elif char == 't':
            pass
        elif char == 'u':
            pass
        elif char == 'y':
            pass
print(SevenSeg('1'))
