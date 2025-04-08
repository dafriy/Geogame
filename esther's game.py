import pygame
import random
import time

# Initialize pygame
pygame.init()

# Fixed screen dimensions
screen_width = 800
screen_height = 600

# Set up the display with fixed resolution
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("GeoQuest: Explore the World!")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
blue = (70, 130, 180)
green = (0, 255, 0)
red = (255, 0, 0)

# Fonts
font_large = pygame.font.Font(None, 72)
font_medium = pygame.font.Font(None, 36)

# Load and Scale the Background Image
background_image = pygame.image.load("background.png")  # Replace with your image file
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

# Load and Scale the Globe Image for Static Display
globe_image = pygame.image.load("globe.png")  # Replace with your image file
globe_image = pygame.transform.scale(globe_image, (100, 100))

# Background Music
pygame.mixer.music.load("background_music.mp3")  # Replace with your music file
pygame.mixer.music.play(-1)  # Loop the music

# Questions Pool
questions_pool = [
    {"question": "Which animal is known as the King of the Jungle?", "options": ["Elephant", "Lion", "Giraffe", "Cheetah"], "answer": "Lion"},
    {"question": "What is the capital of Ghana?", "options": ["Accra", "Kumasi", "Tamale", "Cape Coast"], "answer": "Accra"},
    {"question": "What is the highest mountain in the world?", "options": ["K2", "Kilimanjaro", "Everest", "Denali"], "answer": "Everest"},
    {"question": "Which ocean is the largest on Earth?", "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"], "answer": "Pacific Ocean"},
    {"question": "Which continent is home to the Sahara Desert?", "options": ["Asia", "Africa", "Australia", "South America"], "answer": "Africa"},
    {"question": "Which planet is known as the Red Planet?", "options": ["Venus", "Mars", "Jupiter", "Saturn"], "answer": "Mars"},
    {"question": "What is the longest river in Africa?", "options": ["Niger River", "Nile River", "Zambezi River", "Congo River"], "answer": "Nile River"},
    {"question": "Which country is famous for pizza?", "options": ["France", "Italy", "Mexico", "Spain"], "answer": "Italy"},
    {"question": "What is the smallest country in the world?", "options": ["Malta", "Monaco", "Vatican City", "San Marino"], "answer": "Vatican City"},
    {"question": "Which desert is the largest in the world?", "options": ["Gobi Desert", "Kalahari Desert", "Sahara Desert", "Antarctic Desert"], "answer": "Antarctic Desert"},
    {"question": "Which animal is the fastest land animal?", "options": ["Cheetah", "Horse", "Leopard", "Gazelle"], "answer": "Cheetah"},
    {"question": "Which is the coldest ocean?", "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"], "answer": "Arctic Ocean"},
    {"question": "Which country has the Great Wall?", "options": ["India", "China", "Japan", "South Korea"], "answer": "China"},
    {"question": "What is the largest rainforest in the world?", "options": ["Congo Rainforest", "Amazon Rainforest", "Sundarbans", "Daintree Rainforest"], "answer": "Amazon Rainforest"}
]

# Display Text on the Screen
def display_text(text, x, y, color, font):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Countdown Timer
def display_timer(seconds_left):
    text = f"Time Left: {seconds_left}s"
    display_text(text, 50, screen_height - 50, red, font_medium)  # Timer at the bottom of the screen

# Introduction Screen
def intro_screen():
    running = True
    while running:
        screen.blit(background_image, (0, 0))  # Display the background image

        # Display centered text
        title_surface = font_large.render("Welcome to GeoQuest!", True, black)
        title_rect = title_surface.get_rect(center=(screen_width // 2, screen_height // 2 - 100))  # Offset upward
        screen.blit(title_surface, title_rect)

        instruction_surface = font_medium.render("Test your geography knowledge.", True, blue)
        instruction_rect = instruction_surface.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(instruction_surface, instruction_rect)

        start_surface = font_medium.render("Press S to Start", True, green)
        start_rect = start_surface.get_rect(center=(screen_width // 2, screen_height // 2 + 100))  # Offset downward
        screen.blit(start_surface, start_rect)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:  # Start the game
                    return True

# End Screen
def end_screen(score, total_questions):
    running = True
    while running:
        screen.blit(background_image, (0, 0))  # Display the background image

        # Display centered text
        game_over_surface = font_large.render("Game Over!", True, black)
        game_over_rect = game_over_surface.get_rect(center=(screen_width // 2, screen_height // 2 - 100))  # Offset upward
        screen.blit(game_over_surface, game_over_rect)

        score_surface = font_medium.render(f"Your Score: {score}/{total_questions}", True, blue)
        score_rect = score_surface.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(score_surface, score_rect)

        replay_surface = font_medium.render("Press R to Replay or Q to Quit", True, green)
        replay_rect = replay_surface.get_rect(center=(screen_width // 2, screen_height // 2 + 100))  # Offset downward
        screen.blit(replay_surface, replay_rect)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    return False
                if event.key == pygame.K_r:
                    return True

# Main Game Loop
def game_loop():
    selected_questions = random.sample(questions_pool, 8)  # Pick random questions
    score = 0

    for question_data in selected_questions:
        question = question_data["question"]
        options = question_data["options"]
        answer = question_data["answer"]

        running = True
        timer_seconds = 30  # Timer starts at 30 seconds
        start_time = time.time()

        while running:
            screen.blit(background_image, (0, 0))  # Draw the background

            # Display Question
            display_text(question, 50, 50, black, font_medium)

            # Display Options
            for i, option in enumerate(options):
                y_position = 150 + i * 40
                display_text(f"{i + 1}. {option}", 50, y_position, blue, font_medium)

            # Timer Logic
            elapsed_time = int(time.time() - start_time)
            remaining_time = max(0, timer_seconds - elapsed_time)
            display_timer(remaining_time)

            if remaining_time <= 0:  # Time's up
                print("⏳ Time's up!")
                running = False

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

                # Keyboard Input
                if event.type == pygame.KEYDOWN:
                    if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4]:
                        index = event.key - pygame.K_1
                        if options[index] == answer:
                            print("🎉 Correct!")
                            score += 1
                        else:
                            print("❌ Wrong!")
                        running = False

                    elif event.unicode.lower() == answer.lower():  # Full answer typing
                        print("🎉 Correct!")
                        score += 1
                        running = False

    if not end_screen(score, len(selected_questions)):
        return

# Run the Game
if intro_screen():
    game_loop()