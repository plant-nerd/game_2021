import pygame
pygame.init()
dis = pygame.display.set_mode((800, 600))
pygame.display.update()
pygame.display.set_caption('Color Zone!!!!! XD')

yellow = (255, 255, 0)
pink = (255, 0, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
cyan = (0, 255, 255)
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
orange = (255, 140, 0)
purple = (150, 0, 255)
transparent = (100, 100, 100, 0.2)

game_over = False

x1 = 400
y1 = 300

x1_change = 0
y1_change = 0

clock = pygame.time.Clock()
color = pink

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -10
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = 10
            elif event.key == pygame.K_b:
                color = blue
            elif event.key == pygame.K_c:
                color = cyan
            elif event.key == pygame.K_p:
                color = pink
            elif event.key == pygame.K_r:
                color = red
            elif event.key == pygame.K_y:
                color = yellow
            elif event.key == pygame.K_w:
                color = white
            elif event.key == pygame.K_g:
                color = green
            elif event.key == pygame.K_e:
                color = black
            elif event.key == pygame.K_o:
                color = orange
            elif event.key == pygame.K_u:
                color = purple
            elif event.key == pygame.K_t:
                color = transparent
            ###elif event.key == pygame.K_1:
                #rainbow = True
                #count = 0
                #while rainbow == True:
                    #if count == 0:
                        #color = red
                        #count += 1
                    #elif count == 1:
                    #    color = orange
                     #   count += 1
                    #elif count == 2:
                     #   color = yellow
                      #  count += 1
                    #elif count == 3:
                     #   color = green
                      #  count += 1
                    #elif count == 4:
                     #   color = cyan
                      #  count += 1
                    #elif count == 5:
                     #   color = blue
                      #  count += 1
                    #elif count == 6:
                     #   color = purple
                      #  count += 1
                    #elif count == 7:
                     #   color = pink
                      #  count += 1
                    #elif count >= 8:
                     #   count = 0
                    ### ^This crashes the game
        if event.type == pygame.KEYUP:
            x1_change = 0
            y1_change = 0
    x1 += x1_change
    y1 += y1_change
    pygame.draw.circle(dis, color, (x1, y1), 50)
    pygame.display.update()

    clock.tick(30)

pygame.quit()
quit()