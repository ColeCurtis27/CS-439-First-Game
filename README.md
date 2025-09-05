# CS-439-First-Game

**Game overview**
- The theme of the game is a zombie-survival/defense game where the player has to kill as many zombies as they can without letting any cross the left boundary and get past them. Your goal is to get the highest score possible, and you get more score from killing more zombies. The flow should be constant movement and shooting as the player has a lot of zombies to keep up with. It should feel a little fast-paced.
  
**List of assets**
   - Hero/Player Character
   - Bullet or some sort of projectile
   - Zombie
   - scoreboard
   - background image if I get to it?

**Sprite details**

  **- Hero/Player Character:**
        
  Visual elements
         - tough/rugged man with long hair and a beard holding a projectile weapon
         
  Animation details
         - simple walk animation via a sprite sheet
         
  Life span
         - Born when the game starts. Never resets or dies
         
  Movement
         - Moves up and down with user input. Not allowed to move horizontally
         
  Boundary behavior
         - when leaving top or bottom of the screen, it should wrap around to the opposite border
         
  Collision behavior
         - this sprite won't have any collisions with any other sprite. Could work in a collision with the zombie, but not needed right now
         
**-Bullet or some sort of projectile:**

Visual elements
         - small projectile flying across the thing that coincides with the weapon of the player character (if using gun, will look like a small bullet, if using a bow, will look like a small arrow)
         
Animation details
         - no animations needed
         
Life span
         - child of the player character. Born when player presses the shoot button, and becomes hidden when it reaches the far right border
         
Movement
         - moves to the right at a constant speed
         
Boundary behavior
         - it should hide when it reaches the border and wait for the player to shoot again then it can reset and fly across the screen again
         
Collision behavior**
         - Can collide with the zombie sprite. This will add one to the score and cause the zombie sprite to reset
         
**-Zombie:**

Visual elements
         - green, injured human body not holding anything
         
Animation details
         - walk animation when moving left across the screen done with a sprite sheet
         
Life span
         - 5+ (depending on what I decide for balancing) are all born on the right side of the screen. Reset when colliding iwth an arrow and they die when they walk past the left border
         
Movement
         - moves to the left at a constant speed
         
Boundary behavior
         - once it passes he left border, the game quits
         
Collision behavior**
         - Can collide with the arrow sprite which will cause it to reset at a new y location and back on the right side of the screen


**GUI labels**
 - I will need a label to keep track of the player's score. It will be built with a LblScore class. It will be i nthe top left and will be updated via a collision detection.
   
**Game class initialization**

**-Appearance:** will be a blank background with a player on the left, zombies on the right, and a scoreboard in the top left

**-Sprites:** sprites will be created on running the game

**-GUI elements:** caption will show players the controls and what they should do
   
**-Other assets:** need a scoreboard which will be created on running the game each time
 
**Game class behavior**

 - The process method will check for detection between the zombie and the arrow and if there has been collision, it will call the zombie's reset method. This will also add 1 to the score variable. It will also check to see if any zombie has crossed the left boundary yet. If any has, it will quit the game and print out the player's score.
   
**Asset list**

 - Hero/Player Sprite
   
 - Zombie Sprite

 - Arrow Sprite

 - credits for assets: https://docs.google.com/document/d/1EJ9v3qDtRL_YUrpF3W0BdEmor1OCTOdbGdH_x566uWc/edit?usp=sharing
   
**Milestones**

1. Get the player and zombie characters moving as intended with placeholder shapes I make.
2. Write code for projectile and get the collision with zombie and zombie's reset working
3. Go get assets for these shapes I've created and cro pthe sprite sheets to just the walk animations for the player and the zombie. Write code to have the animations show on screen as intended.
4. Add scoreboard to keep track of score and print the end score to the console.
5. Play around with balancing adding more/less zombies and change the speed of the characters until I find something I like good enough

**STRETCH GOALS**
6. Find or even make a new background and add that in, along with some nice sound effects for shooting the bow and scoring a point.Could even add a walking sound effect for the player.
