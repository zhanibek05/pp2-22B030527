import pygame, math

pygame.init()
WIDTH, HEIGHT = 800, 770
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)

tool_screen = pygame.Surface((800, 30))


class GameObject:
    def draw(self):
        raise NotImplementedError

    def handle(self, mouse_pos):
        raise NotImplementedError


class Button:
    def __init__(self,x, y, path):
        self.x = x
        self.y = y
        #self.rect = pygame.Rect((self.x, self.y, 20, 20))
        self.image = pygame.transform.scale((pygame.image.load(path)), (20, 20))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        
        

    def draw(self):
        #pygame.draw.rect(surface=SCREEN, color= (0, 0, 0), rect=self.rect)
        tool_screen.blit(self.image, self.rect)


class Pen(GameObject):
    def __init__(self, *args, **kwargs):
        self.points = []  # [(x1, y1), (x2, y2)]

    def draw(self):
        for idx, value in enumerate(self.points[:-1]):
            pygame.draw.line(
                SCREEN,
                BLACK,
                start_pos=value,  # self.points[idx]
                end_pos=self.points[idx + 1],
                width=2
            )

    def handle(self, mouse_pos):
        self.points.append(mouse_pos)
   

class Rectangle(GameObject):
    def __init__(self, start_pos):
        self.start_pos = start_pos  # (x1, y1)
        self.end_pos = start_pos  # (x2, y2)

    def draw(self):
        start_pos_x = min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos[1], self.end_pos[1])

        end_pos_x = max(self.start_pos[0], self.end_pos[0])
        end_pos_y = max(self.start_pos[1], self.end_pos[1])

        pygame.draw.rect(
            SCREEN,
            BLACK,
            (
                start_pos_x,
                start_pos_y,
                end_pos_x - start_pos_x,
                end_pos_y - start_pos_y,
            ),
            width=2,
        )

    def handle(self, mouse_pos):
        self.end_pos = mouse_pos

class Circle(GameObject):
    def __init__(self, start_pos):
        self.center = start_pos #x, y
        self.radius = 0 # r
    def draw(self):
        pygame.draw.circle(surface=SCREEN,
                           color=(0, 0, 0),
                           center=self.center,
                           radius=self.radius,
                           width=2)
    def handle(self, mouse_pos):
        a = self.center[0] - mouse_pos[0]
        b = self.center[1] - mouse_pos[1]
        self.radius = math.sqrt(a*a + b*b)

class Eraser(GameObject):
    def __init__(self, *args, **kwargs):
        self.points = []  # [(x1, y1), (x2, y2)]

    def draw(self):
        for value in self.points:
            pygame.draw.circle(SCREEN,
                               WHITE,
                               value,
                               radius=50)

    def handle(self, mouse_pos):
        self.points.append(mouse_pos)
def main():
    running = True
    clock = pygame.time.Clock()
    active_obj = None
    pen_button = Button(10, 10, "images/pen.png")
    rect_button = Button(50, 10, "images/rect.png")
    circle_button = Button(90, 10, "images/circle.png")
    eraser_button = Button(130, 10, "images/eraser.png")

    objects = [
        pen_button,
        rect_button,
        circle_button,
        eraser_button
    ]
    # current_shape = 'pen'
    current_shape = Pen
   
    while running:
        SCREEN.fill((WHITE))
        tool_screen.fill((100, 100, 100))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect_button.rect.collidepoint(event.pos):
                    current_shape = Rectangle
                if pen_button.rect.collidepoint(event.pos):
                    current_shape = Pen
                if circle_button.rect.collidepoint(event.pos):
                    current_shape = Circle
                if eraser_button.rect.collidepoint(event.pos):
                    current_shape = Eraser
                else:
                    active_obj = current_shape(start_pos=event.pos)

            if event.type == pygame.MOUSEMOTION and active_obj is not None:
                active_obj.handle(pygame.mouse.get_pos())
                active_obj.draw()

            if event.type == pygame.MOUSEBUTTONUP and active_obj is not None:
                objects.append(active_obj)
                active_obj = None

        for obj in objects:
            obj.draw()
            
       
        SCREEN.blit(tool_screen, (0, 0))
        

        clock.tick(60)
        pygame.display.update()


if __name__ == '__main__':
    main()