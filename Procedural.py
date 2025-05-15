import pygame # type: ignore
import math
pygame.init()

screen = pygame.display.set_mode((1200, 800))
pygame.mouse.set_visible(False)

class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (158, 69, 72)
        self.borderColor = (80, 80, 80)
        self.constraint = constraint
        self.radius = radius

    def ConstrainToDot(self, dot):
        angle = math.atan2(self.y-dot.y, self.x-dot.x)
        self.x = dot.x + self.constraint * math.cos(angle)
        self.y = dot.y + self.constraint * math.sin(angle)

    def Draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius, 4)

    def DrawConstraint(self):
        pygame.draw.circle(screen, self.borderColor, (self.x, self.y), self.constraint, 2)

# Initialize Spines
constraint = 50
radius = 10
spines = []
size = [52, 58, 40, 60, 68, 71, 65, 50, 28, 15, 11, 9, 7, 7, 7]
for _ in range(15):
    spines.append(Dot(0, 0))
for i in range(len(spines)):
    spines[i].radius = size[i]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Background
    screen.fill((213,211,211))

    # Head
    x, y = pygame.mouse.get_pos()
    spines[0].x = x
    spines[0].y = y
    spines[0].Draw()
    #spines[0].DrawConstraint()

    # Spine
    for i in range(1, len(spines)):
        spines[i].ConstrainToDot(spines[i - 1])
        spines[i].Draw()
        #spines[i].DrawConstraint()

    # Update display
    pygame.display.flip() 

# Quit Pygame
pygame.quit()