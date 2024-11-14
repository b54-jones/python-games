import random

import pygame.display
import random
from Card import Card
from functions import *

cards = buildDeck()
hand = []

(width, height) = (1000, 500)
score = 0
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Blackjack")

background_color = (128, 128, 128)

def drawACard():
    if len(hand) == 5:
        return
    card = random.choice(cards)
    hand.append(card)
    cards.remove(card)
    drawHand(screen, hand)

grey = (224,224,224)
twist_rect = pygame.Rect(191, 425, 300, 50)
stick_rect = pygame.Rect(516, 425, 300, 50)

def setUpGame():
    hand.clear()
    screen.fill(background_color)
    pygame.draw.rect(screen, grey, stick_rect)
    drawCentralText(screen, stick_rect, "Stick", 18)
    pygame.draw.rect(screen, grey, twist_rect)
    drawCentralText(screen, twist_rect, "Twist", 18)
    cards = buildDeck()
    drawACard()
    drawACard()
    pygame.display.update()
    global gameOver
    gameOver = False

def displayHelperText():
    helperTextArea = pygame.Rect(0, 0, 1000, 100)
    drawCentralText(screen, helperTextArea, "Click anywhere to restart...", 36)

setUpGame()

running = True
gameOver = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if gameOver:
                setUpGame()
            elif twist_rect.collidepoint(event.pos):
                drawACard()
                if scoreHand(hand) > 21:
                    print("Bust! You lose.")
                    gameOver = True
                    displayHelperText()
                pygame.display.update()
            elif stick_rect.collidepoint(event.pos):
                opposing_score = random.randint(15,21)
                handScore = scoreHand(hand)
                if opposing_score < handScore or len(hand) == 5:
                    print("You win! Opposing score was: " + str(opposing_score))
                elif opposing_score == handScore:
                    print("It's a draw! Opposing score was: " + str(opposing_score))
                else:
                    print("You lose! Opposing score was: " + str(opposing_score))
                gameOver = True
                displayHelperText()
                pygame.display.update()






