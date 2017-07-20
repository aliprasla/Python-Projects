import turtle
def draw_white_star(ttl,diameter):
  ttl.fillcolor('white')
  ttl.pencolor('white')
  ttl.begin_fill()
  for i in range(5):
    ttl.forward(diameter)
    ttl.right(140)
    ttl.forward(diameter)
    ttl.right(72 - 140)
  ttl.end_fill()
def fill_stars(ttl,hoist):
  canton_w = 1.9 * hoist * 2 / 5
  canton_h = hoist * 7 / 13
  ttl.penup()
  ttl.pencolor('white')
  ttl.fillcolor('white')
  xpos_orig = ttl.xcor()
  xpos = xpos_orig
  ypos = ttl.ycor()
  draw_star = True
  star_count = 0
  for k in range(9):
    ypos += canton_h / 10
    xpos = xpos_orig
    for i in range(11):
      xpos += canton_w / 14
      ttl.goto(xpos, ypos)
      if draw_star:
        ttl.goto(xpos + canton_w/42,ypos)
        ttl.begin_fill()
        #draw star here
        ttl.pendown()
        draw_white_star(ttl, hoist / 13 * 4 / 5/4)
        ttl.end_fill()
        draw_star = False
        xpos = ttl.xcor()
        ttl.penup()
        star_count += 1
        if star_count == 50:
          return 
      else:
        draw_star = True
        ttl.penup()
        xpos = ttl.xcor()
def draw_canton(ttl, hoist):
  #the canton is 2/5 of the width. which means it is .76 * the length
  #the canton's height is the same as the top 7 stripes - 7/13ths the length of the hoist
  ttl.penup()
  ttl.goto(-.8 * hoist, .5 * hoist - (7 * hoist/13))
  ttl.pendown()
  ttl.pencolor('blue')
  ttl.fillcolor('blue')
  ttl.begin_fill()
  ttl.goto(-.8 * hoist, .5 * hoist)
  ttl.goto(-.8 * hoist + .76*hoist, .5 * hoist)
  ttl.goto(-.8 * hoist + .76*hoist, .5 * hoist- (7 * hoist/13))
  ttl.goto(-.8 * hoist, .5 * hoist - (7 * hoist/13))
  ttl.end_fill()
  fill_stars(ttl,hoist)
def draw_stripes(ttl,hoist):
  #draws stripes
  ttl.fillcolor('red')
  ttl.pencolor('red')
  ypos = ttl.ycor()
  xpos = ttl.xcor()
  is_white = False
  for i in range (13):
    if is_white:
      xpos = -xpos
      ttl.goto(xpos,ypos)
      ypos += hoist/13
      ttl.goto(xpos,ypos)
      xpos += 1.6 * hoist
      ttl.goto(xpos,ypos)
      is_white = False
    else:
      ttl.begin_fill()
      xpos = -xpos
      ttl.goto(xpos,ypos)
      ypos += hoist/13
      ttl.goto(xpos,ypos)
      xpos += 1.6 * hoist
      ttl.goto(xpos,ypos)
      ttl.end_fill()
      is_white = True
def draw_initial(ttl,hoist):
  #sets up screen
  turtle.setup(200 + 1.9 * hoist,200 + hoist)
  #draws initial outline
  ttl.penup()
  ttl.goto(.8* hoist, -.5 * hoist)
  ttl.pendown()
  ttl.goto(.8* hoist,.5 * hoist)
  ttl.goto(-.8* hoist,.5 * hoist)
  ttl.goto(-.8* hoist,-.5 * hoist)
  ttl.goto(.8* hoist,-.5 * hoist)
  draw_stripes(ttl,hoist)
def adjust_edges(ttl,hoist):
  ttl.penup()
  ttl.goto(.8* hoist, -.5 * hoist)
  ttl.pencolor('black')
  ttl.pendown()
  ttl.goto(.8* hoist,.5 * hoist)
  ttl.goto(-.8* hoist,.5 * hoist)
  ttl.goto(-.8* hoist,-.5 * hoist)
  ttl.goto(.8* hoist,-.5 * hoist)
def main():
  length = eval(input("Enter vertical height of the flag in pixels : "))
  ttl = turtle.Turtle()
  ttl.speed(10)
  draw_initial(ttl,length)
  draw_canton(ttl,length)
  adjust_edges(ttl,length)
  ttl.hideturtle()
main()
