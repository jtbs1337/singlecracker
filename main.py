from spirits import *




pygame.init()

class Game():

    def __init__(self, screen_width, screen_height, spirit_size):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.spirit_size = spirit_size

        self.screen = pygame.display.set_mode((self.screen_width, screen_height))
        self.map = Map(self.screen, self.screen_width, self.screen_height)
        self.worm = Worm(self.screen, posx=600, posy=600, size=20, speed=5)

        self.clock = pygame.time.Clock()


    def run(self):
        map_done = False
        while True:
            self.clock.tick(60)
            self.screen.fill((0, 0, 0))
    
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            
            self.worm.update()


            # Game logic goes here
            if not map_done:
                self.map.spawn_blocks(0, 0, self.spirit_size, self.spirit_size)
                map_done = True
                #x = (260/5)/4 % 1
                #print("hello", x)
                

    

            # Update the display
            
            pygame.display.flip()
            
            

if __name__ == "__main__":
    game = Game(1000, 800, 20)
    game.run()
    