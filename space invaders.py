import pygame
import sys
pygame.init()
screen = pygame.display.set_mode((1520,780))
pygame.display.set_caption("screen")

yellow_bullets = []
red_bullets = []

health_yellow = 100
health_red = 100

font = pygame.font.SysFont("Arial",35)
fontend = pygame.font.SysFont("Arial",100)

speed = 2 

yellow_rect = pygame.Rect(50,350,70,70)
red_rect = pygame.Rect(1350,350,70,70)
divider = pygame.Rect(755,0,10,780)
#pygame.draw.rect(screen,"blue",yellow_rect)

end_rect = pygame.Rect(0,0,1520,780)


bg = pygame.image.load("space invaders/images space invaders/space background.png")
resize_bg = pygame.transform.scale(bg,(1520,780))
yellow_spaceship = pygame.image.load("space invaders/images space invaders/spaceship yellow.png")
rotate = pygame.transform.rotate(yellow_spaceship,90)
resize_yellow_spaceship = pygame.transform.scale(rotate,(70,70))
def draw():
     screen.blit(resize_bg,(0,0))
     screen.blit(resize_yellow_spaceship,(yellow_rect.x,yellow_rect.y))
     pygame.draw.rect(screen,"white",divider)
     for bullet in yellow_bullets:
          pygame.draw.rect(screen,"yellow",bullet)
     text_y = font.render("HEALTH " + str(health_yellow),True,"white")
     screen.blit(text_y,(10,10))
     for bullet in red_bullets:
          pygame.draw.rect(screen,"red",bullet)
     text_y = font.render("HEALTH " + str(health_red),True,"white")
     screen.blit(text_y,(1330,10))
     
def movement_yellow():
     global health_red
     keys = pygame.key.get_pressed()
     if keys[pygame.K_w] and yellow_rect.y > 0:
          yellow_rect.y = yellow_rect.y - speed
     if keys[pygame.K_a] and yellow_rect.x > 0:
          yellow_rect.x = yellow_rect.x - speed
     if keys[pygame.K_s] and yellow_rect.y < 710:
          yellow_rect.y = yellow_rect.y + speed
     if keys[pygame.K_d] and yellow_rect.x < 685:
          yellow_rect.x = yellow_rect.x + speed
     for bullet in yellow_bullets:
          bullet.x = bullet.x + 5
          if red_rect.colliderect(bullet):
               yellow_bullets.remove(bullet)
               health_red = health_red - 10
          elif bullet.x > 1520:
               yellow_bullets.remove(bullet)
     if health_red <= 0:
          pygame.draw.rect(screen,"black",end_rect)
          win_r = fontend.render("YELLOW WINS!",True,"yellow")
          screen.blit(win_r,(600,30))
  


red_spaceship = pygame.image.load("space invaders/images space invaders/spaceship red.png.png")
rotate_red = pygame.transform.rotate(red_spaceship,270 )
resize_red_spaceship = pygame.transform.scale(rotate_red,(70,70))
def draw2():
     screen.blit(resize_red_spaceship,(red_rect.x,red_rect.y))
     
def movement_red():
     global health_yellow
     keys = pygame.key.get_pressed()
     if keys[pygame.K_i] and red_rect.y > 0:
          red_rect.y = red_rect.y - speed
     if keys[pygame.K_j] and red_rect.x > 766:
          red_rect.x = red_rect.x - speed
     if keys[pygame.K_k] and red_rect.y < 710:
          red_rect.y = red_rect.y + speed
     if keys[pygame.K_l] and red_rect.x < 1450:
          red_rect.x = red_rect.x + speed
     for bullet in red_bullets:
          bullet.x = bullet.x - 5
          if yellow_rect.colliderect(bullet):
               red_bullets.remove(bullet)
               health_yellow = health_yellow - 10
          elif bullet.x < 0:
               red_bullets.remove(bullet)
     if health_yellow <= 0:
          pygame.draw.rect(screen,"black",end_rect)
          win_y = fontend.render("RED WINS!",True,"red")
          screen.blit(win_y,(600,30))
          





while True:
     draw()
     draw2()
     movement_yellow()
     movement_red()
     for event in pygame.event.get():
          if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_f and len(yellow_bullets) < 2:
                    bullet_y = pygame.Rect(yellow_rect.x + 77,yellow_rect.y + 32,17,7)
                    yellow_bullets.append(bullet_y)
               elif event.key == pygame.K_SEMICOLON and len(red_bullets) < 2:
                    bullet_r = pygame.Rect(red_rect.x - 20,red_rect.y + 32,17,7)
                    red_bullets.append(bullet_r)
          if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()
     pygame.display.update()





