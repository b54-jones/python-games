import pygame

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def draw(self, screen, x):
        y = 100
        white = (255, 255, 255)
        black = (0,0,0)
        pygame.draw.rect(screen, black, pygame.Rect(x-2, y-2, 154, 304))

        innerCard = pygame.Rect(x, y, 150, 300)
        pygame.draw.rect(screen, white, innerCard)

        image = pygame.image.load('img/' + self.suit + '.png')
        resized_image = pygame.transform.scale(image, (50, 50))

        screen.blit(resized_image, (x, y))
        screen.blit(resized_image, (x+100, y))
        screen.blit(resized_image, (x, y+250))
        screen.blit(resized_image, (x+100, y+250))

        self.drawCardText(screen, innerCard)

    def drawCardText(self, screen, box):
        pygame.font.init()
        text = str(self.value)
        font = pygame.font.SysFont(None, 72)
        text_color = (0,0,0)
        text_surface = font.render(text, True, text_color)
        text_rect = text_surface.get_rect()
        text_rect.center = box.center
        screen.blit(text_surface, text_rect)

