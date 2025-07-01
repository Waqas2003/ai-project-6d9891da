import pygame
import sys
import random
import time

class SnakeGame:
    def __init__(self):
        self.size = width, height = 640, 480
        self.black = 0, 0, 0
        self.white = 255, 255, 255
        self.red = 255, 0, 0
        self.green = 0, 255, 0
        self.snake_speed = 10
        self.snake_pos = [100, 50]
        self.snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]
        self.food_pos = [random.randrange(1, (width // 10)) * 10, random.randrange(1, (height // 10)) * 10]
        self.food_spawn = True
        self.direction = 'RIGHT'
        self.change_to = self.direction
        self.score = 0

    def run(self):
        pygame.init()
        self.game_display = pygame.display.set_mode(self.size)
        pygame.display.set_caption('Snake Game')
        fps = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or event.key == ord('w'):
                        self.change_to = 'UP'
                    if event.key == pygame.K_DOWN or event.key == ord('s'):
                        self.change_to = 'DOWN'
                    if event.key == pygame.K_LEFT or event.key == ord('a'):
                        self.change_to = 'LEFT'
                    if event.key == pygame.K_RIGHT or event.key == ord('d'):
                        self.change_to = 'RIGHT'
            self.validation()
            self.snake_pos = [self.snake_pos[0] + 10, self.snake_pos[1]]
            self.snake_body.insert(0, list(self.snake_pos))
            if self.snake_pos[0] >= self.size[0] or self.snake_pos[0] < 0:
                self.game_over()
            if self.snake_pos[1] >= self.size[1] or self.snake_pos[1] < 0:
                self.game_over()
            self.game_display.fill(self.black)
            for pos in self.snake_body:
                pygame.draw.rect(self.game_display, self.green, pygame.Rect(pos[0], pos[1], 10, 10))
            pygame.draw.rect(self.game_display, self.red, pygame.Rect(self.food_pos[0], self.food_pos[1], 10, 10))
            if self.snake_pos == self.food_pos:
                self.score += 1
                self.food_spawn = False
            else:
                self.snake_body.pop()
            if not self.food_spawn:
                self.food_pos = [random.randrange(1, (self.size[0] // 10)) * 10, random.randrange(1, (self.size[1] // 10)) * 10]
            self.food_spawn = True
            pygame.display.flip()
            fps.tick(self.snake_speed)

    def validation(self):
        if self.change_to == 'UP' and self.direction != 'DOWN':
            self.direction = 'UP'
        if self.change_to == 'DOWN' and self.direction != 'UP':
            self.direction = 'DOWN'
        if self.change_to == 'LEFT' and self.direction != 'RIGHT':
            self.direction = 'LEFT'
        if self.change_to == 'RIGHT' and self.direction != 'LEFT':
            self.direction = 'RIGHT'

    def game_over(self):
        self.game_display.fill(self.black)
        font = pygame.font.Font(None, 36)
        text = font.render("Game Over! Your score is " + str(self.score), True, self.white)
        self.game_display.blit(text, [self.size[0] // 2 - 150, self.size[1] // 2])
        pygame.display.flip()
        time.sleep(2)
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = SnakeGame()
    game.run()