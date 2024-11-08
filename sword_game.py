
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spinning Sword Simulation")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Agent settings
FPS = 60
clock = pygame.time.Clock()

# Limb lengths
UPPER_ARM_LENGTH = 50
FOREARM_LENGTH = 50
SWORD_LENGTH = 100

# Shoulder positions
shoulder1 = (WIDTH // 4, HEIGHT // 2)
shoulder2 = (3 * WIDTH // 4, HEIGHT // 2)

# Initial angles
angle1 = 0
angle2 = 0

# Angle increment (for continuous rotation)
angle_speed = 0.05  # Radians per frame

# Pattern options
patterns = ["Circular", "Anti-Spin", "Three-Petal Lotus"]
current_pattern = 0  # Start with circular motion

# Function to calculate limb positions based on pattern
def calculate_limb_positions(shoulder, base_angle, pattern="Circular"):
    if pattern == "Circular":
        # Circular motion: all limbs rotate in the same direction
        should_angle = base_angle
        elbow_angle = base_angle
        hand_angle = base_angle
    elif pattern == "Anti-Spin":
        # Anti-spin: rotate the elbow in one direction, hand in the opposite
        should_angle = base_angle
        elbow_angle = base_angle
        hand_angle = -base_angle  # Opposite direction for anti-spin
    elif pattern == "Three-Petal Lotus":
        # Three-petal lotus: elbow rotates once, hand rotates three times in the opposite direction
        should_angle = base_angle
        elbow_angle = base_angle
        hand_angle = -2 * base_angle  # Three times opposite rotation for hand
    else:
        should_angle = base_angle
        elbow_angle = base_angle
        hand_angle = base_angle

    
    # Calculate positions
    elbow_x = shoulder[0] + UPPER_ARM_LENGTH * math.cos(should_angle)
    elbow_y = shoulder[1] + UPPER_ARM_LENGTH * math.sin(should_angle)
    hand_x = elbow_x + FOREARM_LENGTH * math.cos(elbow_angle)
    hand_y = elbow_y + FOREARM_LENGTH * math.sin(elbow_angle)
    sword_tip_x = hand_x + SWORD_LENGTH * math.cos(hand_angle)
    sword_tip_y = hand_y + SWORD_LENGTH * math.sin(hand_angle)
    return (elbow_x, elbow_y), (hand_x, hand_y), (sword_tip_x, sword_tip_y)

# Main loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_t:  # Press 't' to toggle pattern
                current_pattern = (current_pattern + 1) % len(patterns)

    # Update angles for continuous rotation
    angle1 += angle_speed
    angle2 += angle_speed  # Rotate in opposite direction for variety
    
    # Calculate limb positions based on the selected pattern
    elbow1, hand1, sword_tip1 = calculate_limb_positions(shoulder1, angle1, pattern=patterns[current_pattern])
    elbow2, hand2, sword_tip2 = calculate_limb_positions(shoulder2, angle2, pattern=patterns[current_pattern])

    # Clear screen
    screen.fill(WHITE)

    # Display current pattern
    font = pygame.font.SysFont(None, 36)
    pattern_text = font.render(f"Pattern: {patterns[current_pattern]}", True, (0, 0, 0))
    screen.blit(pattern_text, (10, 10))

    # Draw agent 1
    pygame.draw.line(screen, BLUE, shoulder1, elbow1, 3)
    pygame.draw.line(screen, GREEN, elbow1, hand1, 3)
    pygame.draw.line(screen, RED, hand1, sword_tip1, 3)
    pygame.draw.circle(screen, BLUE, (int(elbow1[0]), int(elbow1[1])), 5)
    pygame.draw.circle(screen, GREEN, (int(hand1[0]), int(hand1[1])), 5)
    pygame.draw.circle(screen, RED, (int(sword_tip1[0]), int(sword_tip1[1])), 5)

    # Draw agent 2
    pygame.draw.line(screen, BLUE, shoulder2, elbow2, 3)
    pygame.draw.line(screen, GREEN, elbow2, hand2, 3)
    pygame.draw.line(screen, RED, hand2, sword_tip2, 3)
    pygame.draw.circle(screen, BLUE, (int(elbow2[0]), int(elbow2[1])), 5)
    pygame.draw.circle(screen, GREEN, (int(hand2[0]), int(hand2[1])), 5)
    pygame.draw.circle(screen, RED, (int(sword_tip2[0]), int(sword_tip2[1])), 5)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()

