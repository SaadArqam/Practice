import pygame
import random
import math
import time

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Symbol Decoding")

# Colors
BLACK = (0, 0, 0)
GLOW_COLOR = (0, 255, 0)
PARTICLE_COLOR = (0, 255, 128)

# Fonts
font = pygame.font.SysFont("Arial", 120)

# Alien symbols
alien_symbols = ['@', '#', '%', '&', '!', '*', '?', 'π', 'ν', 'Σ', 'λ', 'ξ']

# Particle class
class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = random.randint(3, 6)
        self.speed_x = random.uniform(-1, 1)
        self.speed_y = random.uniform(-1, 1)
        self.alpha = 255

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.alpha -= 5  # Reduce alpha to fade out the particle
        if self.size > 0.1:
            self.size -= 0.1

    def draw(self, surface):
        if self.alpha > 0:
            s = pygame.Surface((self.size * 2, self.size * 2), pygame.SRCALPHA)
            pygame.draw.circle(s, PARTICLE_COLOR + (self.alpha,), (self.size, self.size), self.size)
            surface.blit(s, (self.x, self.y))

# Function to render glowing symbols
def render_glowing_symbol(symbol, x, y, frame_count):
    glow_surface = font.render(symbol, True, GLOW_COLOR)
    glow_intensity = int(255 * (math.sin(frame_count / 20) + 1) / 2)
    glow_surface.set_alpha(glow_intensity)
    screen.blit(glow_surface, (x - glow_surface.get_width() / 2, y - glow_surface.get_height() / 2))

def decode_animation():
    clock = pygame.time.Clock()
    running = True
    frame_count = 0
    particles = []

    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Create random symbol
        if frame_count % 20 == 0:
            symbol = random.choice(alien_symbols)
            x = random.randint(100, width - 100)
            y = random.randint(100, height - 100)
            render_glowing_symbol(symbol, x, y, frame_count)

            # Add particles around the symbol
            for _ in range(2):
                particles.append(Particle(x, y))

        # Update and draw particles
        for particle in particles[:]:
            particle.move()
            particle.draw(screen)
            if particle.alpha <= 0:
                particles.remove(particle)

        frame_count += 1

        pygame.display.update()
        clock.tick(60)

# Run the animation
decode_animation()

# Quit Pygame
pygame.quit()
