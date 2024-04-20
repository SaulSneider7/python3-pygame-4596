import pygame

class Game:
    screen = None
    aliens = []

    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        done = False

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
            
            pygame.display.flip()
            self.clock.tick(60)
            self.screen.fill((0,0,0))

class Alien:
    def __init__(self, game, x, y):
        self.x = x
        self.game = game
        self.y = y
        self.size = 30
    
    def draw(self):
        pygame.draw.rect(self.game.screen,
                            (81,43,88), 
                            pygame.Rect(self.x, self.y, self.size, self.size))
        self.y += 0.05

class Generator:
    def __init__(selft, game):
        margin = 30
        width = 50
        for x in range(margin, game.width - margin, width):
            for y in range(margin, int(game.height / 2), width):
                game.aliens.append(Alien(game, x, y))

if __name__ == '__main__':
    game = Game(600, 400)