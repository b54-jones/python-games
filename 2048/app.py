import random

import pygame
from Square import Square

def getSquares():
    squares = []
    x = 120
    y = 120
    squaresToAdd = 16;

    while squaresToAdd > 0:
        square = Square(0, x, y)
        squares.append(square)
        x += 120
        if x == 600:
            x = 120
            y += 120
        squaresToAdd -= 1
    return squares

def moveAgain(square, secondSquare):
    if square.value == secondSquare.value:
        secondSquare.value *= 2
        square.value = 0
        global score
        score += secondSquare.value
        return False
    elif secondSquare.value == 0:
        secondSquare.value = square.value
        square.value = 0
        return True
    return False


def moveSquareUp(square, squares):
    if square.value == 0 or square.y == 120:
        return
    squareAbove = next((s for s in squares if s.x == square.x and s.y == square.y - 120), None)

    if squareAbove:
        if moveAgain(square, squareAbove):
            moveSquareUp(squareAbove, squares)

def moveSquaresUp(squares):
    sortedSquares = sorted(squares, key=lambda x: x.y, reverse=True)

    for square in sortedSquares:
        moveSquareUp(square, squares)
    return squares

def moveSquareDown(square, squares):
    if square.value == 0 or square.y == 580:
        return
    squareBelow = next((s for s in squares if s.x == square.x and s.y == square.y + 120), None)

    if squareBelow:
        if moveAgain(square, squareBelow):
            moveSquareDown(squareBelow, squares)

def moveSquaresDown(squares):
    sortedSquares = sorted(squares, key=lambda x: x.y, reverse=True)

    for square in sortedSquares:
        moveSquareDown(square, squares)
    return squares

def moveSquareLeft(square, squares):
    if square.value == 0 or square.x == 120:
        return
    squareLeft = next((s for s in squares if s.y == square.y and s.x == square.x - 120), None)

    if squareLeft:
        if moveAgain(square, squareLeft):
            moveSquareLeft(squareLeft, squares)


def moveSquaresLeft(squares):
    sortedSquares = sorted(squares, key=lambda x: x.x, reverse=True)

    for square in sortedSquares:
        moveSquareLeft(square, squares)
    return squares

def moveSquareRight(square, squares):
    if square.value == 0 or square.x == 580:
        return
    squareRight = next((s for s in squares if s.y == square.y and s.x == square.x + 120), None)

    if squareRight:
        if moveAgain(square, squareRight):
            moveSquareRight(squareRight, squares)


def moveSquaresRight(squares):
    sortedSquares = sorted(squares, key=lambda x: x.x, reverse=True)

    for square in sortedSquares:
        moveSquareRight(square, squares)
    return squares

def drawGameOverScreen():
    outer_color = (128, 128, 128)
    box = pygame.Rect(100, 100, 500, 500)
    pygame.draw.rect(screen, outer_color, box)
    drawCentralText("Game Over", box)
    pygame.display.update()

def addValueSquare(squares):
    filledSquares = [square for square in squares if square.value != 0]
    global gameOver
    if (len(filledSquares) == 15):
        gameOver = True
        drawGameOverScreen()
        return squares;

    placed = False

    while not placed:
        randomSquareIndex = random.randint(0, len(squares) - 1)
        square = squares[randomSquareIndex]

        if (square.value == 0):
            value = 4 if random.randint(0, 10) > 7 else 2
            square.value = value
            placed = True
    updateBoard(squares)
    return squares

def drawCentralText(text, box):
    font = pygame.font.SysFont(None, 48)
    text_color = (0,0,0)

    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect()
    text_rect.center = box.center
    screen.blit(text_surface, text_rect)

def drawSquares(squares):

    for square in squares:
        rect = pygame.Rect(square.x, square.y, 100, 100)
        pygame.draw.rect(screen, square.get_color(), rect)

        if square.value != 0:
            drawCentralText(str(square.value), rect)

def drawScore():
    background_color = (255, 255, 255)
    pygame.draw.rect(screen, background_color, pygame.Rect(100, 60, 200, 40))

    font = pygame.font.SysFont(None, 48)
    score_color = (0,0,0)
    score_text = font.render("Score: " + str(score), True, score_color)

    screen.blit(score_text, (100, 60))
def updateBoard(squares):
    outer_color = (128, 128, 128)
    pygame.draw.rect(screen, outer_color, pygame.Rect(100, 100, 500, 500))
    drawSquares(squares)
    drawScore()
    pygame.display.update()

def setUpBoard():
    squares = getSquares()
    squares = addValueSquare(squares)
    squares = addValueSquare(squares)
    return squares

pygame.init()

(width, height) = (700, 700)
score = 0
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("2048")

background_color = (255, 255, 255)
screen.fill(background_color)

squares = setUpBoard()
updateBoard(squares)

running = True
gameOver = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and not gameOver:
            if event.key == pygame.K_UP:
                squares = moveSquaresUp(squares)
                squares = addValueSquare(squares)
            elif event.key == pygame.K_DOWN:
                squares = moveSquaresDown(squares)
                squares = addValueSquare(squares)
            elif event.key == pygame.K_RIGHT:
                squares = moveSquaresRight(squares)
                squares = addValueSquare(squares)
            elif event.key == pygame.K_LEFT:
                squares = moveSquaresLeft(squares)
                squares = addValueSquare(squares)
        elif event.type == pygame.KEYDOWN and gameOver:
            if event.key == pygame.K_SPACE:
                gameOver = False
                score = 0
                squares = setUpBoard()
                updateBoard(squares)



pygame.quit()