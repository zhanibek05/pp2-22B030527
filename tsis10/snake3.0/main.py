import pygame, sys
import random
import psycopg2
from pygame.math import Vector2

pygame.init()

FPS = 60
BLOCK_SIZE = 25
BLOCK_NUMBER = 25
SPEED = 200
SCORE = 0
LEVEL = 0
NAME = None

clock = pygame.time.Clock()
screen = pygame.display.set_mode((BLOCK_SIZE*BLOCK_NUMBER, BLOCK_NUMBER*BLOCK_SIZE))
score_screen = pygame.Surface((BLOCK_SIZE*BLOCK_NUMBER, 2*BLOCK_SIZE))

#connect to database
conn = psycopg2.connect(
        database = "Snake",
        host = "localhost",
        password = "password",
        user = "postgres"
    )
cur = conn.cursor()
conn.autocommit = True
cur.execute('''
        CREATE TABLE IF NOT EXISTS userscore(
            name TEXT NOT NULL,
            score INT,
            level INT,
            speed INT
        );
    ''')
cur.execute('''
            CREATE TABLE IF NOT EXISTS records(
                name TEXT NOT NULL,
                score int, 
                level int
            )
            
            ''')

cur.execute('''
            CREATE TABLE IF NOT EXISTS position(
                x REAL,
                y REAL
                 
            )
            
            ''')
  

#text
font = pygame.font.SysFont("Verdana", 18)

class Snake:
    def __init__(self):
        self.body = [Vector2(10, 10), Vector2(9, 10), Vector2(8, 10)]
        self.direction = Vector2(1, 0) #вектор направление
        
    def draw_snake(self):
        for block in self.body:
            head_color = (0, 50, 0)
            color = (45, 125, 53)
            if block == self.body[0]:
                color = head_color
            else:
                color = (45, 125, 53)
            body_rect = pygame.Rect(block[0] * BLOCK_SIZE, 
                                    block[1] * BLOCK_SIZE, 
                                    BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, 
                             color, 
                             body_rect)
            
    
    def move_snake(self):
        body_copy = self.body[:-1] #удаляем последний блок и копируем , в конец добавляем новый вектор + направление
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy
    
    def add_block(self):
        self.body.insert(0, self.body[0] + self.direction)
        
class Fruit:
    def __init__(self):
        self.randomize_pos()
    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x * BLOCK_SIZE, #что бы были ровно по сетке
                                 self.pos.y * BLOCK_SIZE, 
                                 BLOCK_SIZE, 
                                 BLOCK_SIZE)
        pygame.draw.rect(surface = screen
                         ,color = (250, 2, 31), 
                         rect = fruit_rect)
    def randomize_pos(self):
        self.x = random.randint(0, BLOCK_NUMBER - 1)
        self.y = random.randint(2, BLOCK_NUMBER - 1)
        self.pos = Vector2(self.x, self.y)
         
class Main:
    def __init__(self):
        
        self.snake = Snake()
        self.fruit = Fruit()
        self.score = 0
        self.level = 1
        self.speed = 200
    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()
        self.check_level()
    def draw_elements(self):
        
        if self.fruit.pos not in self.snake.body:
            self.fruit.draw_fruit()
        else:
            self.fruit.randomize_pos()
            
        self.snake.draw_snake()
    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]: # if collision
            self.fruit.randomize_pos()
            self.snake.add_block()
            self.score += 1
        
            
    def check_fail(self):
        head_pos = self.snake.body[0]
        if not 0 <= head_pos.x < BLOCK_NUMBER or not 2 <= head_pos.y < BLOCK_NUMBER: # hitting the wall
            self.game_over()
        for body in self.snake.body[1:]:
            if head_pos == body:
                self.game_over()
    def check_level(self):
        if self.score/5 == self.level:
            self.level += 1
            main_game.speed -= 10
            pygame.time.set_timer(SCREEN_UPDATE, main_game.speed)
            
    def game_over(self):
        font = pygame.font.SysFont("Verdana", 90)
        
        global SCORE, LEVEL
        SCORE = self.score
        LEVEL = self.level
        game_over = font.render(f"Game Over!",True, (0, 0, 0))
        screen.blit(game_over, (60, 200))
        pygame.display.update()
        pygame.time.delay(5000)
       
        cur.execute(f'''
                    DELETE FROM userscore
                    WHERE name = '{NAME}'
                    
                    ''')
        cur.execute(f"""SELECT EXISTS(SELECT * FROM records WHERE name = '{NAME}')""")
        if cur.fetchone()[0]:
            cur.execute(f"""
                        UPDATE records
                        SET score = {SCORE},
                            level = {LEVEL}
                        WHERE name = '{NAME}'
                        """)
        else:
            cur.execute(f"""INSERT INTO records
                    VALUES
                    ('{NAME}', {SCORE}, {LEVEL})
                    """)
            
        cur.execute("""DELETE FROM position""")
        cur.close()
        conn.close()
        pygame.quit()
        sys.exit()
        
    def pause_and_save(self):
        font = pygame.font.SysFont("Verdana", 25)
        text = font.render("PAUSE...Your results are saving...", True, (0, 0, 0))
        screen.blit(text,(47, 100))
        pygame.display.update()
        pygame.time.delay(5000)
        global SCORE, LEVEL
        SCORE = self.score
        LEVEL = self.level
        cur.execute(f"""SELECT EXISTS(SELECT * FROM userscore WHERE name = '{NAME}')""")
        if cur.fetchone()[0]:
            cur.execute(f"""
                        UPDATE userscore
                        SET score = {SCORE},
                            level = {LEVEL},
                            speed = {self.speed}
                        WHERE name = '{NAME}'
                        """)
        else:
            cur.execute(f"""INSERT INTO userscore
                    VALUES
                    ('{NAME}', {SCORE}, {LEVEL}, {self.speed})
                    """)
        for idx, body_block in enumerate(main_game.snake.body):
            cur.execute(f"""INSERT INTO position
                        VALUES
                        ({body_block[0]},{body_block[0]})
                        """)
            
        cur.close()
        conn.close()
        pygame.quit()
        sys.exit()
            
            
        
main_game = Main()

SCREEN_UPDATE = pygame.USEREVENT  + 1
pygame.time.set_timer(SCREEN_UPDATE, SPEED) # кастомное событье которая происходит раз в 150 мс



            

def get_player_name():
    font = pygame.font.Font(None, 36)
    input_box = pygame.Rect(200, 200, 200, 36)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    player_name = ''
    active = False
    done = False
    
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        done = True
                    elif event.key == pygame.K_BACKSPACE:
                        player_name = player_name[:-1]
                    else:
                        player_name += event.unicode
        
        screen.fill((255, 203, 100))
        # Отрисовка поля для ввода имени игрока
        txt_surface = font.render(player_name, True, (0, 0, 0))
        width = max(200, txt_surface.get_width())
        input_box.w = width
        pygame.draw.rect(screen, color, input_box, 2)
        text1 = font.render("Snake Game!", True, (200, 0, 0))
        text2 = font.render("Enter your name:", True, (0, 0,0))
        cur.execute('''
                     select * from records where score = (select MAX(score) from records)
                              ''')
        rec_name = cur.fetchone()[0]
        cur.execute('''
                     select * from records where score = (select MAX(score) from records)
                             ''')
        rec_score = cur.fetchone()[1]
        
        record = font.render(f"Current record:{rec_name} - {rec_score} scores", True, (50, 50, 50))
        screen.blit(text1, (210, 100))
        screen.blit(text2, (200, 150))
        screen.blit(record,(150, 300))
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, (0, 0, 0), input_box, 2)
        pygame.display.flip()
    
    return player_name


def main():
    name = get_player_name()
    global NAME
    NAME = name
    
    cur.execute(f"""SELECT EXISTS (SELECT * FROM userscore WHERE name = '{name}') """)
    if cur.fetchone()[0]:
        cur.execute(f"""SELECT * FROM userscore WHERE name = '{name}'""")
        main_game.score = cur.fetchone()[1]
        cur.execute(f"""SELECT * FROM userscore WHERE name = '{name}'""")
        main_game.level = cur.fetchone()[2]
        cur.execute(f"""SELECT * FROM userscore WHERE name = '{name}'""")
        main_game.speed = cur.fetchone()[3]
        cur.execute('''SELECT * FROM position''')
        snake_positions = cur.fetchall()
        for snake_block in snake_positions:
            main_game.snake.body.append(snake_block)
    
  
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                sys.exit()
                
            if event.type == SCREEN_UPDATE: #каждые 150 мс двигаем змею
                main_game.update()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if main_game.snake.direction != (0, 1):
                        main_game.snake.direction = (0, -1) 
                if event.key == pygame.K_DOWN:
                    if main_game.snake.direction != (0, -1): 
                        main_game.snake.direction = (0, 1)
                if event.key == pygame.K_RIGHT:
                    if main_game.snake.direction != (-1, 0):
                        main_game.snake.direction = (1, 0)
                if event.key == pygame.K_LEFT:
                    if main_game.snake.direction != (1, 0):
                        main_game.snake.direction = (-1, 0)
                if event.key == pygame.K_SPACE:
                    main_game.pause_and_save()
            
        screen.fill((255, 203, 100))
        score_screen.fill((96, 100, 96))
        user = font.render(f"user: {name}",True, (0, 0, 0))
        scores = font.render("Score:"+ str(main_game.score),True, (0, 0, 0))
        levels = font.render("Level:" + str(main_game.level), True, (0, 0, 0))
        score_screen.blit(scores,(10, 0))
        score_screen.blit(levels,(10, 20))
        score_screen.blit(user,(400, 0))
        
        screen.blit(score_screen, (0, 0))
        main_game.draw_elements()
        pygame.display.update()
        clock.tick(FPS)
        
if __name__ == '__main__':
    main()