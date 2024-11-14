from Card import Card
import pygame

def buildDeck():
    NO_OF_CARDS = 53

    i = 1

    cards = []
    suits = ['hearts', 'diamonds', 'clubs', 'spades']
    current_suit = 0
    current_card_value = 1

    while i < NO_OF_CARDS:
        suit = suits[current_suit]
        value = current_card_value
        if value == 11:
            value = 'J'
        elif value == 12:
            value = 'Q'
        elif value == 13:
            value = 'K'
        card = Card(value, suit)
        current_card_value += 1
        cards.append(card)
        if i % 13 == 0:
            current_suit += 1
            current_card_value = 1
        i+=1
    return cards

def drawHand(screen, hand):
    current_x = 41
    for card in hand:
        card.draw(screen, current_x)
        current_x += 191

def drawCentralText(screen, box, text, fontSize):
    pygame.font.init()
    font = pygame.font.SysFont(None, fontSize)
    text_color = (0,0,0)
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect()
    text_rect.center = box.center
    screen.blit(text_surface, text_rect)

def scoreHand(hand):
    score = 0
    for card in hand:
        if card.value in ['Q', 'K', 'J']:
            score += 10
        else:
            score += card.value
    return score