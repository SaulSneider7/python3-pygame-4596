import pygame


class Game:
    screen = None
    aliens = []
    rockets = []            
    lost = False


    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        done = False

        hero = Hero(self, width / 2, height - 20)
        generator = Generator(self)
        rocket = None

        while not done:
            if len(self.aliens) == 44:
                #por ahora dejamos el valor de 44 para que se pueda apreciar el mensaje
                #luego deberia de ser 0 para ver que ganamos
                self.displayText("Ganaste el juego!")

            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_LEFT]:  
                hero.x -= 2 if hero.x > 20 else 0
            elif pressed[pygame.K_RIGHT]:
                hero.x += 2 if hero.x < width - 20 else 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not self.lost:
                    self.rockets.append(Rocket(self, hero.x, hero.y))

            pygame.display.flip()
            self.clock.tick(60)
            self.screen.fill((0, 0, 0))

            for alien in self.aliens:
                alien.draw()

            for rocket in self.rockets:
                rocket.draw()

            if not self.lost: hero.draw()

    def displayText(self, text):
            pygame.font.init()
            font = pygame.font.SysFont('Arial', 50)
            textsurface = font.render(text, False, (255, 255, 255))
            self.screen.blit(textsurface, (100, 160))




class Alien:
    def __init__(self, game, x, y):
        self.x = x
        self.game = game
        self.y = y
        self.size = 30

    def draw(self):
        pygame.draw.rect(self.game.screen,
                         (81, 43, 88),
                         pygame.Rect(self.x, self.y, self.size, self.size))
        self.y += 0.05


class Hero:
    def __init__(self, game, x, y):
        self.x = x
        self.game = game
        self.y = y

    def draw(self):

        pygame.draw.rect(self.game.screen,(210, 250, 251),pygame.Rect(self.x, self.y, 8, 5))


class Rocket:
    def __init__(self, game, x, y):
        self.x = x
        self.y = y
        self.game = game

    def draw(self):
        pygame.draw.rect(self.game.screen,
                         (254, 52, 110),
                         pygame.Rect(self.x, self.y, 2, 4))
        self.y -= 2


class Generator:
    def __init__(self, game):
        margin = 30
        width = 50
        for x in range(margin, game.width - margin, width):
            for y in range(margin, int(game.height / 2), width):
                game.aliens.append(Alien(game, x, y))



if __name__ == '__main__':
    game = Game(600, 400)