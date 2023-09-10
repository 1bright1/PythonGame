import pygame

class Player(): # class for game character/player
    def __init__(self, x, y, width, height, color): #x and y are the positions of player
        self.x = x #initializing variables. Think of it like this.x = x. remember the "this function" used in java. self is an object/player for this function
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.val = 6 # self.val is the unit space a player can move in any direction
        self.rect = (x,y,width,height)
        # New attributes for animation
        self.animation_step = 0
        self.animation_direction = 1

    def draw(self, window): #draw the shape of the character. in this case it will be rectangle hence rect function
        #pygame.draw.rect(window,self.color,self.rect)
        # Draw stick figure parts
        head_radius = self.width // 4
        head_center = (self.x + self.width // 2, self.y + head_radius)
        pygame.draw.circle(window, self.color, head_center, head_radius)

        # Calculate leg positions based on the animation step and direction
        leg_step = self.animation_step * 2  # Multiply by 2 to increase the leg movement
        left_leg_end = (self.x + self.width // 4, self.y + self.height + leg_step)
        right_leg_end = (self.x + 3 * self.width // 4, self.y + self.height - leg_step)

        body_end = (self.x + self.width // 2, self.y + 2 * head_radius)
        pygame.draw.line(window, self.color, head_center, body_end, 2)
        pygame.draw.line(window, self.color, body_end, left_leg_end, 2)
        pygame.draw.line(window, self.color, body_end, right_leg_end, 2)

        left_leg_end = (self.x + self.width // 4, self.y + self.height)
        pygame.draw.line(window, self.color, body_end, left_leg_end, 2)

        right_leg_end = (self.x + 3 * self.width // 4, self.y + self.height)
        pygame.draw.line(window, self.color, body_end, right_leg_end, 2)

        left_arm_end = (self.x, self.y + head_radius + self.height // 4)
        pygame.draw.line(window, self.color, body_end, left_arm_end, 2)

        right_arm_end = (self.x + self.width, self.y + head_radius + self.height // 4)
        pygame.draw.line(window, self.color, body_end, right_arm_end, 2)

    def move(self, redraw_function, window, play, play2): # move player
        keys = pygame.key.get_pressed()  # checks if certain keys (on the keyboard) are pressed then change the x and y values

        if keys[pygame.K_LEFT]: #yooooo if you do pygame.K... you will see the different keys on a keyboard incase one is pressed
            self.x -= self.val

        if keys[pygame.K_RIGHT]:
            self.x += self.val

        if keys[pygame.K_UP]:
            self.y  -= self.val # the operation= those are just the standard for moving up,down,right,left

        if keys[pygame.K_DOWN]:
            self.y += self.val

        # Implement walking animation
        self.animation_step += self.animation_direction
        if self.animation_step >= 6:  # Set the maximum leg movement step (adjust as needed)
            self.animation_direction = -1
        elif self.animation_step <= 0:
            self.animation_direction = 1

        # Implement a simple animation while moving
        # You can modify these values based on your desired animation
        animation_length = 8
        if any(keys):
            pygame.time.delay(50)
            for i in range(animation_length):
                pygame.event.pump()
                self.update()
                redraw_function(window, play, play2)  # Call the passed redraw function
                pygame.time.delay(10)

        self.update()

    def update(self):
        self.rect = (self.x,self.y,self.width,self.height)
        # Add boundary checks to prevent the player from going off-screen
        window_width = 500
        window_height = 500
        if self.x < 0:
            self.x = 0
        elif self.x > window_width - self.width:
            self.x = window_width - self.width
        if self.y < 0:
            self.y = 0
        elif self.y > window_height - self.height:
            self.y = window_height - self.height







