from turtle import *
from freegames import vector

def line(start, end):
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

'''
La funcion dibuja un circulo en la pantalla desde la primera posicion dada por el ususario hasta el segundo click
Entrada: Posicion en la pantalla al dar el primer y segundo click
Salida: Ninguna
'''

def circleD(start, end):
    "Draw circle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    circle(end.x-start.x)
    end_fill()

'''
La funcion dibuja un rectangulo en la pantalla, desde donde el usuario dio click por primera vez hasta donde dio por segunda
Entrada: Posicion en la pantalla al dar el primer y segundo click
Salida: Ninguna
'''
def rectangle(start, end):
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for cout in range(2):
        forward(end.x - start.x)
        left(90)
        start.x = start.x/2
        end.x = end.x/2
        forward(end.x - start.x)
        left(90)
        start.x = start.x*2
        end.x = end.x*2
    
    end_fill()

'''
La funcion dibuja un triangulo en la pantalla, desde donde el usuario dio click por primera vez hasta donde dio por segunda
Entrada: Posicion en la pantalla al dar el primer y segundo click
Salida: Ninguna
'''
def triangle(start, end):
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for cout in range(3):
        forward(end.x - start.x)
        left(120)
    
    end_fill()

def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    "Store value in state at key."
    state[key] = value

state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')

onkey(lambda: color('violet'), 'V')

onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circleD), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
