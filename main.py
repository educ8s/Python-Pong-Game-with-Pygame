import pygame, sys, random

def game_over(winner):
    global ball_speed_y, ball_speed_x, cpu_points, player_points
    if winner == "cpu":
        cpu_points += 1
    if winner == "player":
        player_points += 1
    ball.x = screen_width/2 - 10
    ball.y = random.randint(10,100)
    ball_speed_x *= random.choice([1,-1])
    ball_speed_y *= random.choice([1,-1])

def animate_ball():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    if ball.bottom >= screen_height or ball.top <= 0:
        ball_speed_y *= -1
    if ball.right >= screen_width: 
        game_over("cpu")
    if ball.left <= 0:
        game_over("player")
    if ball.colliderect(player):
        ball_speed_x *= -1
    if ball.colliderect(opponent):
        ball_speed_x *= -1

def animate_player():
    player.y += player_speed 
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def animate_cpu():
    global cpu_speed
    opponent.y += cpu_speed
    if opponent.bottom >= ball.bottom:
        cpu_speed = - 7
    if opponent.top <= ball.top:
        cpu_speed = 7
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

pygame.init()
clock = pygame.time.Clock()
score_font = pygame.font.Font(None , 100)
screen_width, screen_height = 1280, 960
cpu_points, player_points = 0, 0

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("My Pong Game!")

# Game Assets
ball = pygame.Rect(screen_width/2 - 10, screen_height/2 - 10, 20, 20)
ball_speed_x = 7
ball_speed_y = 7
player_speed = 0
cpu_speed = 0

player = pygame.Rect(screen_width - 30, screen_height/2 - 50, 20, 120)
opponent = pygame.Rect(10, screen_height/2 - 50, 20, 120)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_speed -=7
            if event.key == pygame.K_DOWN:
                player_speed += 7
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_speed += 7 
            if event.key == pygame.K_DOWN:
                player_speed -= 7

    screen.fill("black")
    cpu_score_surface = score_font.render(str(cpu_points), True, "white")
    player_score_surface = score_font.render(str(player_points), True, "white")
    screen.blit(cpu_score_surface,(screen_width/4,20))  
    screen.blit(player_score_surface,(3*screen_width/4,20)) 
    animate_ball()
    animate_player()
    animate_cpu()
    pygame.draw.ellipse(screen,"white",ball)
    pygame.draw.rect(screen, "white", player)
    pygame.draw.rect(screen, "white", opponent)
    pygame.draw.aaline(screen, "white", (screen_width/2, 0), (screen_width/2,screen_height))
    pygame.display.flip()
    clock.tick(60)