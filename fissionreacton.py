import turtle
a=turtle.Turtle()
s=a.getscreen()
turtle.title("Fission")
s.bgcolor('black')
neutronlabel=turtle.Turtle()
neutronlabel.hideturtle()
neutronlabel.speed(300000000)
neutronlabel.color('white')
neutronlabel.penup()

neutronlabel.setposition(-270,-40)
neutronlabel.write("Neutron",font=('times new roman',20,'italic'))
neutron=turtle.Turtle()
neutron.shape('circle')
neutron.color('violet')
neutron.speed(30000000)
neutron.penup()
neutron.setx(-250)
neutron.shapesize(1)
uronium=turtle.Turtle()
uronium.speed(30000000)
uronium.color('yellow')
uronium.shape('circle')
uronium.shapesize(5)
uronium.penup()
uronium.setx(250)
uroniumlabel=turtle.Turtle()
uroniumlabel.hideturtle()
uroniumlabel.color('white')
uroniumlabel.penup()
uroniumlabel.setposition(210,-85)
uroniumlabel.write('Uronium-235',font=('times new roman',20,'italic'))
neutron1=turtle.Turtle()
neutron2=turtle.Turtle()
neutron3=turtle.Turtle()
neutron1.hideturtle()
neutron2.hideturtle()
neutron3.hideturtle()
neutron1.penup()
neutron2.penup()
neutron3.penup()
neutron1.setx(250)
neutron2.setx(250)
neutron2.left(60)
neutron3.setx(250)
neutron3.right(60)
neutron1.color('violet')
neutron2.color('violet')
neutron3.color('violet')
neutron1.shape('circle')
neutron2.shape('circle')
neutron3.shape('circle')
neutron1.shapesize(1)
neutron2.shapesize(1)
neutron3.shapesize(1)
daughter1=turtle.Turtle()
daughter1.hideturtle()
daughter2=turtle.Turtle()
daughter2.hideturtle()
daughter1.color('blue')
daughter2.color('green')

daughter1.shape('circle')
daughter2.shape('circle')
daughter1.shapesize(2.5)
daughter2.shapesize(2.5)
daughter1.penup()
daughter2.penup()
daughter1.setx(250)
daughter2.setx(250)
daughter1.left(90)
daughter2.right(90)
daughter1.speed(300000000)
daughter2.speed(300000000)
lbldgt1=turtle.Turtle()
lbldgt2=turtle.Turtle()
lbldgt1.hideturtle()
lbldgt2.hideturtle()
lbldgt1.penup()
lbldgt2.penup()
lbldgt1.goto(280,200)
lbldgt2.goto(280,-200)
lbldgt1.color('blue')
lbldgt2.color('green')
ntrlbl1=turtle.Turtle()
ntrlbl2=turtle.Turtle()
ntrlbl3=turtle.Turtle()
ntrlbl1.hideturtle()
ntrlbl2.hideturtle()
ntrlbl3.hideturtle()
ntrlbl1.color('violet')
ntrlbl2.color('violet')
ntrlbl3.color('violet')
ntrlbl1.penup()
ntrlbl2.penup()
ntrlbl3.penup()
ntrlbl1.setx(250)
ntrlbl2.setx(250)
ntrlbl3.setx(250)
ntrlbl2.left(60)
ntrlbl3.right(60)
ntrlbl1.setx(400)
ntrlbl1.sety(-10)
ntrlbl2.forward(100)
ntrlbl2.right(60)
ntrlbl2.forward(50)
ntrlbl2.right(90)
ntrlbl2.forward(10)
ntrlbl3.forward(100)
ntrlbl3.left(60)
ntrlbl3.forward(50)
ntrlbl3.right(90)
ntrlbl3.forward(10)
while True:
    neutronlabel.clear()
    uroniumlabel.clear()
    neutron.forward(7)
    if neutron.xcor()>=190 and neutron.xcor()<=200:
        neutron.hideturtle()
        neutronlabel.hideturtle()
        lbldgt1.write('Daughter 1',font=('times new roman',20,'italic'))
        lbldgt2.write('Daughter 2',font=('times new roman',20,'italic'))
        uronium.hideturtle()
        uroniumlabel.hideturtle()
        daughter1.showturtle()
        daughter2.showturtle()
        daughter1.forward(200)
        daughter2.forward(200)
        neutron1.showturtle()
        neutron2.showturtle()
        neutron3.showturtle()
        neutron1.forward(100)
        neutron2.forward(100)
        neutron3.forward(100)
        ntrlbl1.write('Neutron 1',font=('times new roman',15,'italic'))
        ntrlbl2.write('Neutron 2',font=('times new roman',15,'italic'))
        ntrlbl3.write('Neutron 3',font=('times new roman',15,'italic'))
        break




turtle.done()