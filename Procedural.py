import pygame # type: ignore
import math
pygame.init()

screen = pygame.display.set_mode((1200, 800))
pygame.mouse.set_visible(False)
x2, y2 = 0,0

class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def AngleToDot(self, x2, xy):
        return math.atan2(y2-self.y, x2-self.x)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Background
    screen.fill((213,211,211))

    # Head
    x1, y1 = pygame.mouse.get_pos()
    pygame.draw.circle(screen, (158,69,72), (x1, y1), 10)
    pygame.draw.circle(screen, (80,80,80), (x1, y1), 50, 2)


    # Find the angle from Head to Spine
    angle = math.atan2(y2-y1, x2-x1)
    # Find new position
    x2 = x1 + 50 * math.cos(angle)
    y2 = y1 + 50 * math.sin(angle)
    # Draw Spine
    pygame.draw.circle(screen, (158,69,72), (x2, y2), 10)

    # Update display
    pygame.display.flip() 

# Quit Pygame
pygame.quit()