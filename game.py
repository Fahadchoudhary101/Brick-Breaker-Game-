import pygame

# Initialize Pygame
pygame.init()

# Window dimensions
width = 800
height = 600

# Background color
bg_color = (0, 0, 0)

# Create the game window
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Brick Breaker")

# Paddle dimensions
paddle_width = 100
paddle_height = 10
paddle_color = (255, 255, 255)

# Paddle position
paddle_x = (width - paddle_width) // 2
paddle_y = height - 50

# Ball dimensions
ball_radius = 10
ball_color = (255, 255, 255)

# Ball position and speed
ball_x = width // 2
ball_y = height // 2
ball_x_speed = 2
ball_y_speed = -2

# Brick dimensions
brick_width = 80
brick_height = 20
brick_color = (255, 0, 0)

# Create bricks
bricks = []
for row in range(5):
    for col in range(10):
        brick_x = col * (brick_width + 10)
        brick_y = row * (brick_height + 10)
        bricks.append(pygame.Rect(brick_x, brick_y, brick_width, brick_height))

# Game loop flag
running = True

# Game loop
while running:
    window.fill(bg_color)  # Clear the window with the background color

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Exit the game loop

    # Smooth paddle movement with key press check
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle_x -= 5
    if keys[pygame.K_RIGHT]:
        paddle_x += 5

    # Prevent paddle from going out of bounds
    if paddle_x < 0:
        paddle_x = 0
    elif paddle_x > width - paddle_width:
        paddle_x = width - paddle_width

    # Move the ball
    ball_x += ball_x_speed
    ball_y += ball_y_speed

    # Collisions with walls
    if ball_x >= width - ball_radius or ball_x <= ball_radius:
        ball_x_speed *= -1
    if ball_y <= ball_radius:
        ball_y_speed *= -1

    # Collision with paddle
    if ball_y >= paddle_y - ball_radius and paddle_x - ball_radius <= ball_x <= paddle_x + paddle_width + ball_radius:
        ball_y_speed *= -1

    # Collision with bricks
    for brick in bricks[:]:
        if brick.collidepoint(ball_x, ball_y):
            bricks.remove(brick)
            ball_y_speed *= -1
            break

    # Draw bricks on the game window
    for brick in bricks:
        pygame.draw.rect(window, brick_color, brick)

    # Draw the paddle
    pygame.draw.rect(window, paddle_color, (paddle_x, paddle_y, paddle_width, paddle_height))

    # Draw the ball
    pygame.draw.circle(window, ball_color, (ball_x, ball_y), ball_radius)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.delay(5)

# Quit Pygame
pygame.quit()
