import pygame

import random

# Initialisation de Pygame

pygame.init()

# Définition des couleurs

BLANC = (255, 255, 255)

NOIR = (0, 0, 0)

ROUGE = (255, 0, 0)

# Définition de la taille de l'écran

TAILLE_ECRAN = (640, 480)

# Création de la fenêtre

ecran = pygame.display.set_mode(TAILLE_ECRAN)

# Définition de la vitesse du serpent

VITESSE_SERPENT = 10

# Définition de la taille du serpent

TAILLE_SERPENT = 10

# Définition de la position initiale du serpent

position_serpent = [(TAILLE_ECRAN[0] / 2, TAILLE_ECRAN[1] / 2)]

# Définition de la direction initiale du serpent

direction_serpent = "droite"

# Définition de la position initiale de l'objet

position_objet = (random.randint(0, TAILLE_ECRAN[0] - TAILLE_SERPENT), 

                  random.randint(0, TAILLE_ECRAN[1] - TAILLE_SERPENT))

# Boucle principale du jeu

while True:

    # Gestion des événements

    for evenement in pygame.event.get():

        if evenement.type == pygame.QUIT:

            pygame.quit()

            quit()

        elif evenement.type == pygame.KEYDOWN:

            if evenement.key == pygame.K_LEFT and direction_serpent != "droite":

                direction_serpent = "gauche"

            elif evenement.key == pygame.K_RIGHT and direction_serpent != "gauche":

                direction_serpent = "droite"

            elif evenement.key == pygame.K_UP and direction_serpent != "bas":

                direction_serpent = "haut"

            elif evenement.key == pygame.K_DOWN and direction_serpent != "haut":

                direction_serpent = "bas"

    

    # Déplacement du serpent

    if direction_serpent == "gauche":

        nouvelle_position = (position_serpent[0][0] - VITESSE_SERPENT, position_serpent[0][1])

    elif direction_serpent == "droite":

        nouvelle_position = (position_serpent[0][0] + VITESSE_SERPENT, position_serpent[0][1])

    elif direction_serpent == "haut":

        nouvelle_position = (position_serpent[0][0], position_serpent[0][1] - VITESSE_SERPENT)

    elif direction_serpent == "bas":

        nouvelle_position = (position_serpent[0][0], position_serpent[0][1] + VITESSE_SERPENT)

    

    # Ajout de la nouvelle position au début de la liste

    position_serpent.insert(0, nouvelle_position)

    

    # Vérification si le serpent a mangé l'objet

    if position_serpent[0] == position_objet:

        position_objet = (random.randint(0, TAILLE_ECRAN[0] - TAILLE_SERPENT), 

                          random.randint(0, TAILLE_ECRAN[1] - TAILLE_SERPENT))

    else:

        # Suppression de la dernière position de la liste

        position_serpent.pop()

    

    # Affichage de l'écran

    ecran.fill(BLANC)

    

    # Affichage du serpent

    for position in position_serpent:

        pygame.draw.rect(ecran, NOIR, (position[0], position[1], TAILLE_SERPENT, TAILLE_SERPENT))

    

    # Affichage de l'objet

    pygame.draw.rect(ecran, ROUGE, (position_objet[0], position_objet[1], TAILLE_SERPENT, TAILLE_SERPENT))

    

    pygame.display.update()

