import pygame, sys, os, glob

#used asets: https://opengameart.org/content/opp2017-sprites-characters-objects-effects

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        #do prostej animacji tworzymy liste spritów, których zmiany
        #w czasie kontrolujemy
        #os pozwala nam bezpośrednio wczytac wszystkie sprity do listy (ale nie działą)
        #trzeba spróbowac brutalnie
        self.is_animating = False
        #Rada kolegi na wczytanie
        self.sprites_list = [pygame.image.load(img) for img in glob.glob('frog_sprites/*.png')]
        # self.sprites_list.append(pygame.image.load('C:/Users/Alek/Desktop/losowe_python/random_projects/animated_sprites/frog_sprites/attack_1.png'))
        # self.sprites_list.append(pygame.image.load('C:/Users/Alek/Desktop/losowe_python/random_projects/animated_sprites/frog_sprites/attack_2.png'))
        # self.sprites_list.append(pygame.image.load('C:/Users/Alek/Desktop/losowe_python/random_projects/animated_sprites/frog_sprites/attack_3.png'))
        # self.sprites_list.append(pygame.image.load('C:/Users/Alek/Desktop/losowe_python/random_projects/animated_sprites/frog_sprites/attack_4.png'))
        # self.sprites_list.append(pygame.image.load('C:/Users/Alek/Desktop/losowe_python/random_projects/animated_sprites/frog_sprites/attack_5.png'))
        # self.sprites_list.append(pygame.image.load('C:/Users/Alek/Desktop/losowe_python/random_projects/animated_sprites/frog_sprites/attack_6.png'))
        # self.sprites_list.append(pygame.image.load('C:/Users/Alek/Desktop/losowe_python/random_projects/animated_sprites/frog_sprites/attack_7.png'))
        # self.sprites_list.append(pygame.image.load('C:/Users/Alek/Desktop/losowe_python/random_projects/animated_sprites/frog_sprites/attack_8.png'))
        # self.sprites_list.append(pygame.image.load('C:/Users/Alek/Desktop/losowe_python/random_projects/animated_sprites/frog_sprites/attack_9.png'))
        # self.sprites_list.append(pygame.image.load('C:/Users/Alek/Desktop/losowe_python/random_projects/animated_sprites/frog_sprites/attack_10.png'))
        self.current_sprite = 0
        self.image = self.sprites_list[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def animate(self):
        self.is_animating = True


    def update(self, speed):
        if self.is_animating == True:
            #w celu spowolnienia animacji zaokrąglamy liczbe do int()
            self.current_sprite += speed

            if self.current_sprite >= len(self.sprites_list):
                self.current_sprite = 0
                self.is_animating = False
            self.image = self.sprites_list[int(self.current_sprite)]



#general setup:
pygame.init()
clock = pygame.time.Clock()

#screen:
screen_width = 200
screen_height = 200
screen = pygame.display.set_mode((screen_width, screen_height))
#ustawienie nagłówka ekranu
pygame.display.set_caption("Frog animation")

#grupowanie spritów:
frog_animation_group = pygame.sprite.Group()
#obiekty danej klasy mała literą
player = Player(10, 100)
frog_animation_group.add(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            player.animate()

    #drawing scene:
    screen.fill((0,0,0))
    #screen.blit(player, (100, 100))
    #gdzie ma być rysowana
    frog_animation_group.draw(screen)
    frog_animation_group.update(0.25)
    pygame.display.flip()
    clock.tick(60)