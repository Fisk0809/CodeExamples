from turtle import circle, shape
import pymunk as pm, pygame as pg, sys

def create_apple(space,pos):
    body = pm.Body(1,100, pm.Body.DYNAMIC)
    body.position = pos
    shape = pm.Circle(body, 70)
    space.add(body,shape)
    return shape

def draw_apples(apples):
    for apple in apples:
        pos_x = int(apple.body.position.x)
        pos_y = int(apple.body.position.y)
        apple_rect = apple_surface.get_rect(center = (pos_x,pos_y))
        screen.blit(apple_surface,apple_rect)


def static_ball(space, pos):
    body = pm.Body(body_type = pm.Body.STATIC)
    body.position = pos
    shape = pm.Circle(body,50)
    space.add(body,shape)
    return shape

def draw_balls(balls):
    for ball in balls:
        pos_x = int(ball.body.position.x)
        pos_y = int(ball.body.position.y)
        pg.draw.circle(screen,(255,255,255),(pos_x,pos_y),50)


pg.init()
screen = pg.display.set_mode((1280,720))
clock = pg.time.Clock()
space = pm.Space()
space.gravity = (40, -10)
apple_surface = pg.image.load('img.png')
apple_surface = pg.transform.scale(apple_surface, (150, 150))
apples = []

balls = []
balls.append(static_ball(space,(500,500)))
balls.append(static_ball(space,(250,600)))
balls.append(static_ball(space,(450,700)))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            apples.append(create_apple(space,event.pos))
    screen.fill((25,25,25))
    draw_apples(apples)
    draw_balls(balls)
    space.step(1/50)
    pg.display.update()
    clock.tick(165)