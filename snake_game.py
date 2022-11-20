import pygame
import time
import random
import pygame_menu

# Window size
window_x = 720
window_y = 480

# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
yellow = pygame.Color(255, 255, 0)

# Initialising pygame
pygame.init()

# Initialise game window
pygame.display.set_caption('Snake game')
game_window = pygame.display.set_mode((window_x, window_y))

# FPS (frames per second) controller
fps = pygame.time.Clock()
tmp = 15


# set game speed
def set_difficulty(value, difficulty=15):
    global tmp
    tmp = difficulty


color_ = green


# set snake color
def set_color(value, color=green):
    global color_
    color_ = color


window_color = black


# set window color
def set_window(value, color=black):
    global window_color
    window_color = color


def start_the_game():
    global tmp
    snake_speed = tmp

    global window_color
    game_window.fill(window_color)

    # show rating table
    def show_score(choice, color, font, size, score):
        score_font = pygame.font.SysFont(font, size)
        score_surface = score_font.render('Score : ' + str(score), True, color)
        score_rect = score_surface.get_rect()
        game_window.blit(score_surface, score_rect)

    # game over
    def game_over(score):
        my_font = pygame.font.SysFont('Times', 50)
        game_over_surface = my_font.render(
            'Your Score is : ' + str(score), True, red)
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (window_x / 2, window_y / 4)
        game_window.blit(game_over_surface, game_over_rect)
        pygame.display.flip()
        time.sleep(1)
        pygame.quit()
        quit()

    # create first fruit type: pineapple - blue fruit
    class Pineapple:
        fruit_spawn = True
        count_pineapple = 0

        # initialization
        def __init__(self):
            self.fruit_position = [random.randrange(1, ((window_x - 100) // 10)) * 10,
                                   random.randrange(1, ((window_y - 100) // 10)) * 10]

            self.fruit_spawn = True
            self.fruit_color = blue
            self.count_pineapple = 1

        # create random pineapple position
        def fruit_appear(self):
            self.fruit_position = [random.randrange(1, ((window_x - 100) // 10)) * 10,
                                   random.randrange(1, ((window_y - 100) // 10)) * 10]

            self.fruit_color = blue

        # draw pineapple
        def fruit_window_appear(self):
            pygame.draw.rect(game_window, pineapple.fruit_color,
                             pygame.Rect(pineapple.fruit_position[0], pineapple.fruit_position[1], 10, 10))

    class Apple:
        fruit_spawn = True

        def __init__(self):
            self.fruit_position = [random.randrange(1, ((window_x - 100) // 10)) * 10,
                                   random.randrange(1, ((window_y - 100) // 10)) * 10]

            self.fruit_spawn = True
            self.fruit_color = white

        def fruit_appear(self):
            self.fruit_position = [random.randrange(1, ((window_x - 100) // 10)) * 10,
                                   random.randrange(1, ((window_y - 100) // 10)) * 10]
            self.fruit_color = white

        def fruit_window_appear(self):
            pygame.draw.rect(game_window, apple.fruit_color,
                             pygame.Rect(apple.fruit_position[0], apple.fruit_position[1], 10, 10))

    global color_

    class Snake:
        snake_body = []
        snake_position = []
        score = 0
        turns = ''
        direction = ''

        def __init__(self):
            self.snake_body = [[100, 50]]
            self.snake_position = [100, 100]
            self.color = color_
            self.score = 0
            self.turns = 'RIGHT'
            self.direction = 'RIGHT'

        # check keyboard
        def change_pos(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        self.turns = 'UP'
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        self.turns = 'DOWN'
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        self.turns = 'LEFT'
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        self.turns = 'RIGHT'

            # escape from the situation then the "simular" buttons are pushed
            if self.turns == 'UP' and self.direction != 'DOWN':
                self.direction = 'UP'
            if self.turns == 'DOWN' and self.direction != 'UP':
                self.direction = 'DOWN'
            if self.turns == 'LEFT' and self.direction != 'RIGHT':
                self.direction = 'LEFT'
            if self.turns == 'RIGHT' and self.direction != 'LEFT':
                self.direction = 'RIGHT'

        # if user reached high score - increase the level
        def new_level(self, k):
            if k == 1:
                my_font = pygame.font.SysFont('Times', 20)
                game_over_surface = my_font.render('You have eaten apple and reached new level and gain +{} score and '
                                                   'speed'.format(k),
                                                   True,
                                                   red)
                game_over_rect = game_over_surface.get_rect()
                game_over_rect.midtop = (window_x / 2, window_y / 4)
                game_window.blit(game_over_surface, game_over_rect)
                pygame.display.flip()
                time.sleep(1)
                self.score += k
            else:
                my_font = pygame.font.SysFont('Times', 20)
                game_over_surface = my_font.render(
                    'You have eaten pineapple and reached new level and gain +{} score and speed'.format(k),
                    True,
                    red)
                game_over_rect = game_over_surface.get_rect()
                game_over_rect.midtop = (window_x / 2, window_y / 4)
                game_window.blit(game_over_surface, game_over_rect)
                pygame.display.flip()
                time.sleep(1)
                self.score += k

        # provide current snake movement
        def current_move(self):
            if self.direction == 'UP':
                self.snake_position[1] -= 10
            if self.direction == 'DOWN':
                self.snake_position[1] += 10
            if self.direction == 'LEFT':
                self.snake_position[0] -= 10
            if self.direction == 'RIGHT':
                self.snake_position[0] += 10

        # handle the situation when snake meets fruit
        def eat_apple(self):
            if self.snake_position[0] == apple.fruit_position[0] and self.snake_position[1] == apple.fruit_position[1]:
                self.score += 1
                apple.fruit_spawn = False
            elif self.snake_position[0] == pineapple.fruit_position[0] and self.snake_position[1] == \
                    pineapple.fruit_position[1]:
                self.score += 2
                pineapple.fruit_spawn = False
            else:
                self.snake_body.pop()

        # if snake meets its body
        def self_death(self):
            for body in self.snake_body[1:]:
                if self.snake_position[0] == body[0] and self.snake_position[1] == body[1]:
                    game_over(self.score)

        # if snake touches boards
        def boards_death(self):
            if self.snake_position[0] < 0 or self.snake_position[0] > window_x - 10:
                game_over(self.score)
            if self.snake_position[1] < 0 or self.snake_position[1] > window_y - 10:
                game_over(self.score)

        # main snake movement
        def movement(self, fruit, pineapple, snake_speed):
            while True:
                # handling key events
                self.change_pos()
                # Moving the snake
                self.current_move()
                # Snake body growing mechanism
                self.snake_body.insert(0, list(self.snake_position))
                # eating fruit
                self.eat_apple()
                if not apple.fruit_spawn:
                    apple.fruit_appear()

                if not pineapple.fruit_spawn:
                    pineapple.fruit_appear()

                # if user has enough score - get bonuses
                if self.score % 5 == 0 and self.score > 0:
                    if not apple.fruit_spawn:
                        self.new_level(1)
                    else:
                        self.new_level(2)
                    snake_speed += 1
                    pineapple.count_pineapple += 1
                apple.fruit_spawn = True
                pineapple.fruit_spawn = True
                game_window.fill(window_color)
                for pos in self.snake_body:
                    pygame.draw.rect(game_window, color_, pygame.Rect(pos[0], pos[1], 10, 10))
                # new fruit
                apple.fruit_window_appear()
                if pineapple.count_pineapple % 2 == 0:
                    pineapple.fruit_window_appear()
                # game over conditions
                self.boards_death()
                # touching the snake body
                self.self_death()

                # displaying score
                show_score(1, white, 'Times', 20, self.score)

                # Refresh game screen
                pygame.display.update()

                # Frame Per Second /Refresh Rate
                fps.tick(snake_speed)

    snake = Snake()
    apple = Apple()
    pineapple = Pineapple()
    direction = 'RIGHT'
    change_to = direction
    snake.movement(apple, pineapple, snake_speed)


menu = pygame_menu.Menu('Welcome to Snake Game', 720, 480,
                        theme=pygame_menu.themes.THEME_BLUE)
menu.add.selector('Speed :', [('Hard', 15), ('Easy', 10)], onchange=set_difficulty)
menu.add.selector('Snake Color :', [('Green', green), ('Red', red)], onchange=set_color)
menu.add.selector('Window Color :', [('Black', black), ('Yellow', yellow)], onchange=set_window)
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)
menu.mainloop(game_window)
