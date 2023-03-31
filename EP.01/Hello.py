import turtle
tao = turtle. Pen()
tao.shape ('turtle')
tao.fillcolor ('yellow')
tao.pensize (5)
turtle.bgcolor('black')
colors = ['red', 'blue', 'white', 'green', 'orange']
tao.pencolor ('yellow')
tao.penup()
tao.left (90)
tao.backward (200)
tao.pendown ()
tao. forward (400)
tao.right (90)
for R in range (50):
    tao.pencolor (colors [R%5])
    tao.backward (1*R)
    tao.right (29)


    
