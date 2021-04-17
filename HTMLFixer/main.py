#converts html so it uses html codes so html code can be displayed in html
fname = input("File name(must be in same dir):")
with open(fname,"r") as f:
    data = f.read()
repl = [[">",'&gt;'],["<","&lt;"]]
for i in range(len(repl)):
    data = data.replace(repl[i][0],repl[i][1])
with open(fname,"w") as f:
    f.write(data)