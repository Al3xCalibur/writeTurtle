import turtle
import time
import math
from random import randint

t = turtle.Turtle()
l = 100
line = 1


def a():
  t.right(30/2)
  t.forward(l/math.cos(15*math.pi/180))
  t.right(180-30)
  t.forward(l/math.cos(15*math.pi/180))
  t.forward(-l/2/math.cos(15*math.pi/180))
  t.right(90+30/2)
  t.forward(l/4/math.cos(15*math.pi/180))
  t.left(180)
  t.up()
  t.forward(l/4/math.cos(15*math.pi/180))
  t.right(90-30/2)
  t.forward(l/2/math.cos(15*math.pi/180))
  t.left(90-30/2)
  t.down()


def b():
  t.forward(l)
  t.right(90)
  t.forward(l/6)
  t.right(30)
  t.forward(l/6/math.cos(30*math.pi/180))
  t.right(90-30)
  t.forward(l*0.4-l/6/math.cos(30*math.pi/180))
  t.right(90-30)
  t.forward(l/6/math.cos(30*math.pi/180))
  t.right(30)
  t.forward(l/6)
  t.right(180)
  t.forward(l/4)
  t.right(30)
  t.forward(l/4/math.cos(30*math.pi/180))
  t.right(90-30)
  t.forward(l*0.6-l/4/math.cos(30*math.pi/180))
  t.right(90-30)
  t.forward(l/4/math.cos(30*math.pi/180))
  t.right(30)
  t.forward(l/4)
  t.up()
  t.right(180)
  t.forward(l/2)


def c():
  t.right(90)
  t.up()
  t.forward(l/2)
  t.down()
  t.right(180)
  t.forward(l/4)
  t.right(30)
  t.forward(l/4/math.cos(30*math.pi/180))
  t.right(90-30)
  t.forward(l-l/4/math.cos(30*math.pi/180))
  t.right(90-30)
  t.forward(l/4/math.cos(30*math.pi/180))
  t.right(30)
  t.forward(l/4)
  t.right(90)
  t.up()
  t.forward(l)
  t.left(90)
  t.down()
  


def d():
  t.forward(l)
  t.right(90)
  t.forward(l/4)
  t.right(30)
  t.forward(l/4/math.cos(30*math.pi/180))
  t.right(90-30)
  t.forward(l-l/4/math.cos(30*math.pi/180))
  t.right(90-30)
  t.forward(l/4/math.cos(30*math.pi/180))
  t.right(30)
  t.forward(l/4)
  t.right(180)
  t.up()
  t.forward(l/2)
  t.down()


def e():
  t.forward(l)
  t.right(90)
  t.forward(l/2)
  t.up()
  t.right(90)
  t.forward(l/2)
  t.right(90)
  t.down()
  t.forward(l/2)
  t.left(90)
  t.forward(l/2)
  t.left(90)
  t.forward(l/2)


def f():
  t.forward(l)
  t.right(90)
  t.forward(l/2)
  t.up()
  t.right(90)
  t.forward(l/2)
  t.right(90)
  t.down()
  t.forward(l/2)
  t.left(90)
  t.up()
  t.forward(l/2)
  t.left(90)
  t.forward(l/2)
  t.down()


def g():
  t.right(90)
  t.up()
  t.forward(l/2)
  t.down()
  t.right(180)
  t.forward(l/4)
  t.right(30)
  t.forward(l/4/math.cos(30*math.pi/180))
  t.right(90-30)
  t.forward(l-l/4/math.cos(30*math.pi/180))
  t.right(90-30)
  t.forward(l/4/math.cos(30*math.pi/180))
  t.right(30)
  t.forward(l/4)
  t.right(90)
  t.up()
  t.forward(l/2)
  t.right(90)
  t.forward(l/4)
  t.right(180)
  t.down()
  t.forward(l/4)
  t.right(90)
  t.forward(l/2)
  t.left(90)


def h():
  t.forward(l)
  t.backward(l/2)
  t.right(90)
  t.forward(l/2)
  t.left(90)
  t.forward(l/2)
  t.backward(l)
  t.right(90)


def i():
  t.right(90)
  t.forward(l/4)
  t.left(90)
  t.forward(l)
  t.left(90)
  t.forward(l/4)
  t.backward(l/2)
  t.left(90)
  t.up()
  t.forward(l)
  t.right(90)
  t.down()
  t.forward(l/4)
  t.backward(l/4)
  t.left(180)


def j():
  t.right(90)
  t.left(30)
  t.forward(l/4/math.cos(30*math.pi/180))
  t.left(90-30)
  t.forward(l-l/4/math.cos(30*math.pi/180)/2)
  t.left(90)
  t.forward(l/4)
  t.backward(l/2)
  t.left(90)
  t.up()
  t.forward(l)
  t.left(90)
  t.down()
  

def k():
  t.forward(l)
  t.backward(l/2)
  t.right(45)
  t.forward(l/2/math.cos(45*math.pi/180))
  t.backward(l/2/math.cos(45*math.pi/180))
  t.right(90)
  t.forward(l/2/math.cos(45*math.pi/180))
  t.left(45)


def L():
  t.forward(l)
  t.backward(l)
  t.right(90)
  t.forward(l/2)
  

def m():
  t.forward(l)
  t.right(180-15)
  t.forward(l/math.cos(15*math.pi/180))
  t.left(180-30)
  t.forward(l/math.cos(15*math.pi/180))
  t.right(180-15)
  t.forward(l)
  t.left(90)


def n():
  t.forward(l)
  t.right(180-25)
  t.forward(l/math.cos(25*math.pi/180))
  t.left(180-25)
  t.forward(l)
  t.backward(l)
  t.right(90)


def o():
  t.right(90)
  t.up()
  t.forward(l/3)
  t.down()
  t.right(180)
  t.forward(l/3/2)
  t.right(30)
  t.forward(l/3/2/math.cos(30*math.pi/180))
  t.right(90-30)
  t.forward(l-l/3/2/math.cos(30*math.pi/180))
  t.right(90-30)
  t.forward(l/3/2/math.cos(30*math.pi/180))
  t.right(30)
  t.forward(l/3/2)
  t.right(30)
  t.forward(l/3/2/math.cos(30*math.pi/180))
  t.right(90-30)
  t.forward(l-l/3/2/math.cos(30*math.pi/180))
  t.right(90-30)
  t.forward(l/3/2/math.cos(30*math.pi/180))
  t.right(30)
  t.right(180)
  t.up()
  t.forward(l/3/2)
  t.down()


def p():
  t.forward(l)
  t.right(90)
  t.forward(l/4)
  t.right(30)
  t.forward(l/4/math.cos(30*math.pi/180))
  t.right(90-30)
  t.forward(l/2-l/4/math.cos(30*math.pi/180))
  t.right(90-30)
  t.forward(l/4/math.cos(30*math.pi/180))
  t.right(30)
  t.forward(l/4)
  t.up()
  t.left(90)
  t.forward(l/2)
  t.left(90)
  t.forward(l/2)
  t.down()


def q():
  t.right(90)
  t.up()
  t.forward(l/3)
  t.down()
  t.right(180)
  t.forward(l/3/2)
  t.right(30)
  t.forward(l/3/2/math.cos(30*math.pi/180))
  t.right(90-30)
  t.forward(l-l/3/2/math.cos(30*math.pi/180))
  t.right(90-30)
  t.forward(l/3/2/math.cos(30*math.pi/180))
  t.right(30)
  t.forward(l/3/2)
  t.right(30)
  t.forward(l/3/2/math.cos(30*math.pi/180))
  t.right(90-30)
  t.forward(l-l/3/2/math.cos(30*math.pi/180))
  t.right(90-30)
  t.forward(l/3/2/math.cos(30*math.pi/180))
  t.right(30)
  t.right(180)
  t.up()
  t.forward(l/3/2)
  t.down()
  t.left(90+45)
  t.forward(l/3)
  t.backward(l/3)
  t.right(90+45)


def r():
  t.forward(l)
  t.right(90)
  t.forward(l/4)
  t.right(30)
  t.forward(l/4/math.cos(30*math.pi/180))
  t.right(90-30)
  t.forward(l/2-l/4/math.cos(30*math.pi/180))
  t.right(90-30)
  t.forward(l/4/math.cos(30*math.pi/180))
  t.right(30)
  t.forward(l/4)
  t.left(90+45)
  t.forward(l/2/math.cos(45*math.pi/180))
  t.left(45)


def s():
  t.right(90)
  t.forward(l/4)
  t.left(45) 
  t.forward(l/4/math.cos(45*math.pi/180))
  t.left(90)
  t.forward(2*l/4/math.cos(45*math.pi/180))
  t.right(90)
  t.forward(l/4/math.cos(45*math.pi/180))
  t.right(45)
  t.forward(l/4)
  t.right(90)
  t.up()
  t.forward(l)
  t.left(90)
  t.down()


def T():
  t.right(90)
  t.up()
  t.forward(l/4)
  t.left(90)
  t.down()
  t.forward(l)
  t.left(90)
  t.forward(l/4)
  t.backward(l/2)
  t.left(90)
  t.up()
  t.forward(l)
  t.left(90)
  t.down()


def u():
  t.up()
  t.forward(l)
  t.down()
  t.backward(l-l/3/2/2/math.cos(30*math.pi/180))
  t.left(60)
  t.backward(l/3/2/math.cos(30*math.pi/180))
  t.left(90-60)
  t.backward(l/3/2)
  t.left(90-60)
  t.backward(l/3/2/math.cos(30*math.pi/180))
  t.left(60)
  t.backward(l-l/3/2/2/math.cos(30*math.pi/180))
  t.up()
  t.forward(l)
  t.left(90)


def v():
  t.up()
  t.forward(l)
  t.down()
  t.backward(l-l/4/2/math.cos(75*math.pi/180))
  t.left(30)
  t.backward(l/4/math.cos(60*math.pi/180))
  t.left(90-30)
  t.left(90-30)
  t.backward(l/4/math.cos(60*math.pi/180))
  t.left(30)
  t.backward(l-l/4/2/math.cos(75*math.pi/180))
  t.up()
  t.forward(l)
  t.left(90)


def w():
  t.up()
  t.forward(l)
  t.down()
  t.backward(l-l/4/2/2/math.cos(75*math.pi/180))
  t.left(30)
  t.backward(l/4/2/math.cos(60*math.pi/180))
  t.left(90-30)
  t.left(90-30)
  t.backward(l/4/2/math.cos(60*math.pi/180))
  t.left(30)
  t.backward(l-l/4/2/2/math.cos(75*math.pi/180))
  t.right(180)
  t.backward(l-l/4/2/2/math.cos(75*math.pi/180))
  t.left(30)
  t.backward(l/4/2/math.cos(60*math.pi/180))
  t.left(90-30)
  t.left(90-30)
  t.backward(l/4/2/math.cos(60*math.pi/180))
  t.left(30)
  t.backward(l-l/4/2/2/math.cos(75*math.pi/180))
  t.up()
  t.forward(l)
  t.left(90)


def x():
  t.right(30)
  t.forward(l/math.cos(30*math.pi/180))
  t.left(30+90)
  t.up()
  t.forward(l/2/math.cos(30*math.pi/180))
  t.left(90+30)
  t.down()
  t.forward(l/math.cos(30*math.pi/180))
  t.left(2*30)


def y():
  t.right(30)
  t.forward(l/math.cos(30*math.pi/180))
  t.left(30+90)
  t.up()
  t.forward(l/2/math.cos(30*math.pi/180))
  t.left(90+30)
  t.down()
  t.forward(l/2/math.cos(30*math.pi/180))
  t.up()
  t.forward(l/2/math.cos(30*math.pi/180))
  t.left(2*30)
  t.down()

  
def z():
  t.up()
  t.forward(l)
  t.right(90)
  t.down()
  t.forward(l/2)
  t.right(180-63.435)
  t.forward(l/2/math.cos(63.435*math.pi/180))
  t.left(180-63.435)
  t.forward(l/2)


def espace():
  global color_i
  t.up()
  t.right(90)
  t.forward(l/2)
  t.down()
  color_i -= 1

def point():
  for i in range(4):
    t.forward(l/8)
    t.right(90)
  t.right(90)
  t.forward(l/8)

def virgule():
  t.forward(l/8)
  t.backward(l/8)
  t.right(90)

def point_excl():
  for i in range(4):
    t.forward(l/8)
    t.right(90)
  t.up()
  t.forward(l/4)
  t.down()
  t.forward(l*3/4)
  t.right(90)
  t.forward(l/8)
  t.right(90)
  t.forward(l*3/4)
  t.right(90)
  t.forward(l/8)
  t.up()
  t.left(90)
  t.forward(l/4)
  t.left(90)
  t.forward(l/8)
  t.down()
  

def apostrophe():
  t.up()
  t.forward(l*3/4)
  t.down()
  t.forward(l/4)
  t.up()
  t.backward(l)
  t.right(90)

def tiret():
  t.up()
  t.forward(l/2)
  t.right(90)
  t.down()
  t.forward(l/2)
  t.up()
  t.right(90)
  t.forward(l/2)
  t.left(90)
  t.down()

def newLine():
  global line,color_i
  t.up()
  t.setx(-1920/2+20)
  t.sety((1080-40)/2-(40+l)*(line+1))
  t.right(90)
  t.backward(l/8)
  line +=1
  color_i -= 1


  


def drawChar(char):
  switcher = {
    "a":a,
    "b":b,
    "c":c,
    "d":d,
    "e":e,
    "f":f,
    "g":g,
    "h":h,
    "i":i,
    "j":j,
    "k":k,
    "l":L,
    "m":m,
    "n":n,
    "o":o,
    "p":p,
    "q":q,
    "r":r,
    "s":s,
    "t":T,
    "u":u,
    "v":v,
    "w":w,
    "x":x,
    "y":y,
    "z":z,
    ".":point,
    ",":virgule,
    " ":espace,
    "-":tiret,
    "!":point_excl,
    "'":apostrophe,
    "\n":newLine
  }

  func = switcher.get(char, lambda: print("Erreur character"))
  func()

colors = ["#4285f4", "#ea4335", "#fbbc05", "#4285f4","#34a853","#ea4335"]
color_i = 0
def drawString(s):
  global drawing
  global color_i
  drawing = True
  t.down()
  t.left(90)
  
  for c in s:
    t.color(colors[color_i%6])
    color_i+=1
    drawChar(c)
    t.up()
    t.forward(l/8)
    t.down()
    t.left(90)
  t.right(90)
  drawing = False

buffers = []
drawing = False

def drawBuffer():
  if len(buffers)>0:
    if drawing == False:
      drawString(buffers.pop(0))

  

def drawKey(c):
  global buffers
  buffers.append(c)


def update():
    drawBuffer()
    screen.ontimer(update, 30)

def initialize():
    screen.title("AlphaTurtle")
    screen.delay(2)
    t.speed(10)
    t.pensize(5)
    screen.screensize()
    screen.setup(width=1.,height=1.,startx=None,starty=None)
    #x,y=screen.screensize()
    t.up()
    t.goto(-1920/2+20,(1080-40)/2-l-40)
    t.down()


def reset():
    global line,color_i
    t.reset()
    screen.delay(2)
    t.speed(10)
    t.pensize(5)
    line=1
    t.up()
    t.goto(-1920/2+20,(1080-40)/2-l-40)
    t.down()
    color_i = 0
    

screen = t.getscreen()
screen.listen()
screen.onkey(lambda: drawKey("a"),"a")
screen.onkey(lambda: drawKey("b"),"b")
screen.onkey(lambda: drawKey("c"),"c")
screen.onkey(lambda: drawKey("d"),"d")
screen.onkey(lambda: drawKey("e"),"e")
screen.onkey(lambda: drawKey("f"),"f")
screen.onkey(lambda: drawKey("g"),"g")
screen.onkey(lambda: drawKey("h"),"h")
screen.onkey(lambda: drawKey("i"),"i")
screen.onkey(lambda: drawKey("j"),"j")
screen.onkey(lambda: drawKey("k"),"k")
screen.onkey(lambda: drawKey("l"),"l")
screen.onkey(lambda: drawKey("m"),"m")
screen.onkey(lambda: drawKey("n"),"n")
screen.onkey(lambda: drawKey("o"),"o")
screen.onkey(lambda: drawKey("p"),"p")
screen.onkey(lambda: drawKey("q"),"q")
screen.onkey(lambda: drawKey("r"),"r")
screen.onkey(lambda: drawKey("s"),"s")
screen.onkey(lambda: drawKey("t"),"t")
screen.onkey(lambda: drawKey("u"),"u")
screen.onkey(lambda: drawKey("v"),"v")
screen.onkey(lambda: drawKey("w"),"w")
screen.onkey(lambda: drawKey("x"),"x")
screen.onkey(lambda: drawKey("y"),"y")
screen.onkey(lambda: drawKey("z"),"z")
screen.onkey(lambda: drawKey(","),",")
screen.onkey(lambda: drawKey(" ")," ")
screen.onkey(lambda: drawKey("'"),"'")
screen.onkey(lambda: drawKey("-"),"minus")
screen.onkey(lambda: drawKey("\n"),"Return")
screen.onkey(lambda: reset(), "Escape")
screen.onkey(lambda: print(), "Shift_L")
screen.onkey(lambda: drawKey("."), ".")
screen.onkey(lambda: drawKey("!"), "!")
screen.onkey(lambda: t.speed(0),"0")
screen.onkey(lambda: t.speed(1),"1")
screen.onkey(lambda: t.speed(2),"2")
screen.onkey(lambda: t.speed(3),"3")
screen.onkey(lambda: t.speed(4),"4")
screen.onkey(lambda: t.speed(5),"5")
screen.onkey(lambda: t.speed(6),"6")



initialize()
time.sleep(2)
drawString("hello, i'm alexandre, a student\nat telecom sudparis and\npresident of the programming\nclub.")
reset()
drawString("i love to solve problems with\ncode.\nin short, to study every area\nof computer science.")
reset()
#drawString("i want to become a dsc lead\nto enhance my club with the\nhelp of the dsc program.\nindeed, the members of our club\nwant to promote computer\nprogramming with training\nand challenges.")
drawString("i want to become a dsc lead\nto enhance my club thanks to\nthe dsc program.\n\n")
#reset()
#drawString("they also want to create\nsolutions for other clubs\nof our school.\n\n")
t.speed(10)
drawString("developed using turtle from\npython !!!")
reset()



update()

