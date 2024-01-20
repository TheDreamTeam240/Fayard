import pygame
import sys

class Objet(pygame.sprite.Sprite):
    def __init__(self, image_path, nom):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.nom = nom

    def afficher_info(self):
        print(f"Nom: {self.nom}, Dégâts: {self.degats}")

class Arme(Objet):
    def __init__(self, image_path, nom, degats, portee):
        super().__init__(image_path, nom, degats)
        self.nom = nom
        self.portee = portee
        self.degats = degats

    def afficher_info(self):
        super().afficher_info()
        print(f"Portée: {self.portee}")

class Personnage(pygame.sprite.Sprite):
    def __init__(self, spritesheet, largeur_frame, hauteur_frame, x, y, vitesse):
        super().__init__()
        self.spritesheet = spritesheet
        self.largeur_frame = largeur_frame
        self.hauteur_frame = hauteur_frame
        self.frames = [spritesheet.subsurface((i * largeur_frame, 0, largeur_frame, hauteur_frame)) for i in range(4)]
        self.image = self.frames[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vitesse = vitesse
        self.frame_index = 0
        self.animation_active = False

    def update(self):
        if self.animation_active:
            self.frame_index = (self.frame_index + 1) % 4
            self.image = self.frames[self.frame_index]

def main():
    pygame.init()

    largeur, hauteur = 800, 600
    taille_fenetre = (largeur, hauteur)
    noir = (0, 0, 0)
    fenetre = pygame.display.set_mode(taille_fenetre)
    pygame.display.set_caption("Faille Arrrrrr")

    spritesheet = pygame.image.load("assets/camelot/lancelot_.png")

    joueur = Personnage(spritesheet, 30, 32, largeur // 2 - 30 // 2, hauteur // 2 - 32 // 2, 5)

    all_sprites = pygame.sprite.Group()
    all_sprites.add(joueur)

    clock = pygame.time.Clock()
    fps = 24

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        touches = pygame.key.get_pressed()
        if touches[pygame.K_LEFT] and joueur.rect.x > 0:
            joueur.rect.x -= joueur.vitesse
            joueur.animation_active = not joueur.animation_active
        if touches[pygame.K_RIGHT] and joueur.rect.x < largeur - joueur.largeur_frame:
            joueur.rect.x += joueur.vitesse
            joueur.animation_active = not joueur.animation_active
        if touches[pygame.K_UP] and joueur.rect.y > 0:
            joueur.rect.y -= joueur.vitesse
            joueur.animation_active = not joueur.animation_active
        if touches[pygame.K_DOWN] and joueur.rect.y < hauteur - joueur.hauteur_frame:
            joueur.rect.y += joueur.vitesse
            joueur.animation_active = not joueur.animation_active

        all_sprites.update()

        fenetre.fill(noir)
        all_sprites.draw(fenetre)
        pygame.display.flip()
        clock.tick(fps)

if __name__ == "__main__":
    main()
