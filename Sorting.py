import pygame
py = pygame

width,height = 1980,1080

py.init()
screen = py.display.set_mode((0,0),py.FULLSCREEN)
screen.fill(((66, 66, 88)))
py.display.set_caption('Rendezés')

font_1 = py.font.Font('fonts/Cocogoose-Pro-Light.ttf', 100)
main_text =  font_1.render('Lista rendezés', True, 'black')
main_text_rect = main_text.get_rect(center=(width/2,55))

sort_mode_btn = pygame.Surface((300,100))
sort_mode_btn_rect = sort_mode_btn.get_rect(center=(width/2,height/2))

running = True
while running:
    for event in pygame.event.get():
        if event.type == py.QUIT:
            running = False


    screen.blit(main_text,main_text_rect)
    py.display.update()
py.quit()