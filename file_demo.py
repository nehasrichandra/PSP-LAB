#to open existing file from python

f = open("C:/Users/neha/Desktop/Raptor programs/lines.txt","r")

if f.mode=="r":
    contents=f.read()
    print(contents)
