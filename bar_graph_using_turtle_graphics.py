''' Please open this spyder'''


import pandas as pd
import xlrd
import openpyxl
xls = pd.ExcelFile('C:/Users/neha/OneDrive/Desktop/bar graph.xlsx')
print(xls)
df = xls.parse('Sheet1')
print(df)
print(df['Grade'].value_counts())
A = df['Grade'] == 'A'
print(df[A])
x=df[A]
print(x)
First_class = len(x)
print(First_class)

B = df['Grade'] == 'B'
print(df[B])
y=df[B]
print(y)
Second_class = len(y)
print(Second_class)

C = df['Grade'] == 'C'
print(df[C])
z=df[C]
print(z)
Third_class = len(z)
print(Third_class)

D = df['Grade'] == 'D'
print(df[D])
w=df[D]
print(w)
Fourth_class = len(w)
print(Fourth_class)


import turtle

def drawBar(t, height):
    " Get turtle t to draw one bar, of height. "
    t.begin_fill()               
    t.left(90)
    t.forward(height)
    t.write(str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()





wn = turtle.Screen()             
wn.bgcolor("black")
xs = [First_class, Second_class, Third_class, Fourth_class]
maxheight = max(xs)
numbars = len(xs)
border = 10

alex = turtle.Turtle() 
wn.setworldcoordinates(0-border, 0-border,40*numbars+border, maxheight+border)          
alex.color("blue")
alex.fillcolor("white")
alex.pensize(3)



for a in xs:
    drawBar(alex, a)

alex.penup()
alex.goto(165,6)    
alex.pendown()
alex.write('X-axis is for the various distinctions')
alex.penup()
alex.goto(165,5)
alex.pendown()
alex.write('Y-axis represents the number of students')
alex.penup()
alex.goto(165,4)
alex.pendown()
alex.write('The first bar is the first divison')
alex.penup()
alex.goto(165,3)
alex.pendown()
alex.write('The second bar is the second divison')
alex.penup()
alex.goto(165,2)
alex.pendown()
alex.write('The third bar is the third divison')
alex.penup()
alex.goto(165,1)
alex.pendown()
alex.write('The fourth bar is the fourth divison')
alex.penup()
    
    


wn.exitonclick()



