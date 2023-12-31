import pygame
import time

"""class Map():

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
            posx = initial_posx"""


class Worm():
    def __init__(self, screen, posx, posy, size, speed):
        self.screen = screen
        self.posx = posx
        self.posy = posy
        self.size = size
        self.speed = speed


        
        self.facing = "right"
        self.previous_facing = self.facing
        self.facing_number = 0

        self.up = False
        self.down = False
        self.right = False
        self.left = False
        

        self.part = pygame.Rect(self.posx, self.posy, self.size, self.size)
        self.length = [self.part]

        self.worm_butt_last_position_x = self.posx
        self.worm_butt_last_position_y = self.posy

        self.turning_cord = None

        self.done = False


    def reset_values(self):
        self.done = False


    def update(self):

        #UPPDATERAR ORMEN
        self.part = pygame.Rect(self.posx, self.posy, self.size, self.size)
        self.worm_butt_last_position_x = self.posx
        self.worm_butt_last_position_y = self.posy

        self.length = [self.part]
        for part in self.length:
            pygame.draw.rect(self.screen, (255, 255, 255), part, 1)



        #The snake wont turn until it is perfectly linear with the track, the snake cannot make it out of track.
        perfect_line_with_x = (self.posx/self.speed)/4 % 1
        perfect_line_with_y = (self.posy/self.speed)/4 % 1

        if self.facing == "up":
            if perfect_line_with_x == 0:
                self.posy = self.posy - self.speed
                if not self.done:
                    self.turning_cord = self.posx, self.posy + 5
                    print("this is yeah", self.turning_cord)
                    self.done = True
            else:
                if self.previous_facing == "left":
                    self.posx = self.posx - self.speed

                if self.previous_facing == "right":
                    self.posx = self.posx + self.speed

        if self.facing == "down":
            if perfect_line_with_x == 0:
                self.posy = self.posy + self.speed
                

            else:
                if self.previous_facing == "left":
                    self.posx = self.posx - self.speed

                if self.previous_facing == "right":
                    self.posx = self.posx + self.speed
                self.turning_cord = self.posx, self.posy - 20
                print("this is yeah", self.turning_cord)

        if self.facing == "left":
            if perfect_line_with_y == 0:
                self.posx = self.posx - self.speed
            else:
                if self.previous_facing == "up":
                    self.posy = self.posy - self.speed
                
                if self.previous_facing == "down":
                    self.posy = self.posy + self.speed

        if self.facing == "right":
            if perfect_line_with_y == 0:
                self.posx = self.posx + self.speed
            else:
                if self.previous_facing == "up":
                    self.posy = self.posy - self.speed
                
                if self.previous_facing == "down":
                    self.posy = self.posy + self.speed
        

        
        

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.up == False and self.facing_number != 1 and self.facing != "down":
            self.facing_number = 1
            self.previous_facing = self.facing
            self.facing = "up"
            self.reset_values()
            print(self.previous_facing)

        if keys[pygame.K_DOWN] and self.down == False and self.facing_number != 2  and self.facing != "up":
        if keys[pygame.K_DOWN] and self.down == False and self.facing_number != 2 and self.facing != "up":
            self.facing_number = 2
            self.previous_facing = self.facing
            self.facing = "down"
            self.reset_values()
            print(self.previous_facing)


        if keys[pygame.K_LEFT] and self.left == False and self.facing_number != 3 and self.facing != "right":
            self.facing_number = 3
            self.previous_facing = self.facing
            self.facing = "left"
            self.reset_values()
            print(self.previous_facing)

        if keys[pygame.K_RIGHT] and self.right == False and self.facing_number != 4 and self.facing != "left":
            self.facing_number = 4
            self.previous_facing = self.facing
            self.facing = "right"
            self.reset_values()
            print(self.previous_facing)

        if keys[pygame.K_SPACE]:
            pass
        

    def eat(self):
        pass







class Food():
    def __init__(self, screen):
        self.screen = screen
        self.posx, self.posy = 300, 300
        self.size = 20
        self.part = pygame.Rect(self.posx, self.posy, self.size, self.size)

    
    def update(self):
        pygame.draw.rect(self.screen, (255, 0, 0), self.part)

    