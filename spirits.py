import pygame
import time

class Map():

    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
    

    def spawn_blocks(self, posx, posy, width, height):
        blocks_x = self.screen_width/width
        blocks_y = self.screen_height/height
        initial_posx = posx


        for b in range(int(blocks_y)):
            for b in range(int(blocks_x)):
                block = pygame.Rect(posx, posy, width, height)
                posx = posx + width
                pygame.draw.rect(self.screen, (255, 255, 0), block, 1)
                b += 1
                print(b)
            posy = posy + height
            posx = initial_posx


class Worm():
    def __init__(self, screen, posx, posy, size, speed):
        self.screen = screen
        self.posx = posx
        self.posy = posy
        self.size = size
        self.speed = speed


        self.length = 1
        self.facing = "right"
        self.previous_facing = self.facing

        self.up = False
        self.down = False
        self.right = False
        self.left = False
        

        self.part = pygame.Rect(self.posx, self.posy, self.size, self.size)

        self.worm_butt_last_position_x = self.posx
        self.worm_butt_last_position_y = self.posy


    def reset_values(self):
            self.up = False
            self.down = False
            self.left = False
            self.right = False

    def update(self):
        za = (self.posx/self.speed)/4 % 1
        ba = (self.posy/self.speed)/4 % 1
        #time.sleep(0.13)
        #self.worm_butt_last_position_x = self.posx
        #self.worm_butt_last_position_y = self.posy

        self.part = pygame.Rect(self.posx, self.posy, self.size, self.size)
        pygame.draw.rect(self.screen, (255, 255, 255), self.part, 1)


        if self.facing == "up":
            if za == 0:
                self.posy = self.posy - self.speed
            else:
                if self.previous_facing == "left":
                    self.posx = self.posx - self.speed

                if self.previous_facing == "right":
                    self.posx = self.posx + self.speed

                
        if self.facing == "down":
            if za == 0:
                self.posy = self.posy + self.speed
            else:
                if self.previous_facing == "left":
                    self.posx = self.posx - self.speed

                if self.previous_facing == "right":
                    self.posx = self.posx + self.speed

        if self.facing == "left":
            if ba == 0:
                self.posx = self.posx - self.speed
            else:
                if self.previous_facing == "up":
                    self.posy = self.posy - self.speed
                
                if self.previous_facing == "down":
                    self.posy = self.posy + self.speed

        if self.facing == "right":
            if ba == 0:
                self.posx = self.posx + self.speed
            else:
                if self.previous_facing == "up":
                    self.posy = self.posy - self.speed
                
                if self.previous_facing == "down":
                    self.posy = self.posy + self.speed
        

        
        

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.up == False:
            self.up = True
            self.previous_facing = self.facing
            self.facing = "up"
            
            print(self.previous_facing)

        if keys[pygame.K_DOWN] and self.down == False:
            self.down = True
            self.previous_facing = self.facing
            self.facing = "down"
            print(self.previous_facing)


        if keys[pygame.K_LEFT] and self.left == False:
            self.left = True
            self.previous_facing = self.facing
            self.facing = "left"
            print(self.previous_facing)

        if keys[pygame.K_RIGHT] and self.right == False:
            self.right = True
            self.previous_facing = self.facing
            self.facing = "right"
            print(self.previous_facing)

        if keys[pygame.K_SPACE]:
            pass
        

    def eat(self):
        pass







class Food():
    def __init__(self) -> None:
        pass




class asd(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Load the sprite image
        #self.image = pygame.image.load('path_to_your_image.png')
        #self.image = pygame.transform.scale(self.image, (50, 50))  # Scale the image to a suitable size

        # Get the rectangle object from the image which will be used for positioning
        #self.rect = self.image.get_rect()
        self.hitbox = pygame.Rect(100, 100, 100, 100)
        #self.rect.x = 100  # Initial X position
        #self.rect.y = 100  # Initial Y position

    def update(self):
        # Update the sprite's position and behavior
        self.rect.x += 1  # Move the sprite to the right every frame

    