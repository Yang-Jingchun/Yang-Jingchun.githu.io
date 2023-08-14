import js
p5 = js.window

space_img=p5.loadImage('assets/space.jpeg')

exploding = p5.loadSound('assets/explode.mp3')
win = p5.loadSound('assets/win.mp3')
popping = p5.loadSound('assets/pop.mp3')

class Sprite:
  def __init__(self, x = 0, y = 0,speed=1,width=0, height=0):
    self.x = x
    self.y = y
    self.width=width
    self.height=height
    
    self.speed = speed

  def update(self):
    if(self.y < p5.height + self.height/2):
      self.y += self.speed
    else:
      self.y = -self.height/2

class EnergyBall(Sprite):
  def __init__(self,x=p5.random(p5.width),y=p5.random(p5.height),speed=1, width=60, height=60):
    self.x = x  
    self.y = y
    self.speed = speed
    self.width = width
    self.height = height
    self.img=p5.loadImage('assets/energy ball.png')

  def update(self):
    if(self.y < p5.height + self.height/2):
      self.y += self.speed
    else:
      self.y = -self.height/2
    
  def draw(self,x=100,y=100,width=60,height=60):
    p5.tint(255, 200)
    p5.push()
    p5.translate(self.x, self.y)
    p5.image(self.img,0,0,width,height)
    p5.pop()

energyBall_list = []  # empty list
for i in range(15):
  energyBall=EnergyBall(x=p5.random(400), y=p5.random(-1800,0))
  energyBall_list.append(energyBall)

      

class FireBall(Sprite):
  def __init__(self, x,y,speed=1,width=70,height=70):
    self.x = x  
    self.y = y
    self.speed=speed
    self.width = width
    self.height = height
    self.img=p5.loadImage('assets/fireball.png')

  def update(self):
    if(self.y < p5.height + self.height/2):
      self.y += self.speed
    else:
      self.y = -self.height/2
      
  def draw(self):
    p5.tint(255, 200)
    p5.push()
    p5.translate(self.x, self.y)
    p5.image(self.img,0,0,self.width,self.height)
    p5.pop()
    
fireBall_list = []  # empty list
for i in range(10):
  fireBall=FireBall(x=p5.random(400), y=p5.random(-1200,0))
  fireBall_list.append(fireBall)


class Rocket:
  def __init__(self):
    self.x = 200
    self.y = 550
    self.img=p5.loadImage('assets/rocket.png')
  
  def draw(self, width=40, height=100):
    p5.push()
    p5.translate(self.x, self.y)
    p5.image(self.img, 0, 0, width, height)
    p5.pop()

rocket=Rocket()

class RocketUpdate:
  def __init__(self):
    self.x=200
    self.y=250
    self.img=p5.loadImage('assets/rocket update.png')

  def draw(self, width=250, height=300):
    p5.tint(255, 255)
    p5.push()
    p5.translate(self.x,self.y)
    p5.image(self.img, 0,0,width,height)
    p5.pop()

rocketUpdate=RocketUpdate()
      

class Start:
  def __init__(self):
    self.x = 200
    self.y = 300
    self.img=p5.loadImage('assets/Play.png')
  
  def draw(self, width=150, height=50):
    p5.push()
    p5.translate(self.x, self.y)
    p5.image(self.img, 0, 0, width, height)
    p5.pop()

start=Start()


program_state='START'

energy_point=0
prev_energy_point=0

class Explode:
  def __init__(self):
    self.x=200
    self.y=550
    self.img=p5.loadImage('assets/explode.png')

  def draw(self, width=150, height=150):
    p5.tint(255, 255)
    p5.push()
    p5.translate(self.x,self.y)
    p5.image(self.img,0,0,width, height)
    p5.pop()


explode=Explode()


class Plus:
  def __init__(self):
    self.x=200
    self.y=550
    self.timer = 0
    self.img=p5.loadImage('assets/+1.png')

  def draw(self, width=40, height=50):
    # self.timer = p5.millis() 
    # popping.play()
    p5.tint(255,255)
    p5.push()
    p5.translate(self.x,self.y)
    # if(p5.millis() % 2000 < 1000):
    p5.image(self.img,0,0,width, height)
    
    # if(p5.millis() > self.timer + 1000):
    #   p5.image(self.img,0,0,width, height)
    #   self.timer = p5.millis()
      
    p5.pop()

plus=Plus()

class MissionFailed:
  def __init__(self):
    self.x= 200
    self.y= 300
    self.img=p5.loadImage('assets/mission_failed.png')

  def draw(self,width=400,height=200):
    p5.tint(255, 255)
    p5.push()
    p5.translate(self.x,self.y)
    p5.image(self.img,0,0,width, height)
    p5.pop()

missionFailed=MissionFailed()

class LevelUp:
  def __init__(self):
    self.x=200
    self.y=450
    self.img=p5.loadImage('assets/LevelUp.png')

  def draw(self,width=260, height=80):
    p5.tint(255, 255)
    p5.push()
    p5.translate(self.x,self.y)
    p5.image(self.img,0,0,width, height)
    p5.pop()

levelUp=LevelUp()
    

def setup():
  p5.createCanvas(400, 600) 
  p5.imageMode(p5.CENTER)

  

def draw():
  global program_state, energy_point, fireBall_list, prev_energy_point, win,exploding,plus
  
  p5.background(0) 
  p5.fill(0)  # fill with black
  p5.noStroke()  # no stroke
  # show cursor coordinates:
  p5.text((int(p5.mouseX), int(p5.mouseY)), 10, 20)
  p5.strokeWeight(1)  # 1-pixel stroke

  p5.tint(255, 130)
  p5.image(space_img,100,300,900,600)

  p5.tint(255, 255)

  p5.textFont('Din Pro')
  p5.textSize(20)
  p5.fill(198,205,255)
  p5.text((f'Energy Point: {energy_point}/10'), 10, 30)


  if(program_state == 'START'):
    p5.fill(255)
    start.draw()
    
  if(program_state == 'PLAY'):

    if(p5.keyIsPressed == True):
      if(p5.keyCode == p5.RIGHT_ARROW):
        if(rocket.x < p5.width - 20):
          rocket.x += 2
      elif(p5.keyCode == p5.LEFT_ARROW):
        if(rocket.x > 20):     #20: the width of rocket
          rocket.x -= 2
          
    rocket.draw()

    
    i = 0
    while i < len(energyBall_list):
      energyBall = energyBall_list[i]
      energyBall.update()
      energyBall.draw()
    
      d_energy = p5.dist(energyBall.x, energyBall.y, rocket.x, rocket.y)
      
      if (d_energy < 40):
        energyBall_list.pop(i)  # Use pop() to remove this energy ball from the list
        energy_point += 1
        print('collide with energy ball..')
        popping.play()  
        plus.timer = p5.millis()  # update timer
        # plus.x=rocket.x
        # plus.y=rocket.y-50
        # plus.draw()

      # if (energy_point>prev_energy_point):
          
          # elapsedTime = p5.millis() - plus.startTime
        
      
        
    
        #plus.timer = p5.millis() 


      


      # prev_energy_point=energy_point

    
        # Initiate a new energy ball to replace the removed one:
        # newEnergyBall = EnergyBall(x=p5.random(400), y=p5.random(-1800,0))
        # energyBall_list.append(newEnergyBall)  # Append the new EnergyBall to the list
    
        #print('energy point', energy_point)
        #continue  
    
      i += 1
    
          
      if(energy_point == 10):
        program_state = 'WIN'

    if(p5.millis() < plus.timer + 1000):
      plus.x=rocket.x
      plus.y=rocket.y-50
      plus.draw()
      # popping.play()

    
    i=0 #counter variable
    while (i<len(fireBall_list)):
        # for i in range(3): increase 1
      fireBall=fireBall_list[i]
      fireBall.update()
      fireBall.draw()
  
      i+=1
  
      d_fire = p5.dist(fireBall.x, fireBall.y, rocket.x, rocket.y)
      # print(d_energy)
  
      if(d_fire < 40):  
        program_state='LOSE'
        print(program_state)  

  if (program_state=='LOSE'):
    
    missionFailed.draw()
    
    explode.x=rocket.x
    explode.y=rocket.y-50
    explode.draw()

    exploding.play()
    p5.delay(2000)
    # exploding.stop()






  if (program_state=='WIN'):
    rocketUpdate.draw()
    levelUp.draw()

    win.play()
    p5.delay(2000)
    win.stop()
  





      


  # # energyBall.draw()
  # i = 0  # loop counter variable
  # while(i < len(energyBall_list)):
  #   EnergyBall = energyBall_list[i]
  #   # invader.update()
  #   energyBall.draw()
  


  

  



  # p5.image(house_img,changing_house[0],100,100,100)
  # p5.image(house_img,changing_house[0],100,100,100)
  
def keyPressed(event):
  print('key pressed.. ' + p5.key)

def keyReleased(event):
  pass
  
def mousePressed(event):
  global program_state
  
  if(program_state == 'START'):
    program_state = 'PLAY'
    print('program_state = ' + program_state)

def mouseReleased(event):
  pass
