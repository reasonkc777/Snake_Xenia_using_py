import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Set up colors
OFF_PINK = (0, 0, 128)
NAVY_BLUE = (231, 202, 194)
RED = (255, 0, 0)


# Main class for the game
class SnakeGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Snake Xenia")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.score = 0
        self.high_score = 0
        self.snake = Snake()
        self.food = Food()
        self.main_menu = MainMenu(self.screen, self.clock)

    def run(self):
        self.main_menu.show_menu()
        while True:
            if self.main_menu.check_start():
                self.snake.reset()
                self.score = 0
                self.game_loop()

    def game_loop(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    self.snake.handle_keys(event.key)

            self.snake.move()
            collision = self.check_collision()
            if collision == 1:
                if self.score > self.high_score:
                    self.high_score = self.score
                self.game_over_screen()
                running = False
            self.screen.fill(OFF_PINK)
            self.snake.draw(self.screen)
            self.food.draw(self.screen)
            self.display_score()
            self.display_high_score()
            pygame.display.flip()
            self.clock.tick(10)

        self.run()

    def check_collision(self):
        if self.snake.check_collision(SCREEN_WIDTH, SCREEN_HEIGHT):
            return 1

        if self.snake.check_eating(self.food.position):
            self.food.new_position()
            self.snake.add_segment()
            self.score += 1
        return -1

    def display_score(self):
        text = self.font.render(f"Score: {self.score}", True, NAVY_BLUE)
        self.screen.blit(text, (10, 10))

    def display_high_score(self):
        text = self.font.render(f"High Score: {self.high_score}", True, NAVY_BLUE)
        self.screen.blit(text, (SCREEN_WIDTH - 200, 10))

    def game_over_screen(self):
        self.screen.fill(OFF_PINK)
        text = self.font.render("Game Over", True, NAVY_BLUE)
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.wait(2000)

# Class for the Snake
class Snake:
    def __init__(self):
        self.size = 1
        self.elements = [[100, 50]]
        self.size_of_block = 20
        self.dx = 20
        self.dy = 0

    def reset(self):
        self.size = 1
        self.elements = [[100, 50]]
        self.dx = 20
        self.dy = 0

    def draw(self, screen):
        for element in self.elements:
            pygame.draw.rect(screen, NAVY_BLUE, (element[0], element[1], self.size_of_block, self.size_of_block))

    def move(self):
        for i in range(len(self.elements) - 1, 0, -1):
            self.elements[i] = list(self.elements[i - 1])

        self.elements[0][0] = (self.elements[0][0] + self.dx) % SCREEN_WIDTH
        self.elements[0][1] = (self.elements[0][1] + self.dy) % SCREEN_HEIGHT

    def add_segment(self):
        self.size += 1
        self.elements.append([0, 0])

    def handle_keys(self, key):
        if key == pygame.K_LEFT and self.dx == 0:
            self.dx = -20
            self.dy = 0
        if key == pygame.K_RIGHT and self.dx == 0:
            self.dx = 20
            self.dy = 0
        if key == pygame.K_UP and self.dy == 0:
            self.dy = -20
            self.dx = 0
        if key == pygame.K_DOWN and self.dy == 0:
            self.dy = 20
            self.dx = 0

    def check_collision(self, screen_width, screen_height):
        if (self.elements[0][0] < 0 or
            self.elements[0][0] >= screen_width or
            self.elements[0][1] < 0 or
            self.elements[0][1] >= screen_height):
            return True

        for block in self.elements[1:]:
            if (block[0] == self.elements[0][0] and block[1] == self.elements[0][1]):
                return True
        return False

    def check_eating(self, food_position):
        if (abs(self.elements[0][0] - food_position[0]) < 20 and
                abs(self.elements[0][1] - food_position[1]) < 20):
            return True
        return False

# Class for the Food
class Food:
    def __init__(self):
        self.position = [random.randrange(1, SCREEN_WIDTH // 20) * 20, random.randrange(1, SCREEN_HEIGHT // 20) * 20]
        self.size_of_block = 20

    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.position[0], self.position[1], self.size_of_block, self.size_of_block))

    def new_position(self):
        self.position = [random.randrange(1, SCREEN_WIDTH // 20) * 20, random.randrange(1, SCREEN_HEIGHT // 20) * 20]

# Class for the Main Menu
class MainMenu:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.font = pygame.font.Font(None, 36)

    def show_menu(self):
        menu = True
        while menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        menu = False
                    if event.key == pygame.K_2:
                        pygame.quit()

            self.screen.fill(OFF_PINK)
            title = self.font.render("Snake Xenia", True, NAVY_BLUE)
            self.screen.blit(title, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 4))
            start = self.font.render("Press 1 to Start", True, NAVY_BLUE)
            quit_game = self.font.render("Press 2 to Quit", True, NAVY_BLUE)
            self.screen.blit(start, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2))
            self.screen.blit(quit_game, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 50))
            pygame.display.flip()
            self.clock.tick(10)

    def check_start(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            return True
        return False

# Run the game
if __name__ == "__main__":
    game = SnakeGame()
    game.run()
