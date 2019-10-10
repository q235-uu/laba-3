import graph

sunset = None


def sun():
    global sunset
    graph.brushColor('black')
    sunset = graph.circle(x0, y0, 30)


def sun_move():
    global x0, y0, sunset
    graph.moveObjectTo(sunset, x0, y0)
    x0 += 3
    y0 += 2
    if x0 > 1200:
        x0 = 0
    if y0 > 800:
        y0 = 0


def bird(x, y, color):
    graph.penColor(color)
    graph.line(x, y, x + 20, y)
    graph.line((x + 20), y, (x + 37), y + 10)


def cir(a, b, r):
    graph.brushColor('yellow')
    graph.circle(a, b, r)


graph.windowSize(1200, 800)
graph.canvasSize(1200, 800)
graph.penSize(0)

graph.brushColor("#fed5a2")
graph.rectangle(0, 0, 1200, 200)
graph.brushColor("#fed5c4")
graph.rectangle(0, 200, 1200, 400)
graph.brushColor("#fed594")
graph.rectangle(0, 400, 1200, 600)
graph.brushColor("#b38694")
graph.rectangle(0, 600, 1200, 800)


def update():
    for i in range(1, 11):
        x = 1.1**i
        y = 3 * i
        graph.moveObjectBy(obj, x, y)


graph.onTimer(update, 20)


graph.penColor("#fc9831")
graph.brushColor("#fc9831")
graph.polygon([(250, 250), (500, 300), (0, 400)])
graph.polygon([(850, 150), (1200, 200), (700, 300)])

graph.penColor("red")
graph.brushColor("red")
graph.circle(600, 500, 50)
graph.polygon([(0, 600), (300, 400), (600, 550)])
graph.polygon([(600, 550), (850, 400), (1200, 500)])


x = 20
y = 10
x0 = y0 = 100
for j in range(1, 100):
    bird(x, y, "black")
    x += 30
    y += 30
x = 20
y = 790
for j in range(1, 100):
    bird(x, y, "black")
    x += 30
    y -= 30


a = 40
b = 40
r = 25
for h in range(1, 100):
    cir(a, b, r)
    a += 60
    b += 70
    r += 5
sun()
graph.onTimer(sun_move, 100)
graph.penColor("yellow")
graph.brushColor("yellow")
obj = graph.circle(600, 100, 60)

graph.run()
