from tkinter import*

master = Tk()

WIDTH = 500
HEIGHT = 300

x1 = WIDTH/2
y1 = HEIGHT/2

canvas = Canvas(master, width=WIDTH, height=HEIGHT)
canvas.pack()

X_LOC = WIDTH-100
Y_LOC = 40

def clicked_up(event):
    print('You clicked top')
    print('You clicked left')
    global x1, y1
    draw_white_rect()
    y1-=10
    draw_green_rect()
    
def clicked_left(event):
    print('You clicked left')
    global x1, y1
    draw_white_rect()
    x1-=10
    draw_green_rect()
    
    
def clicked_right(event):
    print('You clicked right')
    print('You clicked left')
    global x1, y1
    draw_white_rect()
    x1+=10
    draw_green_rect()
    
def clicked_down(event):
    print('You clicked down')
    print('You clicked left')
    global x1, y1
    draw_white_rect()
    y1+=10
    draw_green_rect()

top = canvas.create_rectangle(X_LOC+15, Y_LOC-30, X_LOC+45, Y_LOC, fill='gray', tags='top')
canvas.tag_bind(top, '<Button-1>', clicked_up)
left = canvas.create_rectangle(X_LOC, Y_LOC, X_LOC+30, Y_LOC+30, fill='gray', tags='left')
canvas.tag_bind(left, '<Button-1>', clicked_left)
right = canvas.create_rectangle(X_LOC+30, Y_LOC, X_LOC+60, Y_LOC+30, fill='gray', tags='right')
canvas.tag_bind(right, '<Button-1>', clicked_right)
down = canvas.create_rectangle(X_LOC+15, Y_LOC+30, X_LOC+45, Y_LOC+60, fill='gray', tags='down')
canvas.tag_bind(down, '<Button-1>', clicked_down)


canvas.create_rectangle(x1, y1, x1+10, y1+10)

def draw_green_rect():
    canvas.create_rectangle(x1, y1, x1+10, y1+10, fill='green')
    
def draw_white_rect():
    canvas.create_rectangle(x1, y1, x1+10, y1+10, fill='pink')
    
def move(event):
    global x1, y1
    if event.char=='a':
        draw_white_rect()
        x1-=10
    elif event.char=='d':
        draw_white_rect()
        x1+=10
    elif event.char=='w':
        draw_white_rect()
        y1-=10
    elif event.char=='z':
        draw_white_rect()
        y1+=10
    draw_green_rect()
        

master.bind("<Key>", move)
master.mainloop()
