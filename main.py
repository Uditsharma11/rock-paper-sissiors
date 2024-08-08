import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rock, Paper, Scissors")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Load and scale images for choices
choices = ['rock', 'paper', 'scissors']
images = {choice: pygame.transform.scale(pygame.image.load(f"images/{choice}.png"), (150, 150)) for choice in choices}

# Coordinates for images (centered horizontally with equal spacing)
positions = {
    'rock': (width // 5, height // 2 - 75),
    'paper': (2 * width // 5, height // 2 - 75),
    'scissors': (3 * width // 5, height // 2 - 75)
}

# Game variables
player_choice = None
computer_choice = None
result = None
player_score = 0
computer_score = 0
draw_score = 0
font = pygame.font.Font(None, 36)
play_again = False

def get_computer_choice():
    return random.choice(choices)

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "You lose!"

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_again:
                play_again = False
                player_choice = None
                computer_choice = None
                result = None
            else:
                mouse_x, mouse_y = event.pos
                for choice, pos in positions.items():
                    if pos[0] < mouse_x < pos[0] + 150 and pos[1] < mouse_y < pos[1] + 150:
                        player_choice = choice
                        computer_choice = get_computer_choice()
                        result = determine_winner(player_choice, computer_choice)
                        
                        if result == "You win!":
                            player_score += 1
                        elif result == "You lose!":
                            computer_score += 1
                        else:
                            draw_score += 1
                        play_again = True
                        break

    # Fill the background with white
    screen.fill(WHITE)
    
    # Display title
    title_text = font.render("Choose:", True, BLACK)
    screen.blit(title_text, (width // 2 - title_text.get_width() // 2, 20))
    
    # Draw images for choices in the center
    for choice, pos in positions.items():
        screen.blit(images[choice], pos)

    # Display the result and scores
    if result:
        result_text = font.render(f"Result: {result}", True, BLACK)
        screen.blit(result_text, (width // 2 - result_text.get_width() // 2, 300))
        
        comp_choice_text = font.render(f"Computer chose: {computer_choice.capitalize()}", True, BLACK)
        screen.blit(comp_choice_text, (width // 2 - comp_choice_text.get_width() // 2, 330))
        
        score_text = font.render(f"Won = {player_score} | Lost = {computer_score} | Draw = {draw_score}", True, BLACK)
        screen.blit(score_text, (width // 2 - score_text.get_width() // 2, 360))
        
        play_again_text = font.render("Click to play again!", True, GREEN)
        screen.blit(play_again_text, (width // 2 - play_again_text.get_width() // 2, 390))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
