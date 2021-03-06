import turtle
import random
window=turtle.Screen()
board=[[0,2,3],[5,6,7],[8,9,10],0]

def reset():
    board[0][0]=0
    board[0][1]=2
    board[0][2]=3
    board[1][0]=4
    board[1][1]=5
    board[1][2]=6
    board[2][0]=7
    board[2][1]=8
    board[2][2]=9
    board[3]=0

def move(x,y,orient):
    turtle.penup()
    turtle.goto(x,y)
    turtle.setheading(orient)
    turtle.pendown()
    return True

def tarta():
    turtle.speed(0)
    turtle.shape('turtle')
    turtle.hideturtle()
    return True

def board_maker():
    coord = [(-100,250,270),(100,250,270),(-250,100,0),(-250,-100,0)]
    for i in range(4):
        tup= coord[i]
        move(tup[0],tup[1],tup[2])
        turtle.forward(500)
        
def c_v_h():
    for i in range(3):
        if board[0][i]==board[1][i]==board[2][i]:
            return True
        elif board[i][0]==board[i][1]==board[i][2]:
            return True
    return False

def check():
    if c_v_h() or board[0][0]==board[1][1]==board[2][2]or board[0][2] == board[1][1]==board[2][0]:
        return True
    
    elif board[3]==9:
        turtle.clear()
        move(0,0,0)
        turtle.color('black')
        turtle.write('Empate!',False,'center',("Arial", 30, "normal"))
        reset()
        window.onclick(begin)
        window.listen()
    else:
        return False

def dic(lin,col):
    if col==0:
        x=-200
    elif col==1:
        x=0
    elif col==2:
        x=200
    if lin==0:
        y1=200
        y2=125
    elif lin==1:
        y1=0
        y2=-75
    elif lin==2:
        y1=-200
        y2=-275
    if (-1)**board[3]==-1:
        return (x,y1,45)
    elif(-1)**board[3]==1:
        return (x,y2,0)

def draw(lin,col):
    tup=dic(lin,col)
    if (-1)**board[3]==-1:
        move(tup[0],tup[1],tup[2])    
        turtle.pencolor('green')
        for i in range(4):
            turtle.forward(75)
            turtle.backward(75)
            turtle.right(90)        
    elif(-1)**board[3]==1:
        move(tup[0],tup[1],tup[2])
        turtle.pencolor('red')
        turtle.circle(75)   

def fim():
    turtle.clear()
    move(0,0,0)
    if (-1)**board[3]==-1:
        turtle.write('Player 1 Ganhou!',False,'center',("Arial", 30, "normal"))
        reset()
        window.onclick(begin)
        window.listen()
    else:
        turtle.write('Player 2 Ganhou!',False,'center',("Arial", 30, "normal"))
        reset()
        window.onclick(begin)
        window.listen()

def decode(x,y):
    if x < -100:
        col=0
    elif x>=-100 and x<=100:
        col=1
    elif x>100:
        col=2
    if y > 100:
        lin=0
    elif y<=100 and y>=-100:
        lin=1
    elif y<-100:
        lin=2    
    if board[lin][col]!= -1 and board[lin][col] !=1:
        board[3]+=1
        board[lin][col]=(-1)**board[3]
        draw(lin, col)
        if check():
            fim()
        #print(board, '---' , lin, col)
    return True

def play():
    turtle.hideturtle()
    board_maker()
    window.onclick(decode)
    window.listen()

def loop(x,y):
    if -50<x<50 and -5<y<45:
        turtle.clear()
        play()
    else:
        turtle.showturtle()
        turtle.goto(x, y)

def begin(x,y):
    r_x=random.randint(0,300)
    r_y=random.randint(0,300)
    turtle.clear()
    turtle.color('black')
    turtle.write('Play',False,'center',("Arial", 30, "normal"))
    move(-50,-5,90)
    turtle.forward(50)
    move(-50,-5,0)
    turtle.forward(100)
    move(50,-5,90)
    turtle.forward(50)
    move(-50,45,0)
    turtle.forward(100)
    move(r_x,r_y,0)
    window.onclick(loop)
    window.listen()

def main():
    tarta()
    begin(0,0)
    turtle.mainloop()
    
    return 'Fim'

if __name__ == '__main__':
	main()
