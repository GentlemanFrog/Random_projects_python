import pygame, sys, random


#source: https://www.youtube.com/watch?v=hDu8mcAlY4E
#arty z filmu i strony: opengameart.org, https://opengameart.org/content/shooting-gallery
#sprites in Pygame: A class that combines a surface, a react and many addityiona features like animations
#or sound

#klasa, która ma wypluć na ekran interesujacy nasz sprite
#musi dziedziczyć z pygame.sprite.Sprite
class Crosshair(pygame.sprite.Sprite):
    #inicjujemy podstawowe atrybuty, i dajemy tej kalsie atrybuty obiektu jaki chcemy:
    def __init__(self, picture_path):
        #metoda inicjująca obiekt: funkcja super zwraca obiekt który reprezentuje klase rodzica
        super().__init__()
        #ta funkcja potrzebuje tylko atrybutów położenia
        self.image = pygame.image.load(picture_path)
        #mamy image i teraz potrzebujemy prostokątu do jeog poruszania dokoła:
        #odwołujemy sie że powyzej wywoływany image ma mieć narysowany rectangle na nim
        self.rect = self.image.get_rect()
    def shoot(self):
        #funkcja wykrywa kolizje spritów i pozwala na dowolna manipulacje
        pygame.sprite.spritecollide(red_crosshair, dummy_group, True)
        #update słuzacy do ustawienia celownika na pozycje myszki
    def update(self):
        self.rect.center = pygame.mouse.get_pos()

class Target(pygame.sprite.Sprite):
    def __init__(self, target_picture_path, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(target_picture_path)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]


#general setup
#inicjacja pygame
pygame.init()
clock = pygame.time.Clock()

#setuping game screen:
screen_width = 1280
screen_height = 720
#activating screen on display
screen = pygame.display.set_mode((screen_width, screen_height))
#background:
background = pygame.image.load('bg_blue.png')
background = pygame.transform.scale(background, (1280, 720))
#ukrywanie myszki na celownik:
pygame.mouse.set_visible(False)

#wywołujemy obiekt naszej klasy rysujacej do stworznia obiektu, wymagane jest również podanie
#jego wszystkich atrybutów: width, height, koordynaty na ekranie, kolor w RGB
red_crosshair = Crosshair('crosshair_red_large.png')
#problem ze spritami jest taki że nie mozna ich wyświetlac indywidualnie tylko muszą byc wyswietlane
#w grupie która trzeba stworzyć:
red_rect_group = pygame.sprite.Group()
#następnie dodajemy nasz interesujący nasz obiekt do grupy:
red_rect_group.add(red_crosshair)
#do wyrywosowania potrzebna jest funkcja w pętli umożliwiająca rysownie spritów

#targets:
dummy_group = pygame.sprite.Group()
for dummy in range(10):
    new_dummy = Target('duck_target_yellow.png', random.randrange(0, screen_width), random.randrange(0, screen_height))
    dummy_group.add(new_dummy)




#main game loop:
while True:
    #wykrywanie wysątpienie eventu
    for event in pygame.event.get():
        #okreslenie wystąpienia eventu zamknięcia
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            red_crosshair.shoot()

    #wyrysowanie na ekranie czegokolwiek co sie zmieniło
    pygame.display.flip()
    #ustawienie tłą: nazwa pliku koordynaty gdzie chcemy nasze tło postawić (0,0)
    #określa położenie oryginalnej powierzchni
    screen.blit(background, (0,0))
    #funkcja umożliwiajaca rysowanie
    dummy_group.draw(screen)
    red_rect_group.draw(screen)
    red_rect_group.update()
    clock.tick(60)


