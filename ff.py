from graph import *


def qq():
    moveTo(0,600)

def bird(x,y,color):
    penColor(color)
    line(x, y, x+20, y)
    line((x+20), y, (x+37), y+10)

def cir(a,b,r):
    brushColor('yellow')
    circle(a,b,r)
  


windowSize(1200,800)
canvasSize(1200,800)
penSize(0)

brushColor("#fed5a2")
rectangle(0, 0, 1200, 200)
brushColor("#fed5c4")
rectangle(0, 200, 1200, 400)
brushColor("#fed594")
rectangle(0, 400, 1200, 600)
brushColor("#b38694")
rectangle(0, 600, 1200, 800)

penColor("yellow")
brushColor("yellow")
circle(600,100,60)

penColor("#fc9831")
brushColor("#fc9831")
polygon([(250,250),(500,300),(0,400)])
polygon([(850,150),(1200,200),(700,300)])
     
penColor("red")
brushColor("red")
circle(600,500,50)
polygon([(0,600),(300,400),(600,550)])
polygon([(600,550),(850,400),(1200,500)])



x=20
y=10
for j in range (1,100):
    bird(x,y,"black")
    x+=30
    y+=30
x=20
y=790
for j in range (1,100):
    bird(x,y,"black")
    x+=30
    y-=30





a=40
b=40
r=25
for h in range (1,100):
    cir(a,b,r)
    a+=60
    b+=70
    r+=5
    
run()
