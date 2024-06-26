import pygame 
pygame.init()
font =  pygame.font.Font('freesansbold.ttf', 24)
screen = pygame.display.set_mode([800, 500])
timer = pygame.time.Clock()
messages = ['write game backstory and context here'
            '(click enter to see next page)',
            'this is another page',
            'blaaa bla bla heeee heeeeeee']
snip = font.render('' , True, 'white')
counter = 0 
speed = 3
active_message = 0
message = messages[active_message]
done = False

run = True 
while run:
    screen.fill('black')
    timer.tick(60)
    # this is a box for the text, first two numbers are x y coordinate for the text, last two numbers are for the box sizes 
    # pygame.draw.rect(screen, 'black', [0, 0, 800, 200])
    if counter < speed * len(message):
        counter += 1
    elif counter >= speed*len(message):
        done = True 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and done and active_message < len(messages) -1:
                active_message += 1
                done = False
                message = messages[active_message]
                counter = 0

        
    snip = font.render(message[0:counter//speed], True, 'white')
    screen.blit(snip, (10, 10))
    pygame.display.flip()
pygame.quit()