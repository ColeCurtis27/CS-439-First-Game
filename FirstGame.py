import simpleGE, pygame, random

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.background.fill(pygame.Color("darkorange4"))
        self.setCaption("Use W/S To Move and Space to Shoot! Kill As Many Zombies As You Can!")
        self.player = Player(self)
        self.arrow = Arrow(self, self.player)
        self.numZombies = 5
        self.score = 0
        self.lblScore = LblScore()
        self.zombies = []
        for i in range(self.numZombies):
            self.zombies.append(Zombie(self))
        
        self.sprites = [self.player, self.arrow, self.zombies, self.lblScore]
        
    def doEvents(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.arrow.fire()
    
    def process(self):
        for zombie in self.zombies:        
            if zombie.collidesWith(self.arrow):
                zombie.reset()
                self.score += 1
                self.lblScore.text = f"Score: {self.score}"
            if zombie.checkBounds():
                print(f"Score: {self.score}")
                self.stop()

class Player(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.walkAnim = simpleGE.SpriteSheet("heroWalk1.png", (64, 64), 4, 9, 0.1)

        self.walkAnim.startCol = 1
        self.animRow = 2
        self.moveSpeed = 5
        
    def process(self):
        self.dx = 0
        self.dy = 0
        walking = False
        
        if self.isKeyPressed(pygame.K_w):
            self.animRow = 0
            self.dy = -self.moveSpeed
            walking = True
        if self.isKeyPressed(pygame.K_s):
            self.animRow = 2 
            self.dy = self.moveSpeed
            walking = True

        if walking:        
            self.copyImage(self.walkAnim.getNext(self.animRow))
        else:
            self.copyImage(self.walkAnim.getCellImage(0, self.animRow))
            
class LblScore(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Score: 0"
        self.center = (100, 30)
            
class Arrow(simpleGE.Sprite):
    def __init__(self, scene, parent):
        super().__init__(scene)
        self.parent = parent
        self.setImage("arrow.png")
        self.setBoundAction(self.HIDE)
        self.hide()

    def fire(self):
        if not self.visible:
            self.show()
            self.position = self.parent.position
            self.moveAngle = self.parent.imageAngle
            self.speed = 20
            
class Zombie(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.walkAnim = simpleGE.SpriteSheet("zombieWalk1.png", (64, 64), 4, 9, 0.1)

        self.walkAnim.startCol = 1
        self.animRow = 2
        self.moveSpeed = 2
        self.reset()
     
    def reset(self):
     self.x = 600
     
     self.y = random.randint(0, 479)
     
    def checkBounds(self):
        if self.right < 20:
            return True
        
    def process(self):
        self.dx = -2
        self.animRow = 1
        self.dx = -self.moveSpeed
        walking = True

        if walking:        
            self.copyImage(self.walkAnim.getNext(self.animRow))
        else:
            self.copyImage(self.walkAnim.getCellImage(0, self.animRow))

        
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()