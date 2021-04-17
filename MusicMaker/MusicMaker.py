from playsound import playsound
import random,time,threading,pianotools,os
resrcs = os.path.join(os.getcwd(),'resources/')
notes=[]
class Note:
    def __init__(self,noteltr,octave=None):
        self.octave = octave
        self.name = noteltr
        self.sound = noteltr
        notes.append(self)
    def play(self):
        octave = self.octave
        if octave:
            if octave == 1:
                playsound(resrcs+self.sound+".mp3",False)
            elif octave == 2:
                playsound(resrcs+self.sound+"'"+".mp3",False)
            elif octave == 3:
                playsound(resrcs+self.sound+"''"+".mp3",False)
            elif octave == 4:
                playsound(resrcs+self.sound+"'''"+".mp3",False)
        else:
            playsound(resrcs+self.sound+".mp3",False)
for note in noteltrs:
    nt = Note(note)
def play_melodies():
    with open("melodies.txt","r") as f:
        count = 1
        while True:
            line = f.readline() 
  
            if not line: 
                break
            print(count)
            for nt in line.split(" "):
                
                play_note(nt)
                time.sleep(0.3)
            count += 1
            time.sleep(1)
def play_melody(lno):
    with open("melodies.txt","r") as f:
        count = 1
        while True:
            line = f.readline() 
  
            if not line: 
                break
            if count == lno:
                for nt in line.split(" "):
                    play_note(nt)
                    time.sleep(0.3)
            count += 1
            time.sleep(1)
def play_note(note,octave=None):
    for nts in notes:
        if nts.name.lower() == note.lower():
            nts.play(octave)
def generate_melody(nts,amnt=7,play=False):
    with open("melodies.txt","a") as f:
        melody=[]
        md=f"{nts[0]} "
        melody.append(Note(nts[0],1))
        for _ in range(1,amnt):
            nt = nts[random.randint(0,len(nts)-1)]
            octave = random.randint(1,3)
            nt = Note(nt,octave)
            melody.append(nt)
            md += f"{nt.name}{nt.octave} "
        melody.append(Note(nts[0],1))
        
        md += f"{melody[0].name}{melody[0].octave} "
        f.write(md+'\n')
        print(f"Generated melody: {md}")
        if play:
            for note in melody:
                note.play()
                time.sleep(0.3)
for i in range(10):
    key = random.choice(list(pianotools.keys.keys()))
    print(key)
    generate_melody(pianotools.keys[key],amnt=50,play=True)
    time.sleep(1)

