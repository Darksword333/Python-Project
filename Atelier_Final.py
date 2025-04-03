# -*- coding: utf-8 -*-

###initialisation des grilles et autres variables de jeu
grille_debut_partie = [[" ", "1", "2", "3", "4", "5", "6", "7"],
                       ["A", "●", "●", "●", "●", "●", "●", "○"],
                       ["B", "●", "●", "●", "●", "●", "○", "○"],
                       ["C", "●", "●", "●", "●", "○", "○", "○"],
                       ["D", "●", "●", "●", " ", "○", "○", "○"],
                       ["E", "●", "●", "●", "○", "○", "○", "○"],
                       ["F", "●", "●", "○", "○", "○", "○", "○"],
                       ["G", "●", "○", "○", "○", "○", "○", "○"]]

grille_milieu_partie = [[" ", "1", "2", "3", "4", "5", "6", "7"],
                       ["A", "●", "●", "●", "●", "●", "●", "○"],
                       ["B", "●", "●", "●", "●", "●", "○", " "],
                       ["C", "●", "●", "●", "●", " ", " ", "○"],
                       ["D", "●", "●", " ", " ", "○", "○", "○"],
                       ["E", "●", " ", "●", "○", "○", "○", "○"],
                       ["F", "●", "●", "○", "○", "○", "○", "○"],
                       ["G", " ", "○", "○", "○", "○", "○", "○"]]

grille_fin_partie = [[" ", "1", "2", "3", "4", "5", "6", "7"],
                       ["A", "●", "●", "●", " ", "●", " ", " "],
                       ["B", "●", " ", " ", "●", " ", " ", " "],
                       ["C", "●", " ", " ", " ", " ", " ", " "],
                       ["D", " ", " ", " ", "●", " ", " ", " "],
                       ["E", " ", " ", " ", " ", " ", " ", "○"],
                       ["F", " ", " ", " ", "●", " ", "○", "○"],
                       ["G", " ", " ", " ", "○", "○", "○", "○"]]

from random import * #Pour que l'ia puisse faire un choix aléatoire

tour = 0

### REPRESENTATION GRAPHIQUE
def afficher_grille(grille) :
    resultat = ""
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            resultat += " " + grille[i][j] + " |"
        resultat += "\n"
    resultat +="    Joueur 1 = ●,   Joueur 2 = ○" + "\n"
    print(resultat)
    print(f"Pion du Joueur 1 restant : {nb_pion(grille)[0]} \nPion du Joueur 2 restant : {nb_pion(grille)[1]}")


### Fonction principale
def mare():
    rep = mode_de_jeux()
    if rep == "D":
        print('Fin du jeu')
        return True
    grille = choix_grille()
    afficher_grille(grille)
    if rep == "A":
        jcj_local(grille)
    elif rep == "B":
        partie_ordinateur(grille)

def jcj_local(grille):
    #Permet le déroulement de la partie en joueur contre joueur local
    global tour #Pour modifier les tours de jeu (il n'y a pas bcp de facon de l'initialiser obligé de faire une variable globale ou de le mettre en paramètre sur toutes les fonctions)
    while not est_fini_partie(nb_pion(grille)[0], nb_pion(grille)[1]):
        print("-----")
        print(f"C'est le tour du Joueur {tour_joueur(tour)}")
        print("-----")
        co1 = saisir_coordonnees(input("Veuillez saisir une coordonnée : "))
        co2 = saisir_coordonnees(input("Veuillez saisir la coordonnée d'arrivé : "))
        co1 = saisir_deplacement(co1, co2, grille)
        afficher_grille(grille)
        enchainement(co1, co2, grille)
        tour += 1
    if nb_pion(grille)[0] > nb_pion(grille)[1]:
        print("Le joueur 1 a gagné !!!")
        print(f"La partie s'est finis en {tour} tours.")
    elif nb_pion(grille)[0] < nb_pion(grille)[1]:
        print("Le joueur 2 a gagné !!!")
        print(f"La partie s'est finis en {tour} tours.")

def partie_ordinateur(grille):
    #Permet le déroulement de la partie en mode contre l'ordinateur
    global tour #Pour modifier les tours de jeu (il n'y a pas bcp de facon de l'initialiser obligé de faire une variable globale ou de le mettre en paramètre sur toutes les fonctions)
    valide = False
    rep = input("Voulez vous jouer en premier ? (y or n) : ")
    ordi = 0
    while not valide:
        if rep == 'y':
            rep = 1
            ordi = 2
            valide = True
        elif rep == 'n':
            rep = 2
            ordi = 2
            valide = True
        else:
            rep = input("Veuillez saisir une réponse valide. \nVoulez vous jouer en premier ? (y or n) : ")
    while not est_fini_partie(nb_pion(grille)[0], nb_pion(grille)[1]):
        if tour_joueur(tour) == rep:
            print("-----")
            print("C'est à vous de jouer")
            print("-----")
            co1 = saisir_coordonnees(input("Veuillez saisir une coordonnée : "))
            co2 = saisir_coordonnees(input("Veuillez saisir la coordonnée d'arrivé : "))
            co1 = saisir_deplacement(co1, co2, grille)
            afficher_grille(grille)
            enchainement(co1, co2, grille)
            tour += 1
        else:
            tour_ordinateur(ordi, grille)
            tour += 1
    if nb_pion(grille)[0] > nb_pion(grille)[1]:
        if rep == 1:
            print("Vous avez gagné !!!")
            print(f"La partie s'est finis en {tour} tours.")
        else:
            print("Vous avez perdu...")
            print(f"La partie s'est finis en {tour} tours.")
    elif nb_pion(grille)[0] < nb_pion(grille)[1]:
        if rep == 2:
            print("Vous avez gagné !!!")
            print(f"La partie s'est finis en {tour} tours.")
        else:
            print("Vous avez perdu...")
            print(f"La partie s'est finis en {tour} tours.")

def tour_ordinateur(numero, grille):
    #Permet à l'ordinateur de faire son tour
    for i in range(nb_pion[numero-1]):
        choix = randint(1,10)

def co_pion(joueur, grille):
    #Permet d'obtenir les coordonnées de tout les pions d'un joueur
    co = []
    if joueur == 1:
        for i in range(len(grille)):
            for j in range(len(grille[0])):
                if grille[i][j] == "●":
                    co.append((i,j))
    if joueur == 2:
        for i in range(len(grille)):
            for j in range(len(grille[0])):
                if grille[i][j] == "○":
                    co.append((i,j))
    return co

def mode_de_jeux():
    #Permet à l'utilisateur de choisir son mode de jeu
    rep = str(input("Quel mode de jeu voulez vous ? \n(Pour joueur contre joueur en local tapez A, pour joueur contre ordinateur tapez B, pour afficher les tests tapez C et pour annuler tapez D)\n").upper())
    valide = False
    while not valide:
        if rep == "A":
            valide = True
        elif rep == "B":
            valide = True
        elif rep == "C":
            test()
        elif rep == "D":
            valide = True
        else:
            print("Veuillez saisir A, B ou C pour choisir le mode de jeu")
    return rep

def choix_grille():
    #Permet à l'utilisateur de choisir sa grille
    rep = str(input("Quelle grille voulez vous ? \n(Pour celle du début tapez A, pour celle du milieu tapez B et pour celle de fin tapez C)\n").upper())
    valide = False
    while not valide:
        if rep == "A":
            grille_courante = grille_debut_partie
            valide = True
        elif rep == "B":
            grille_courante = grille_milieu_partie
            valide = True
        elif rep == "C":
            grille_courante = grille_fin_partie
            valide = True
        else:
            rep = str(input("Veuillez saisir A, B ou C pour choisir la grille : ").upper())
    return grille_courante

def enchainement(co1, co2, grille):
    #Permet d'effectuer les enchainements
    rep = " "
    while not co1 == False and est_possible_enchainement(co1, grille) and rep != "n" and not est_fini_partie(nb_pion(grille)[0], nb_pion(grille)[1]):
        rep = str(input("Voulez vous faire un enchainement ? \ny/n (oui tapez y, non tapez n.) : ").lower())
        if rep == "y":
            co2 = saisir_coordonnees(input("Veuillez saisir les coordonnées de votre enchainement :\n"))
            co1 = saisir_deplacement(co1, co2, grille, True)
            afficher_grille(grille)

def tour_joueur(tour):
    #Permet de savoir au tour de quel joueur nous sommes
    if tour%2 == 0:
        return 1
    elif tour%2 != 0:
        return 2

def conversion(co):
    #Permet de convertir les coordonnées utilisateur en indice si elles ne sont pas déjà converti
    new_co = []
    if len(co) == 2 and str(co[0]) in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        new_co = (ord(str(co[0]))-ord("A")+1, int(co[1]))
        co = new_co
    elif len(co) == 2 and str(co[0]) in 'abcdefghijklmnopqrstuvwxyz':
        new_co = (ord(str(co[0]))-ord("a")+1, int(co[1]))
        co = new_co
    return co

def nb_pion(grille):
    #Compte le nombre de pion de la grille
    pion_j1 = 0
    pion_j2 = 0
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            if grille[i][j] == "●": #Compte le nombre de pion du joueur 1
                pion_j1+=1
            elif grille[i][j] == "○": #Compte le nombre de pion du joueur 2
                pion_j2+=1
    return pion_j1, pion_j2

### Saisis
def saisir_coordonnees(co):
    #Permet de saisir une coordonnée, l'utilisateur saisi la coordonnée tant qu'elle n'est pas valide
    valide = False
    while not valide:
        if est_au_bon_format(co) and est_dans_grille(co):
            valide = True
        else:
            co = input("Veuillez saisir des coordonnées valide (respectant la grille, respectant les règles) : ")
    return conversion(co)

def saisir_deplacement(co1, co2, grille, enchainement=False):
    #Permet de saisir un déplacement, l'utilisateur saisi le déplacement tant qu'il n'est pas valide vérifie aussi si un enchainement est en cours pour un if (met en valeur par défaut false pour en faire un paramètre facultatif)
    valide = False
    co3 = []
    while not valide:
        if est_dans_grille(co1) and est_dans_grille(co2):
            if est_au_bon_joueur(co2, grille) and enchainement == True:
                co2 = input("Veuillez saisir des coordonnées du pion à sauter de votre enchainement : ")
            elif not est_au_bon_joueur(co1, grille) and enchainement == False:
                co1 = input("Veuillez saisir des coordonnées avec un pion vous appartenant : ")
                co2 = input("Veuillez saisir les coordonnées d'arrivées : ")
            elif co1 == co2:
                print("Veuillez saisir des coordonnées différentes")
                co1 = input("Veuillez resaisir les coordonnées de départ : ")
                co2 = input("Veuillez resaisir les coordonnées d'arrivées : ")
            elif est_possible_deplacement_simple(co1, co2, grille) and enchainement == False:
                co = deplacement_simple(co1, co2, grille)
                co = [conversion(co[0]), conversion(co[1])]
                grille[co[1][0]][co[1][1]] = grille[co[0][0]][co[0][1]]
                grille[co[0][0]][co[0][1]] = " "
                valide = True
            elif est_possible_deplacement_saut(co1, co2, grille):
                if deplacement_saut(co1, co2, grille, True) != False and est_libre(co3, grille):
                    co1 = conversion(co1)
                    co3 = deplacement_saut(co1, co2, grille)
                    grille[co3[0]][co3[1]] = grille[co1[0]][co1[1]]
                    grille[co1[0]][co1[1]] = " "
                    valide = True
                else:
                    print("Déplacement impossible ! (veuillez vérifier d'avoir bien compris les règles)")
                    co1 = input("Veuillez resaisir les coordonnées de départ : ")
                    co2 = input("Veuillez resaisir les coordonnées d'arrivée : ")
    return co3

### Fonction de déplacement
def deplacement_simple(co1, co2, grille):
    #Permet d'effectuer les déplacements simple
    valide = False
    co3 = [0, 0]
    while not valide:
        if not est_libre(co1, grille) and est_libre(co2, grille):
            valide = True
        elif est_libre(co1, grille) and est_libre(co2, grille):
            print("Coordonnée de départ invalide veuillez vérifier que la case de départ contient un pion")
            co1 = saisir_coordonnees(input("Veuillez resaisir les coordonnées de départ : "))
            co2 = saisir_coordonnees(input("Veuillez resaisir les coordonnées d'arrivée : "))
        elif not est_libre(co1, grille) and not est_libre(co2, grille):
            co3 = deplacement_saut(co1, co2, grille)
            saisir_deplacement(co1, co3, grille)
            valide = True
        else:
            print("Coordonnée de départ et d'arrivé invalide veuillez vérifier que la case de départ contient un pion et la case d'arrivé est libre")
            co1 = saisir_coordonnees(input("Veuillez resaisir les coordonnées de départ : "))
            co2 = saisir_coordonnees(input("Veuillez resaisir les coordonnées d'arrivée : "))
    return co1, co2

def deplacement_saut(co1, co2, grille, co=False):
    #Permet d'effectuer les déplacements saut avec prises
    co1 = conversion(co1)
    co2 = conversion(co2)
    co3 = est_possible_deplacement_saut(co1, co2, grille)[1]
    if est_possible_deplacement_saut(co1, co2, grille) and co == False:
        grille[co2[0]][co2[1]] = " "
    return co3

def respect_distance(co1, co2):
    #Permet de vérifier si la distance d'un déplacement est possible
    co1 = saisir_coordonnees(co1)
    co2 = saisir_coordonnees(co2)
    delta_ligne = co1[0]-co2[0]
    delta_colonne = co1[1]-co2[1]
    if delta_ligne == 0 and delta_colonne == 1:
        return True, "Droite"
    elif delta_ligne == 0 and delta_colonne == -1:
        return True, "Gauche"
    elif delta_ligne == 1 and delta_colonne == 0:
        return True, "Bas"
    elif delta_ligne == -1 and delta_colonne == 0:
        return True, "Haut"
    return False

### Test des inputs
def est_au_bon_format(co):
    #Vérifie si les coordonnées sont au bon format ou non
    if len(co) != 2:
        return False
    co = conversion(co)
    if int(co[0]) < 1 or int(co[0]) > 26 or int(co[1]) < 0 or int(co[1]) > 9:
        return False                                                                                                                                                                             
    return True

def est_dans_grille(co):
    #Vérifie si les coordonnées sont dans la grille ou non
    if len(co) != 2:
        return False
    co = conversion(co)
    if (ord(str(co[0])) < ord("1") or ord(str(co[0])) > ord("7")) or (int(co[1]) < 1 or int(co[1]) > 7): #Test si la coordonnée est valide (premiere partie contenue entre A et G seconde partie contenu entre 1 et 7)                                                                                                                                        
        return False
    return True

def est_possible_deplacement_simple(co1, co2, grille):
    #Vérifie si le déplacement est possible
    if est_libre(co2, grille) and respect_distance(co1, co2):
        return True
    return False

def est_possible_deplacement_saut(co1, co2, grille):
    #Vérifie si le déplacement saut avec prise est possible
    co1 = conversion(co1)
    co2 = conversion(co2)
    co3 = list(co2)
    if est_au_bon_joueur(co1, grille) and not est_libre(co2, grille) and respect_distance(co1, co2) and not est_au_bon_joueur(co2, grille):
        if respect_distance(co1, co2)[1] == "Haut":
            co3[0] = co3[0] + 1
            co3[1] = co3[1]
            return True, co3
        elif respect_distance(co1, co2)[1] == "Bas":
            co3[0] = co3[0] - 1
            co3[1] = co3[1]
            return True, co3
        elif respect_distance(co1, co2)[1] == "Gauche":
            co3[0] = co3[0]
            co3[1] = co3[1] + 1
            return True, co3
        elif respect_distance(co1, co2)[1] == "Droite":
            co3[0] = co3[0]
            co3[1] = co3[1] - 1
            return True, co3
    return False, False

def est_possible_enchainement(co, grille):
    #Vérifie si un enchainement est possible
    if co == []:
        return False
    if est_dans_grille((co[0]+2, co[1])):
        if not est_au_bon_joueur((co[0]+1, co[1]), grille) and est_libre((co[0]+2, co[1]), grille):
            return True
    if est_dans_grille((co[0]-2, co[1])):
        if not est_au_bon_joueur((co[0]-1, co[1]), grille) and est_libre((co[0]+2, co[1]), grille):
            return True
    if est_dans_grille((co[0], co[1]+2)):
        if not est_au_bon_joueur((co[0], co[1]+1), grille) and est_libre((co[0]+2, co[1]), grille):
            return True 
    if est_dans_grille((co[0], co[1]-2)):
        if not est_au_bon_joueur((co[0], co[1]-1), grille) and est_libre((co[0]+2, co[1]), grille):
            return True
    return False

def est_libre(co, grille):
    #Vérifie si la case actuelle est libre ou non
    co = conversion(co)
    if est_dans_grille(co):
        if grille[co[0]][co[1]] == "●" or  grille[co[0]][co[1]] == "○":
            return False
    return True

def est_au_bon_joueur(co, grille):
    #Vérifie si la case contient un pion qui est au bon joueur
    J1 = "●"
    J2 = "○"
    co = conversion(co)
    if grille[co[0]][co[1]] == J1 and tour_joueur(tour) == 1:
        return True
    elif grille[co[0]][co[1]] == J2 and tour_joueur(tour) == 2:
        return True
    return False

def est_fini_partie(x, o):
    #Vérifie si la partie est fini
    if x < 6:
        return True
    elif o < 6:
        return True
    return False

### Fonction de test
def test_est_au_bon_format():
    assert est_au_bon_format("A0") == True, "Test classique 1"
    assert est_au_bon_format("Z9") == True, "Test classique 2"
    assert est_au_bon_format("A22") == False, "Test erreur message trop long"
    print('OK est_au_bon_format')

def test_est_dans_grille():
    assert est_dans_grille("A1") == True, "Test classique 1"
    assert est_dans_grille("G7") == True, "Test classique 2"
    assert est_dans_grille("H7") == False, "Test classique 3"
    assert est_dans_grille("A22") == False, "Test erreur message trop long"
    print('OK est_dans_grille')

def test_est_possible_deplacement_simple():
    assert est_possible_deplacement_simple((5, 4), (4, 4), grille_debut_partie) == True, "Test classique 1"
    assert est_possible_deplacement_simple((4, 2), (4, 3), grille_milieu_partie) == True, "Test classique 2"
    assert est_possible_deplacement_simple((6, 4), (6, 3), grille_fin_partie) == True, "Test classique 3"
    print('OK est_possible_deplacement_simple')

def test_est_possible_deplacement_saut():
    #Nécessite la modification de la variable ligne 33 pour effectuer des bons tests
    assert est_possible_deplacement_saut((5, 3), (6, 3), grille_debut_partie)[0] == False, "Test classique 1"
    assert est_possible_deplacement_saut((5, 4), (5, 3), grille_milieu_partie)[0] == False, "Test classique 2"
    assert est_possible_deplacement_saut((7, 4), (6, 4), grille_fin_partie)[0] == False, "Test classique 3"
    print('OK est_possible_deplacement_saut')

def test_est_possible_enchainement():
    #Nécessite la modification de la variable ligne 33 pour effectuer des bons tests 
    assert est_possible_enchainement((5, 4), grille_debut_partie) == False, "Test classique 1"
    assert est_possible_enchainement((7, 2), grille_milieu_partie) == True, "Test classique 2"
    assert est_possible_enchainement((7, 4), grille_fin_partie) == True, "Test classique 3"
    print('OK est_possible_enchainement')

def test_est_libre():
    assert est_libre((4, 4), grille_debut_partie) == True, "Test classique 1"
    assert est_libre((1, 1), grille_milieu_partie) == False, "Test classique 2"
    assert est_libre((2, 3), grille_fin_partie) == True, "Test classique 3"
    print('OK est_libre')

def test_est_au_bon_joueur():
    #Nécessite la modification de la variable ligne 33 pour effectuer des bons tests
    assert est_au_bon_joueur((7, 7), grille_debut_partie) == False, "Test classique 1"
    assert est_au_bon_joueur((1, 1), grille_milieu_partie) == True, "Test classique 2"
    assert est_au_bon_joueur((2, 3), grille_fin_partie) == False, "Test case vide"
    print('OK est_au_bon_joueur')

def test_est_fini_partie():
    assert est_fini_partie(6, 5) == True, "Test classique 1"
    assert est_fini_partie(5, 6) == True, "Test classique 2"
    assert est_fini_partie(6, 6) == False, "Test case vide"
    print('OK est_fini_partie')

# Appel des fonctions de tests
def test():
    test_est_au_bon_format()
    test_est_dans_grille()
    test_est_possible_deplacement_simple()
    test_est_possible_deplacement_saut()
    test_est_possible_enchainement()
    test_est_libre()
    test_est_au_bon_joueur()
    test_est_fini_partie()
    print("Les test sont tous OK")

# Appel de la fonction de démarrage
mare()