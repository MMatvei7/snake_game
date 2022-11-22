import Globals
import pygame
import pygame_menu
import random
import time

globals = Globals.Globals()
# Window size
globals.window_x = 720
globals.window_y = 480

# defining colors
globals.black = pygame.Color(0, 0, 0)
globals.white = pygame.Color(255, 255, 255)
globals.red = pygame.Color(255, 0, 0)
globals.green = pygame.Color(0, 255, 0)
globals.blue = pygame.Color(0, 0, 255)
globals.yellow = pygame.Color(255, 255, 0)

# Initialising pygame
pygame.init()

# Initialise game window
pygame.display.set_caption('Snake game')
game_window = pygame.display.set_mode((globals.window_x, globals.window_y))

# FPS (frames per second) controller
fps = pygame.time.Clock()
globals.tmp = 15

globals.rating_score = [0] * 3


# set game speed
def set_difficulty(value, difficulty=15):
    globals.tmp = difficulty


globals.color_ = globals.green


# set snake color
def set_color(value, color=globals.green):
    globals.color_ = color


globals.window_color = globals.black


# set window color
def set_window(value, color=globals.black):
    globals.window_color = color


def draw_text(k, y):
    my_font = pygame.font.SysFont('Times', 20)
    game_over_surface = my_font.render(str(-k) + ': ' + str(sorted(globals.rating_score)[k]),
                                       True,
                                       globals.red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (globals.window_x / 2, y)
    game_window.blit(game_over_surface, game_over_rect)


def show_rating():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu_r()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menu_r()
        game_window.fill(globals.window_color)
        draw_text(-1, 100)
        draw_text(-2, 200)
        draw_text(-3, 300)
        pygame.display.update()


def start_the_game():
    snake_speed = globals.tmp

    game_window.fill(globals.window_color)

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
            'Your Score is : ' + str(score), True, globals.red)
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (globals.window_x / 2, globals.window_y / 4)
        game_window.blit(game_over_surface, game_over_rect)
        pygame.display.flip()
        time.sleep(1)
        globals.rating_score.append(score)
        menu_r()

    # create first fruit type: pineapple - globals.blue fruit
    class Pineapple:
        fruit_spawn = True
        count_pineapple = 0

        # initialization
        def __init__(self):
            self.fruit_position = [random.randrange(1, ((globals.window_x - 100) // 10)) * 10,
                                   random.randrange(1, ((globals.window_y - 100) // 10)) * 10]

            self.fruit_spawn = True
            self.fruit_color = globals.blue
            self.count_pineapple = 1

        # create random pineapple position
        def fruit_appear(self):
            self.fruit_position = [random.randrange(1, ((globals.window_x - 100) // 10)) * 10,
                                   random.randrange(1, ((globals.window_y - 100) // 10)) * 10]

            self.fruit_color = globals.blue

        # draw pineapple
        def fruit_window_appear(self):
            pygame.draw.rect(game_window, pineapple.fruit_color,
                             pygame.Rect(pineapple.fruit_position[0], pineapple.fruit_position[1], 10, 10))

    class Apple:
        fruit_spawn = True

        def __init__(self):
            self.fruit_position = [random.randrange(1, ((globals.window_x - 100) // 10)) * 10,
                                   random.randrange(1, ((globals.window_y - 100) // 10)) * 10]

            self.fruit_spawn = True
            self.fruit_color = globals.white

        def fruit_appear(self):
            self.fruit_position = [random.randrange(1, ((globals.window_x - 100) // 10)) * 10,
                                   random.randrange(1, ((globals.window_y - 100) // 10)) * 10]
            self.fruit_color = globals.white

        def fruit_window_appear(self):
            pygame.draw.rect(game_window, apple.fruit_color,
                             pygame.Rect(apple.fruit_position[0], apple.fruit_position[1], 10, 10))

    class Snake:
        snake_body = []
        snake_position = []
        score = 0
        turns = ''
        direction = ''

        def __init__(self):
            self.snake_body = [[100, 50]]
            self.snake_position = [100, 100]
            self.color = globals.color_
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
                                                   'speed'.format(k), True, globals.red)
                game_over_rect = game_over_surface.get_rect()
                game_over_rect.midtop = (globals.window_x / 2, globals.window_y / 4)
                game_window.blit(game_over_surface, game_over_rect)
                pygame.display.flip()
                time.sleep(1)
                self.score += k
            else:
                my_font = pygame.font.SysFont('Times', 20)
                game_over_surface = my_font.render(
                    'You have eaten pineapple and reached new level and gain +{} score and speed'.format(k), True,
                    globals.red)
                game_over_rect = game_over_surface.get_rect()
                game_over_rect.midtop = (globals.window_x / 2, globals.window_y / 4)
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
            if self.snake_position[0] < 0 or self.snake_position[0] > globals.window_x - 10:
                game_over(self.score)
                # quit()
            if self.snake_position[1] < 0 or self.snake_position[1] > globals.window_y - 10:
                game_over(self.score)

        # main snake movement
        def movement(self, fruit, pineapple, snake_speed):
            while True:
                self.change_pos(), self.current_move(), self.snake_body.insert(0, list(self.snake_position))
                self.eat_apple()
                if not apple.fruit_spawn:
                    apple.fruit_appear()
                if not pineapple.fruit_spawn:
                    pineapple.fruit_appear()
                if self.score % 5 == 0 and self.score > 0:
                    if not apple.fruit_spawn:
                        self.new_level(1)
                    else:
                        self.new_level(2)
                    snake_speed, pineapple.count_pineapple = snake_speed + 1, pineapple.count_pineapple + 1
                apple.fruit_spawn, pineapple.fruit_spawn = True, True
                game_window.fill(globals.window_color)
                for pos in self.snake_body:
                    pygame.draw.rect(game_window, globals.color_, pygame.Rect(pos[0], pos[1], 10, 10))
                apple.fruit_window_appear()
                if pineapple.count_pineapple % 2 == 0:
                    pineapple.fruit_window_appear()
                self.boards_death(), self.self_death(), show_score(1, globals.white, 'Times', 20, self.score)
                pygame.display.update(), fps.tick(snake_speed)

    snake = Snake()
    apple = Apple()
    pineapple = Pineapple()
    direction = 'RIGHT'
    change_to = direction
    snake.movement(apple, pineapple, snake_speed)


def menu_r():
    menu = pygame_menu.Menu('Welcome to Snake Game', 720, 480,
                            theme=pygame_menu.themes.THEME_BLUE)
    menu.add.selector('Speed :',
                      [('Absolutely Hard', 20), ('Hard', 15), ('Medium', 10), ('Easy', 5), ('Elementary', 3)],
                      onchange=set_difficulty)
    menu.add.selector('Snake Color :', [('green', globals.green), ('red', globals.red)],
                      onchange=set_color)
    menu.add.selector('Window Color :', [('black', globals.black), ('yellow', globals.yellow)],
                      onchange=set_window)
    menu.add.button('Play', start_the_game)
    menu.add.button('Rating', show_rating)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(game_window)


menu_r()
