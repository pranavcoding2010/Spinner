from turtle import *
state = {'turn':0}
def Spinner():
    clear()
    angle = state['turn']/10
    right(angle)
    forward(100)
    dot(120,'blue')
    back(100)
    right(120)
    forward(100)
    dot(120,'red')
    back(100)
    right(120)
    forward(100)
    dot(120,'yellow')
    back(100)
    right(120)
    update()
def animate():
    if state['turn']>0:
        state['turn']-=1
    Spinner()
    ontimer(animate)
    
def Flip():
    state['turn']+=10
setup(420,420,370,0)
tracer(False)
onkey(Flip,'space')
listen()
animate()
done()